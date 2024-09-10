from django.db import models
from account.models import MyUser, BusinessCategory

# Create your models here.

def news_pic_path(instance, filename):
    return 'news_pics/{}/{}'.format(instance.user.id, filename)


STATUS_TYPES = (
   ('pending','Pending'),
   ('draft','Draft'),
   ('published','Published')
)

class News(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name="user_articles")
    title = models.CharField(max_length=256)
    description = models.TextField()
    image = models.ImageField(upload_to=news_pic_path)
    status = models.CharField(choices=STATUS_TYPES,max_length=20,default='pending')
    deleted = models.BooleanField(default=False)
    delete_requested = models.BooleanField(default=False)
    category = models.ForeignKey(BusinessCategory, on_delete=models.DO_NOTHING)
    is_popular = models.BooleanField(default=False)
    # popular = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)


