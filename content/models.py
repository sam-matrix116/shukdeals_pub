from django.db import models
from django.utils.translation import gettext as _

def aboutus_pictures_path(instance, filename):
    return 'aboutus_pictures/{}'.format(filename)

# Create your models here.
class Faq(models.Model):
    question = models.CharField(max_length=300, verbose_name=_("Question"))
    answer = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class About(models.Model):
    heading = models.CharField(max_length=100, null=True)
    description = models.TextField(null=True, blank=True)
    sub_heading = models.CharField(max_length=100, null=True)
    sub_description = models.TextField(null=True)
    team_heading = models.CharField(max_length=100, null=True)
    team_description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)


class AboutJourney(models.Model):
    icon = models.ImageField(max_length=256,upload_to=aboutus_pictures_path)
    counter = models.CharField(max_length=10)
    title = models.CharField(max_length=20)
    description = models.TextField()


class AboutTeam(models.Model):
    image = models.ImageField(max_length=256,upload_to=aboutus_pictures_path)
    name = models.CharField(max_length=30)
    designation = models.CharField(max_length=30)
    facebook_link = models.URLField()
    twitter_link = models.URLField()
    instagram_link = models.URLField()
    linkedin_link = models.URLField()



class TermsAndCondition(models.Model):
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class PrivacyPolicy(models.Model):
    description = models.TextField(default="", null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)


class ContactUs(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=17)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)