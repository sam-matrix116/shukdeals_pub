from rest_framework.views import APIView
from article.api.serializers import *
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from shuktv.utils.customPermissionClass import IsNormalUser
from shuktv.utils.customPaginations import paginated_data
from django.utils.translation import gettext as _
from django.db.models import Q


class CreateNewsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)
    
    def post(self, request):

        serializer = NewsSerializer(data=request.data, context={'request':request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            "status": True,
            "data": serializer.data,
            'message': _("News article created successfully")
        })


class OthersNewsListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        news = News.objects.filter(deleted = False).exclude(user=request.user)

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            news = news.filter(Q(title__icontains = search_key)|Q(description__icontains = search_key))

        month = self.request.GET.get('month')
        year = self.request.GET.get('year')

        if month and year:
            news = news.filter(created_at__year = year, created_at__month=month).order_by('-created_at')

        search_by_category = self.request.GET.get('search_by_category')
        if search_by_category and search_by_category != '':
            news = news.filter(category = search_by_category)
        # search end

        return paginated_data(news,NewsSerializer,request,16)


class MyNewsListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        news = News.objects.filter(deleted = False, user=request.user)

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            news = news.filter(Q(title__icontains = search_key)|Q(description__icontains = search_key))
        # search end

        return paginated_data(news,NewsSerializer,request,16)
    

class UpdateNewsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request, news_id):

        try:
            news = News.objects.get(id=news_id, user=request.user, deleted = False)
        except:
            return Response({
                "status":False,
                "message": _("Invalid News")
            })
        
        serializer = NewsSerializer(news, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("News updated successfully")
        })
    

class NewsDetailView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, news_id):

        try:
            news = News.objects.get(id=news_id, deleted = False)
        except:
            return Response({
                "status":False,
                "message": _("Invalid News")
            })
        
        serializer = NewsDetailSerializer(news, context={'request': request, 'user': request.user})
        
        return Response({
            'status': True,
            'data': serializer.data
        })
    

class DeleteNewsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request, news_id):

        try:
            news = News.objects.get(id = news_id, user=request.user, delete_requested = False, deleted = False)
        except:
            return Response({
                'status': False,
                'message':_("Invalid News")
            })

        news.delete_requested = True
        news.save()

        return Response({
            'status': True,
            'message':_("News delete requested successfully")
        })
  