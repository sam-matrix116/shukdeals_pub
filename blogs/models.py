from django.db import models
from django.utils.translation import gettext as _
from account.models import MyUser

def blog_picture_path(instance, filename):
    return 'blog_pictures/{}/{}'.format(instance.user.id, filename)


# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)


NEWS_STATUS_TYPES = (
    ('pending','Pending'),
    ('published','Published'),
    ('draft','Draft')
)

class News(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    title = models.CharField(verbose_name=_("Title"), max_length=100)
    description = models.TextField(verbose_name=_("Write news and article"))
    feature_picture = models.ImageField(upload_to=blog_picture_path,verbose_name=_("Feature Picture"))
    status = models.CharField(max_length = 10, choices=NEWS_STATUS_TYPES, default='pending')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)