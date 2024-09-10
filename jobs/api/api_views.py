from jobs.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from jobs.api.serializers import *
from django.utils.translation import gettext as _
from rest_framework.permissions import IsAuthenticated
from shuktv.utils.customPermissionClass import IsNormalUser
from shuktv.utils.customPaginations import paginated_data
from django.db.models import Count
import calendar

class CreateJobView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        serializer = JobSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Job posting created successfully")
        })


class AllJobsListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')

        jobs = Job.objects.all().exclude(status='inactive')
        
        if pagination_on:
            return paginated_data(jobs,JobDetailSerializer,request,items_per_page)
        else:
            serializer = JobDetailSerializer(jobs, many = True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            }) 
   

class RecentJobListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        jobs = Job.objects.filter(user=request.user).exclude(status='inactive')
        return paginated_data(jobs,JobDetailSerializer,request,6)
    

class PastJobListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        jobs = Job.objects.filter(user=request.user,status='inactive')
        return paginated_data(jobs,JobDetailSerializer,request,6)
    

class UpdateJobView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request, job_id):

        try:
            job = Job.objects.get(id=job_id, user=request.user)
        except:
            return Response({
                "status":False,
                "message": _("Invalid Job")
            })
        
        serializer = JobSerializer(job, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Job updated successfully")
        })
    

class JobDetailView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, job_id):

        try:
            job = Job.objects.get(id=job_id)
        except:
            return Response({
                "status":False,
                "message": _("Invalid Job")
            })
        
        try:
            JobClick.objects.get(job=job,user=request.user)
        except:
            JobClick.objects.create(job=job,user=request.user)
        
        serializer = JobDetailSerializer(job, context={'request': request, 'user': request.user})
        
        return Response({
            'status': True,
            'data': serializer.data
        })
    

class DeleteJobView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request, job_id):

        try:
            job = Job.objects.get(id = job_id, user=request.user)
        except:
            return Response({
                'status': False,
                'message':_("Invalid Job")
            })

        job.delete()

        return Response({
            'status': True,
            'message':_("Job deleted successfully")
        })
    

class ResumeListView(APIView):
    
    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request):
        
        resumes = Resume.objects.filter(user=request.user, reuse=True)
        serializer = ResumeSerializer(resumes, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })


class ApplyJobView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self,request):

        try:
            job = Job.objects.get(id = request.data["job"])
        except:
            return Response({
                'status': False,
                'message':_("Invalid Job")
            })
        
        try:
            already_applied = Application.objects.get(job=job, user=request.user)
        except:
            already_applied = None

        if already_applied:
            return Response({
                "status": False,
                "message":_("You have already applied to this job")
            })
        
        if "file" not in request.data and "old_resume" not in request.data:
            return Response({
                "status": False,
                "message":_("Please send resume")
            })
        
        resume = None
        resume_serializer = None
        if "file" in request.data:
            resume_serializer = ResumeSerializer(data=request.data, context={'request': request})
            resume_serializer.is_valid(raise_exception=True)
            
        elif "resume" in request.data:
            try:
                resume = Resume.objects.get(id=request.data["resume"],user=request.user)
            except:
                return Response({
                    'status': False,
                    'field': request.data["resume"],
                    'message':_("Invalid resume")
                })

        application_serializer = ApplicationSerializer(data=request.data, context={'request':request})
        application_serializer.is_valid(raise_exception=True)
        if "file" in request.data:
            resume = resume_serializer.save()
        application = application_serializer.save()
        application.resume = resume
        application.save()

        if "save_for_future" not in request.data:
            resume.reuse = False
            resume.save()

        return Response({
            'status': True,
            'message':_("Your job application is saved successfully")
        })
    

class JobStatisticsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, job_id):

        if "month" not in request.data:
            return Response({
                "status": False,
                "field": "month",
                "message":_("Month is required")
            })
        
        if "year" not in request.data:
            return Response({
                "status": False,
                "field": "year",
                "message":_("Year is required")
            })
        
        try:
            job = Job.objects.get(id=job_id)
        except:
            return Response({
                "status": False,
                "message":_("Invalid Job")
            })
        
        year = request.data["year"]
        month = request.data["month"]

        if month < 10:
            month_str = '0'+str(month)
        else:
            month_str = str(month)
        
        job_clicks = JobClick.objects.filter(job=job,created_at__year = year, created_at__month=month).values('created_at__date').order_by('created_at__date').annotate(total=Count('id'))
        
        found_dates = {}
        for click in job_clicks:
            found_dates[click['created_at__date'].strftime("%Y-%m-%d")] = click['total']

        all_date_clicks = {}

        date_range = calendar.monthrange(year,month)
        last_date = date_range[1]


        from datetime import datetime
        
        for i in range(1,last_date):
            if i < 10:
                i = '0'+str(i)
            current_date = str(year)+"-"+month_str+"-"+str(i)
            datetime_object = datetime.strptime(current_date, '%Y-%m-%d')
            short_current_date = datetime_object.strftime("%b%d")
            if current_date in found_dates:
                all_date_clicks[short_current_date] = found_dates[current_date]
            else:
                all_date_clicks[short_current_date] = 0

        return Response({
            "status": True,
            "data": all_date_clicks
        })
    

class JobApplicantsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request, job_id):

        try:
            job = Job.objects.get(id=job_id)
        except:
            return Response({
                "status": False,
                "message":_("Invalid Job")
            })
        
        applicants = job.job_applications.filter(job=job, deleted=False)
        serializer = ApplicationSerializer(applicants, many=True)

        return Response({
            "status": True,
            "data": serializer.data
        })


class DeleteJobApplicantView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self,request):

        job_id = request.data["job_id"]
        user_id = request.data["user_id"]

        try:
            job = Job.objects.get(id=job_id,user = request.user)
        except:
            return Response({
                "status": False,
                "message":_("Invalid Job")
            })

        try:
            application = Application.objects.get(job_id=job_id,user_id=user_id, deleted=False)
        except:
            return Response({
                "status": False,
                "message":_("Invalid Application")
            })
        
        application.deleted = True
        application.save()

        return Response({
            "status": True,
            "message": _("Application deleted successfully")
        })
    

class AddRemoveFavouriteJobView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, job_id):

        try:
            job = Job.objects.get(id = job_id)
        except:
            return Response({
                'status': False,
                'message':_("This Job does not exist.")
            })

        if job in request.user.favourite_job.all():
            request.user.favourite_job.remove(job)
            status = "removed from"
        else:
            request.user.favourite_job.add(job)
            status = "added to"

        return Response({
            'status': True,
            'message': _("Job {} favourite.").format(status)
        })