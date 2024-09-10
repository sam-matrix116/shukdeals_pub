from django.db import models
from account.models import MyUser, Location
from django.utils.translation import gettext as _

def classified_images(instance, filename):
    return 'classified_images/user_{}/{}'.format(instance.classified.user_id, filename)

PRICE_TYPE = (
   ('monthly',_("Monthly")),
   ('quarterly',_("Quarterly")),
   ('yearly',_("Yearly"))
)

PRODUCT_CONDITION_CHOICES = (
    ('new','New'),
    ('old', 'Old')
)

class ClassifiedCategory(models.Model):
    name = models.CharField(max_length=50)
    name_es = models.CharField(max_length=50, null=True)
    name_fr = models.CharField(max_length=50, null=True)
    name_he = models.CharField(max_length=50, null=True)
    name_ru = models.CharField(max_length=50, null=True)
    name_ar = models.CharField(max_length=50, null=True)
    name_pt = models.CharField(max_length=50, null=True)
    name_de = models.CharField(max_length=50, null=True)

# Create your models here.
class Classified(models.Model):
   user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
   category = models.ForeignKey(ClassifiedCategory, on_delete=models.SET_NULL, null=True)
   title = models.CharField(max_length=100, verbose_name=_('Title'))
   description = models.TextField(verbose_name=_('Description'))
   price_type = models.CharField(choices=PRICE_TYPE, max_length=20)
   price = models.FloatField(verbose_name=_('Price'))
   shuk_fee = models.FloatField(default=0.0)
   ngo_fee = models.FloatField(default=0.0)
   location = models.ForeignKey(Location, null=True,blank=True, on_delete=models.CASCADE,related_name='location_classified')
   contact_phone = models.CharField(max_length=17, blank=True, null=True, verbose_name=_("Contact Phone"))
   contact_email = models.EmailField(blank=True, null=True, verbose_name=_("Contact Email"))
   expiry_date = models.DateField()
   is_deleted = models.BooleanField(default=False)
   active = models.BooleanField(default=True)
   pinned = models.BooleanField(default=False)
   paid = models.BooleanField(default=False)
   created_at = models.DateTimeField(auto_now_add=True)
   product_condition = models.CharField(max_length=3, default='new', choices=PRODUCT_CONDITION_CHOICES)
   updated_at = models.DateTimeField(auto_now=True)


class ClassifiedImage(models.Model):
   classified = models.ForeignKey(Classified,on_delete=models.CASCADE, related_name="classified_images")
   image = models.ImageField(upload_to=classified_images)
   created_at = models.DateTimeField(auto_now_add=True)


class Flagged(models.Model):
    classified = models.ForeignKey(Classified,on_delete=models.CASCADE, related_name='classified_flags')
    flagged_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='classified_flaggers')
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ClassifiedClick(models.Model):
    classified = models.ForeignKey(Classified,on_delete=models.CASCADE, related_name='classified_clicks')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='classified_clickers')
    created_at = models.DateTimeField(auto_now_add=True)