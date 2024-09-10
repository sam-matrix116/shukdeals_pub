from django.db import models
from django.utils.translation import gettext as _
from account.models import MyUser, CURRENCIES_ALLOWED


def resume_files_path(instance, filename):
    return "resumes/{}/{}".format(instance.user.id, filename)

# Create your models here.

STATUS_TYPES = (
   ('active','Active'),
   ('inactive','Inactive'),
   ('payment_pending','Payment Pending')
)

JOB_TYPES = (
   ('full_time','Full Time'),
   ('part_time','Part Time')
)

SALARY_TYPES = (
   ('monthly','Monthly'),
   ('yearly','Yearly')
)

class Job(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=100, verbose_name=_('Job Title'))
    description = models.TextField(verbose_name=_('Job Description'))
    roles_and_responsibilities = models.TextField(verbose_name=_("Roles and Responsibilities"))
    job_type = models.CharField(verbose_name=_("Job Type"), max_length=20,choices=JOB_TYPES)
    salary = models.IntegerField()
    salary_currency = models.CharField(choices=CURRENCIES_ALLOWED, max_length=5, default="usd")
    salary_type = models.CharField(verbose_name=_("Salary Type"), max_length=20,choices=SALARY_TYPES, default="monthly")
    status = models.CharField(choices=STATUS_TYPES,max_length=20,default='active')
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    expiry_date = models.DateField(null=True)


class Resume(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name="resumes")
    file = models.FileField(upload_to=resume_files_path)
    reuse = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)


class Application(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_applications")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    phone = models.CharField(max_length=17)
    email = models.EmailField(max_length=200)
    resume = models.ForeignKey(Resume, on_delete=models.SET_NULL, null=True)
    deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)


class JobClick(models.Model):
    job = models.ForeignKey(Job, on_delete=models.CASCADE, related_name="job_clicks")
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)