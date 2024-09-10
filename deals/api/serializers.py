from rest_framework import serializers
from deals.models import *
import datetime
from django.utils.translation import gettext as _
from account.utils import convert_currency as __
from account.api.serializers import LocationSerializer, CreatorProfileSerializer, UserProfileSerializer
from django.db.models import Avg


class DealImageSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = DealImage
        fields = '__all__'


class BusinessDealSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = serializers.SerializerMethodField()
    actual_price = serializers.SerializerMethodField()
    free_member_discount_value = serializers.SerializerMethodField()
    club_member_discount_value = serializers.SerializerMethodField()
    business_category = serializers.SerializerMethodField()
    avg_rating = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    is_redeemed = serializers.SerializerMethodField()
    total_redeemed = serializers.SerializerMethodField()
    creator_details = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    is_flagged = serializers.SerializerMethodField()
    property_details = serializers.SerializerMethodField()
    total_clicks = serializers.SerializerMethodField()
    
    class Meta:

        model = Deal
        fields = '__all__'
        extras = ('images','business_category','avg_rating','added_to_wishlist','total_redeemed','creator_details','location','is_redeemed','is_flagged','property_details','total_clicks')

    def get_images(self, deal):
        serializer = DealImageSerializer(deal.deal_images, many=True)
        return serializer.data
    
    def get_actual_price(self,deal):
        to_currency = self.context.get('to_currency')
        return __(deal.actual_price,deal.user.currency.iso_code, to_currency)
    
    def get_free_member_discount_value(self,deal):
        to_currency = self.context.get('to_currency')
        if deal.free_member_discount_type == 'fixed':
            return __(deal.free_member_discount_value,deal.user.currency.iso_code, to_currency)
        else:
            return deal.free_member_discount_value
        
    def get_club_member_discount_value(self,deal):
        to_currency = self.context.get('to_currency')
        if deal.club_member_discount_type == 'fixed':
            return __(deal.club_member_discount_value,deal.user.currency.iso_code, to_currency)
        else:
            return deal.club_member_discount_value
        
    def get_business_category(self,deal):
        if deal.user.business_category:
            return deal.user.business_category.name
        
    def get_avg_rating(self,deal):
        review = Review.objects.filter(deal=deal).aggregate(Avg("rating"))
        if review['rating__avg']:
            return review['rating__avg']
        return 0
    
    def get_added_to_wishlist(self, deal):
        
        user = self.context.get('user')

        if user and not user.is_anonymous:
            fav_deals = [deal.id for deal in user.favourite_deal.all()]
            if deal.id in fav_deals:
                return True
        
        return False
    
    def get_total_redeemed(self, deal):
        return deal.redeemed_deals.all().count()
    
    def get_creator_details(self,job):

        serializer = CreatorProfileSerializer(job.user, context={'user': self.context.get('user')})
        return serializer.data
    
    def get_location(self, deal):
        print('deal.location',deal.location)
        if deal.location:
            location = Location.objects.filter(id = deal.location.id).first()
            serializer = LocationSerializer(location)
            return serializer.data
        return ''
    
    def get_is_redeemed(self, deal):
        
        user = self.context.get('user')

        if user and not user.is_anonymous:
            try:
                redeemed = DealRedeem.objects.filter(user=user, deal=deal).last()
            except:
                return False
            
            if redeemed:
                return True

        return False
    
    def get_is_flagged(self, deal):
        
        logged_user = self.context.get('user')
        if not logged_user.is_anonymous:
            try:
                flagged = Flagged.objects.get(deal=deal, flagged_by=logged_user)
            except:
                return False
            
            if flagged:
                return True
        
        return False
    
    def get_property_details(self, deal):
        
        try:
            property_detail = deal.property_detail
        except:
            return ""
        
        if property_detail:
            to_currency = self.context.get('to_currency')
            serializer = PropertyDetailSerializer(property_detail,context={'to_currency':to_currency})
            return serializer.data
        
    def get_total_clicks(self, deal):
        clicks = DealClick.objects.filter(deal=deal).count()
        return clicks


class CreateBusinessDealSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    images = serializers.SerializerMethodField()
    business_category = serializers.SerializerMethodField()
    

    class Meta:

        model = Deal
        extras = ('images','business_category')
        exclude = ('location',)

    def get_images(self, deal):
        serializer = DealImageSerializer(deal.deal_images, many=True)
        return serializer.data
    
    
    def get_business_category(self,deal):
        if deal.user.business_category:
            return deal.user.business_category.name

    def validate(self,attrs):

        # regular deal restrictions
        weekly = attrs.get('weekly', '')
        online_supported = attrs.get('online_supported', '')
        deal_type = attrs.get('deal_type', '')
        redemption_link = attrs.get('redemption_link', '')
        actual_price = attrs.get('actual_price', '')
        expiry_date = attrs.get('expiry_date', '')
        free_member_discount_type = attrs.get('free_member_discount_type', '')
        free_member_discount_value = attrs.get('free_member_discount_value', '')
        free_member_code = attrs.get('free_member_code', '')
        club_member_discount_type = attrs.get('club_member_discount_type', '')
        club_member_discount_value = attrs.get('club_member_discount_value', '')
        club_member_code = attrs.get('club_member_code', '')

        if not actual_price:
            raise serializers.ValidationError({
                "actual_price": _("Actual price is required")
            })
        
        if not free_member_discount_type:
            raise serializers.ValidationError({
                "free_member_discount_type": _("Free member discount type is required")
            })
        
        if not free_member_discount_value:
            raise serializers.ValidationError({
                "free_member_discount_value": _("free_member_discount_value is required")
            })
        
        if not free_member_code:
            raise serializers.ValidationError({
                "free_member_code": _("Free member code is required")
            })

        if not weekly:
            if not expiry_date:
                raise serializers.ValidationError({
                    "expiry_date": _("Expiry date is required")
                })
            if not club_member_discount_type:
                raise serializers.ValidationError({
                    "club_member_discount_type": _("Club member discount type is required")
                })
            if not club_member_discount_value:
                raise serializers.ValidationError({
                    "club_member_discount_value": _("Club member discount value is required")
                })
            if not club_member_code:
                raise serializers.ValidationError({
                    "club_member_code": _("Club member code is required")
                })
        
            today = datetime.datetime.now().date()
            expiry_date = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d").date()

            if expiry_date <= today:
                raise serializers.ValidationError({
                    "expiry_date": _("Expiry date should be greater than today")
                })
            
        if not online_supported:
            if deal_type == 'online' or deal_type == 'online_offline':
                raise serializers.ValidationError({
                    "online_supported": _("Online deal not supported. Please select online supported to add online deals.")
                })
            
        if (deal_type == 'online' or deal_type == 'online_offline') and not redemption_link:
            
            raise serializers.ValidationError({
                "redemption_link": _("Redemption link is required.")
            })
        


        return attrs


class PropertySerializer(serializers.ModelSerializer):

    class Meta:

        model = PropertyDetails
        fields = ('property_type','offer_text','price_type','price','phone','email','no_of_bedroom','no_of_bathroom','sq_feet','rent_period')

    

class PropertyDetailSerializer(serializers.ModelSerializer):

    price = serializers.SerializerMethodField()
    property_type = serializers.SerializerMethodField()
    property_type_key = serializers.SerializerMethodField()

    class Meta:

        model = PropertyDetails
        fields = ('property_type_key','property_type','offer_text','price_type','price','phone','email','no_of_bedroom','no_of_bathroom','sq_feet','rent_period')

    def get_price(self,property):
        to_currency = self.context.get('to_currency')
        if property.price:
            return __(property.price,property.deal.user.currency.iso_code, to_currency)
        
        return 0
    
    def get_property_type(self,property):
        return _(property.get_property_type_display())
    
    def get_property_type_key(self,property):
        return property.property_type




class CreatePropertyDealSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location = serializers.SerializerMethodField()
    property_details = serializers.SerializerMethodField()

    class Meta:

        model = Deal
        fields = (
            'id','title','description','expiry_date','user',
            'property_details','location',
            'free_member_discount_type', 'free_member_discount_value', 'free_member_code', 
            'club_member_discount_type','club_member_discount_value', 'club_member_code',
            'business_sub_category','deal_type','online_supported','redemption_link'
        )

    def validate(self,attrs):

        # regular deal restrictions
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
    
    def get_property_details(self, deal):
        to_currency = self.context.get('to_currency')
        serializer = PropertyDetailSerializer(deal.property_detail,context={'to_currency':to_currency})
        return serializer.data
    
    def get_location(self, deal):
        print('deal.location',deal.location)
        location = Location.objects.filter(id = deal.location.id).first()
        serializer = LocationSerializer(location)
        return serializer.data


class PropertyDealSerializer(serializers.ModelSerializer):

    location = serializers.SerializerMethodField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    property_details = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    is_redeemed = serializers.SerializerMethodField()
    total_redeemed = serializers.SerializerMethodField()
    creator_details = serializers.SerializerMethodField()
    is_flagged = serializers.SerializerMethodField()
    actual_price = serializers.SerializerMethodField()
    free_member_discount_value = serializers.SerializerMethodField()
    club_member_discount_value = serializers.SerializerMethodField()

    class Meta:

        model = Deal
        fields = (
            'id','title','description','expiry_date','user',
            'property_details','location','images','added_to_wishlist',
            'free_member_discount_type', 'free_member_discount_value', 'free_member_code', 
            'club_member_discount_type','club_member_discount_value', 'club_member_code',
            'is_redeemed','total_redeemed','creator_details','is_flagged','actual_price',
            'deal_type','business_sub_category','business_sub_sub_category','property_class',
            'weekly', 'online_supported','redemption_link'
        )

    
    def get_property_details(self, deal):
        
        try:
            property_detail = deal.property_detail
        except:
            return ""
        
        if property_detail:
            to_currency = self.context.get('to_currency')
            serializer = PropertyDetailSerializer(property_detail,context={'to_currency':to_currency})
            return serializer.data

    
    def get_location(self, deal):

        try:
            location = Location.objects.get(id = deal.location.id)
        except:
            return ""
        
        serializer = LocationSerializer(location)
        return serializer.data
        
    def get_images(self, deal):
        serializer = DealImageSerializer(deal.deal_images, many=True)
        return serializer.data
    
    def get_added_to_wishlist(self, deal):
        
        user = self.context.get('user')
        if user and not user.is_anonymous:
                fav_deals = [deal.id for deal in user.favourite_deal.all()]
                if deal.id in fav_deals:
                    return True
        
        return False
    
    def get_total_redeemed(self, deal):
        return deal.redeemed_deals.all().count()
    
    def get_is_redeemed(self, deal):
        
        user = self.context.get('user')

        if user and not user.is_anonymous:
            try:
                redeemed = DealRedeem.objects.filter(user=user, deal=deal).last()
            except:
                return False
            
            if redeemed:
                return True

        return False
    
    def get_creator_details(self,job):

        serializer = CreatorProfileSerializer(job.user, context={'user': self.context.get('user')})
        return serializer.data
    
    def get_is_flagged(self, deal):
        
        logged_user = self.context.get('user')
        if logged_user and not logged_user.is_anonymous:
            try:
                flagged = Flagged.objects.get(deal=deal, flagged_by=logged_user)
            except:
                return False
            
            if flagged:
                return True
        
        return False

    def get_actual_price(self,deal):
        to_currency = self.context.get('to_currency')
        return __(deal.actual_price,deal.user.currency.iso_code, to_currency)
    
    def get_free_member_discount_value(self,deal):
        to_currency = self.context.get('to_currency')
        if deal.free_member_discount_type == 'fixed':
            return __(deal.free_member_discount_value,deal.user.currency.iso_code, to_currency)
        else:
            return deal.free_member_discount_value
        
    def get_club_member_discount_value(self,deal):
        to_currency = self.context.get('to_currency')
        if deal.club_member_discount_type == 'fixed':
            return __(deal.club_member_discount_value,deal.user.currency.iso_code, to_currency)
        else:
            return deal.club_member_discount_value
    

class AddDealReviewSerializer(serializers.ModelSerializer):

    reviewed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Review
        fields = ('deal','rating','comment','reviewed_by')


class DealReviewSerializer(serializers.ModelSerializer):

    reviewed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Review
        fields = '__all__'


class DealReviewDetailSerializer(serializers.ModelSerializer):

    reviewed_by = serializers.SerializerMethodField()
    reviewed_by_profile_pic = serializers.SerializerMethodField()
    marked_useful_by_logged_user = serializers.SerializerMethodField()
    flagged_by_logged_user = serializers.SerializerMethodField()
    review_useful_count = serializers.SerializerMethodField()

    class Meta:

        model = Review
        fields = '__all__'

    def get_reviewed_by(self, review):
        if review.reviewed_by.name:
            return review.reviewed_by.name
        else:
            return review.reviewed_by.get_full_name()
        
    
    def get_reviewed_by_profile_pic(self, review):
        if review.reviewed_by.image:
            return review.reviewed_by.image.url
        else:
            return "/static/default_profile_pic.jpeg"
        
    
    def get_marked_useful_by_logged_user(self, review):
        
        logged_user = self.context.get('user')
        try:
            marked_useful = ReviewMark.objects.get(user = logged_user, review = review)
        except:
            return ""
        
        if marked_useful:
            if marked_useful.mark_type:
                return 'yes'
            else:
                return 'no'
            
    def get_flagged_by_logged_user(self, review):
        
        logged_user = self.context.get('user')
        try:
            flagged = ReviewFlag.objects.get(user = logged_user, review = review)
        except:
            return False
        
        if flagged:
            return True
        else:
            return False
        
    def get_review_useful_count(self, review):
        
        all_marked_useful = ReviewMark.objects.filter(review = review, mark_type = True)
        return all_marked_useful.count()


class ReviewMarkSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = ReviewMark
        fields = '__all__'


class ReviewFlagSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = ReviewFlag
        fields = '__all__'


class AddDealFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = ('reason','deal','flagged_by')


class DealFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = '__all__'


class DealRedeemSerializer(serializers.ModelSerializer):

    deal = serializers.SerializerMethodField()
    user = serializers.SerializerMethodField()

    class Meta:

        model = DealRedeem
        fields = '__all__'

    def get_deal(self, redeem):
        return redeem.deal.title
    
    def get_user(self, redeem):
        serializer = UserProfileSerializer(redeem.user)
        return serializer.data