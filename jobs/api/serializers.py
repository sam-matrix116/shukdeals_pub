from rest_framework import serializers
from jobs.models import *
import datetime
from django.utils.translation import gettext as _
from account.api.serializers import CreatorProfileSerializer


class JobSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Job
        fields = '__all__'

    def validate(self,attrs):

        expiry_date = attrs.get('expiry_date', '')

        if not expiry_date:
            raise serializers.ValidationError({
                "expiry_date": _("Expiry date is required")
            })
        
        today = datetime.datetime.now().date()
        expiry_date = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d").date()

        if expiry_date <= today:
            raise serializers.ValidationError({
                "expiry_date": _("Expiry date should be greater than today")
            })

        return attrs
    

class JobDetailSerializer(serializers.ModelSerializer):

    user_details = serializers.SerializerMethodField()
    total_applications = serializers.SerializerMethodField()
    total_clicks = serializers.SerializerMethodField()
    job_type = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()

    class Meta:
        model = Job
        fields = '__all__'

    def get_user_details(self,job):

        serializer = CreatorProfileSerializer(job.user, context={'user': self.context.get('user')})
        return serializer.data
    
    def get_total_applications(self, job):
        return job.job_applications.all().count()
    
    def get_total_clicks(self, job):
        return job.job_clicks.all().count()
    
    def get_job_type(self, job):

        return job.get_job_type_display()
    
    def get_added_to_wishlist(self, job):
        
        user = self.context.get('user')
        fav_jobs = [job.id for job in user.favourite_job.all()]
        if job.id in fav_jobs:
            return True
        
        return False
    

class ResumeSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Resume
        fields = '__all__'


class ApplicationSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    user_image = serializers.SerializerMethodField()
    resume = serializers.SerializerMethodField()

    class Meta:
        model = Application
        fields = '__all__'

    def get_user_image(self, application):
        return application.user.image.url
    
    def get_resume(self, application):

        serializer = ResumeSerializer(application.resume)
        return serializer.data