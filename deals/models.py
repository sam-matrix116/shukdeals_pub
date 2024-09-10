from django.db import models
from django.utils.translation import gettext as _
from account.models import MyUser, Location, BusinessCategory
from django.core.validators import MaxValueValidator, MinValueValidator


def deal_images(instance, filename):
    return 'deals_images/{}/{}/{}'.format(instance.deal.user.id, instance.id, filename)


# Create your models here.
DISCOUNT_TYPE_CHOICES = (
   ('fixed',_('Fixed Amount')),
   ('percentage',_('Percentage Off'))
)

DEAL_TYPE_CHOICES = (
   ('online',_('Online')),
   ('offline',_('Offline')),
   ('online_offline',_('Online Offline'))
)

DEAL_STATUS_CHOICES = (
   ('active', 'Active'),
   ('payment_pending', 'Payment Pending')
)

PROPERTY_CLASSES = (
   ('1', '1 Star'),
   ('2', '2 Star'),
   ('3', '3 Star'),
   ('4', '4 Star'),
   ('5', '5 Star')
)

class Deal(models.Model):
   user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
   title = models.CharField(max_length=100, verbose_name=_('Title'))
   description = models.TextField(verbose_name=_('Description'))
   actual_price = models.FloatField(verbose_name=_('Actual Price'), default=0)

   shuk_fee = models.FloatField(default=0.0)
   ngo_fee = models.FloatField(default=0.0)

   online_supported = models.BooleanField(default=True)
   deal_type = models.CharField(max_length=20,choices=DEAL_TYPE_CHOICES, default='online',verbose_name=_('Deal Type'))
   redemption_link = models.TextField(null=True)

   business_sub_category = models.ForeignKey(BusinessCategory, on_delete=models.SET_NULL, null=True, related_name="sub_category_deals")
   business_sub_sub_category = models.ForeignKey(BusinessCategory, on_delete=models.SET_NULL, null=True, related_name="sub_sub_category_deals")
   
   free_member_discount_type = models.CharField(max_length=20,choices=DISCOUNT_TYPE_CHOICES,verbose_name=_('Discount Type'), null=True)
   free_member_discount_value = models.FloatField(verbose_name=_('Off Value'), null=True)
   free_member_code = models.CharField(max_length=20,verbose_name=_('Coupon/Deal Code'), null=True)

   club_member_discount_type = models.CharField(max_length=20,choices=DISCOUNT_TYPE_CHOICES,verbose_name=_('Discount Type'), null=True)
   club_member_discount_value = models.FloatField(verbose_name=_('Off Value'), null=True)
   club_member_code = models.CharField(max_length=20,verbose_name=_('Coupon/Deal Code'), null=True)
   
   weekly = models.BooleanField(default=False,verbose_name=_("Weekly Deal"))
   location = models.ForeignKey(Location, null=True,blank=True, on_delete=models.CASCADE,related_name='location_deal')

   status = models.CharField(choices=DEAL_STATUS_CHOICES, default='payment_pending', max_length=20)

   is_deleted = models.BooleanField(default=False)
   active = models.BooleanField(default=True)
   paid = models.BooleanField(default=False)

   property_class = models.CharField(max_length=100, null=True, choices=PROPERTY_CLASSES)
   number_of_travellers = models.IntegerField(default=0)

   expiry_date = models.DateField(null=True)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField(auto_now=True)

   all_stores = models.BooleanField(default=False)

   parent = models.ForeignKey("self", on_delete=models.SET_NULL, null=True)

   def get_location(self):
      if self.location:
         return self.location.address+", "+self.location.city+", "+self.location.state+", "+self.location.country+", "+str(self.location.zipcode)

      return ''

class DealImage(models.Model):
   deal = models.ForeignKey(Deal,on_delete=models.CASCADE, related_name="deal_images")
   image = models.ImageField(upload_to=deal_images)
   created_at = models.DateTimeField(auto_now_add=True)


PROPERTY_TYPES = (
   ('apartment',_('Apartment')),
   ('house',_('House')),
   ('hotel',_('Hotel')),
   ('guest_house',_('Guest House')),
   ('hostel_pg',_('Hostel/PG')),
   ('farmhouse',_('Farmhouse')),
   ('houseboat',_('Houseboat')),
)

PRICE_TYPES = (
   ('monthly', _('Monthly')),
   ('yearly',_('Yearly')),
)

class PropertyDetails(models.Model):
   deal = models.OneToOneField(Deal, related_name='property_detail', on_delete=models.CASCADE)
   property_type = models.CharField(choices=PROPERTY_TYPES, max_length=24)
   offer_text = models.TextField(null=True)
   price_type = models.CharField(choices=PRICE_TYPES, max_length=24, null=True)
   price = models.FloatField(default=0)
   phone = models.CharField(verbose_name=_("Phone Number"), max_length=17, null=True)
   email = models.EmailField(verbose_name=_("Email"), null=True)
   rent_period = models.PositiveSmallIntegerField(null=True)
   no_of_bedroom = models.IntegerField(null=True)
   no_of_bathroom = models.IntegerField(null=True)
   sq_feet = models.IntegerField(null=True)


class Order(models.Model):
   deal = models.ForeignKey(Deal, on_delete=models.CASCADE)
   created_at = models.DateTimeField(auto_now_add=True)
   updated_at = models.DateTimeField()


STATUS_TYPES = (
   ('paid',_('Paid')),
   ('failed',_('Failed'))
)

class Payment(models.Model):
   order = models.ForeignKey(Order, on_delete=models.CASCADE)
   amount = models.FloatField()
   description = models.TextField()
   status = models.CharField(choices=STATUS_TYPES,max_length=20)
   created_at = models.DateTimeField(auto_now_add=True)


class Review(models.Model):
    deal = models.ForeignKey(Deal,on_delete=models.CASCADE, related_name='deal_reviews')
    reviewed_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='deal_reviewers')
    rating = models.FloatField(validators=[MinValueValidator(0.0), MaxValueValidator(5.0)],)
    comment = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewMark(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='useful_markers')
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='useful_marked')
    mark_type = models.BooleanField()
    created_at = models.DateTimeField(auto_now_add=True)


class ReviewFlag(models.Model):
    user = models.ForeignKey(MyUser,on_delete=models.CASCADE, related_name='deal_review_flaggers')
    review = models.ForeignKey(Review,on_delete=models.CASCADE, related_name='deal_flagged_reviews')
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class DealRedeem(models.Model):
   deal = models.ForeignKey(Deal,on_delete=models.DO_NOTHING, related_name="redeemed_deals")
   user = models.ForeignKey(MyUser, on_delete=models.DO_NOTHING, related_name="redeemed_by")
   created_at = models.DateTimeField(auto_now_add=True)


class Flagged(models.Model):
    deal = models.ForeignKey(Deal,on_delete=models.CASCADE, related_name='deal_flags')
    flagged_by = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='deal_flaggers')
    reason = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

   
class DealClick(models.Model):
    deal = models.ForeignKey(Deal,on_delete=models.CASCADE, related_name='deal_clicks')
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE, related_name='deal_clickers')
    created_at = models.DateTimeField(auto_now_add=True)