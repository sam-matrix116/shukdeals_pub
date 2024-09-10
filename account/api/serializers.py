from rest_framework import serializers,exceptions
from account.models import *
import uuid
from django.contrib.auth import authenticate
from django.utils.translation import gettext as _
from django.db.models import Sum
from account.utils import get_map_for_currency, convert_currency as __
from deals.models import DealRedeem
from rest_framework_simplejwt.serializers import TokenRefreshSerializer
from rest_framework_simplejwt.state import token_backend
from django.db.models import Q
from account.utils import *


class CustomTokenRefreshSerializer(TokenRefreshSerializer):
    def validate(self, attrs):
        data = super(CustomTokenRefreshSerializer, self).validate(attrs)
        decoded_payload = token_backend.decode(data['access'], verify=True)
        user_uid=decoded_payload['user_id']
        # add filter query
        data.update({'status': True})
        return data


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('phone', 'email','user_type','password','name','administrator_name','firstname','lastname','country','language','currency','ngo')

    def validate(self, attrs):

        user_type = attrs.get('user_type', '')
        phone = attrs.get('phone', '')
        name = attrs.get('name', '')
        firstname = attrs.get('firstname', '')
        lastname = attrs.get('lastname', '')
        administrator_name = attrs.get('administrator_name', '')
        country = attrs.get('country', '')
        language = attrs.get('language', '')
        currency = attrs.get('currency', '')
        ngo = attrs.get('ngo', '')
        
        if (len(phone) < 10 or len(phone) > 17):
            raise serializers.ValidationError(
                { "phone": [
                    _('Please enter proper phone number.')
                    ]
                }
            )
        # attrs['phone'] = int(phone)

        if user_type != 'ngo' and not ngo:
            
            raise serializers.ValidationError(
                { "ngo": [
                    _('NGO is required.')
                    ]
                }
            )
        
        if ngo:
            if ngo.user_type != 'ngo':
                raise serializers.ValidationError(
                    { "ngo": [
                        _('Please send valid ngo.')
                        ]
                    }
                )


        if user_type == 'ngo' or user_type == 'news_agency':
            if not name:
                raise serializers.ValidationError(
                    { "name": [
                        _('Name is required.')
                        ]
                    }
                )
            if not administrator_name:
                raise serializers.ValidationError(
                    { "administrator_name": [
                        _('Administrator name is required.')
                        ]
                    }
                )
            
        if user_type == 'business':
            if not name:
                raise serializers.ValidationError(
                    { "name": [
                        _('Business name is required.')
                        ]
                    }
                )
            if not administrator_name:
                raise serializers.ValidationError(
                    { "administrator_name": [
                        _('Administrator name is required.')
                        ]
                    }
                )
            
        if user_type == 'member':
            if not firstname:
                raise serializers.ValidationError(
                    { "firstname": [
                        _('First Name is required.')
                        ]
                    }
                )
            if not lastname:
                raise serializers.ValidationError(
                    { "lastname": [
                        _('Last Name is required.')
                        ]
                    }
                )
            
        if not country:
            raise serializers.ValidationError(
                { "country": [
                    _('Country is required.')
                    ]
                }
            )
            
        if not language:
            raise serializers.ValidationError(
                { "language": [
                    _('Language is required.')
                    ]
                }
            )
        
        if not currency:
            raise serializers.ValidationError(
                { "currency": [
                    _('Currency is required.')
                    ]
                }
            )

        return attrs
    
    def save(self):

        account = MyUser(
            email=self.validated_data['email'],
        )
        account.set_password(str(uuid.uuid4()))

        user_type = self.validated_data['user_type']
        
        account.is_staff = False
        account.is_verified = False
        account.user_type = self.validated_data['user_type']
        account.is_superuser = False
        account.is_admin = False
        account.phone = self.validated_data['phone']
        
        if user_type == 'ngo' or user_type == 'news_agency' or user_type == 'business':
            account.name = self.validated_data['name']
            account.administrator_name = self.validated_data['administrator_name']
        
        if user_type == 'member':
            account.firstname = self.validated_data['firstname']
            account.lastname = self.validated_data['lastname']

        if user_type != 'ngo':
            account.ngo = self.validated_data['ngo']

        account.country = self.validated_data['country']
        account.language = self.validated_data['language']
        account.currency = self.validated_data['currency']

        account.save()
        return account


class LoginSerializer(serializers.Serializer):
    
    email_or_phone = serializers.CharField()
    password = serializers.CharField()

    def validate(self, data):
        
        email_or_phone = data.get('email_or_phone', '')
        password = data.get('password', '')

        if email_or_phone and password:
            user = authenticate(email=email_or_phone, password=password)
            
            # check with phone
            if not user:
                email_or_phone_with_plus = "+"+email_or_phone
                try:
                    user = MyUser.objects.get(Q(phone=email_or_phone)|Q(phone=email_or_phone_with_plus))
                except:
                    message = _('Wrong Credentials!')
                    raise exceptions.ValidationError(message)
                user = authenticate(email=user.email, password=password)
            
            if user:
                if user.is_verified:
                    data['user'] = user
                else:
                    message = _('Account is not verified, Verify it first!')
                    raise exceptions.ValidationError(message)
            else:
                message = _('Wrong Credentials!')
                raise exceptions.ValidationError(message)
        else:
            message = _('Both fields are required!')
            raise exceptions.ValidationError(message)
        return data


class LoginUserDetailSerializer(serializers.ModelSerializer):

    plan_details = serializers.SerializerMethodField()
    ngo = serializers.SerializerMethodField()
    location_set = serializers.SerializerMethodField()
    currency_icon = serializers.SerializerMethodField()
    currency = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id','email','phone','firstname','lastname','name','user_type','image','cover_pic','is_verified','plan_details','ngo','currency','currency_icon','language','location_set')

    def get_plan_details(self, user):

        try:
            plan = Plan.objects.get(id=user.plan_id)
        except:
            return ""
        
        serializer = PlanSerializer(plan)
        return serializer.data
    
    def get_ngo(self, user):

        try:
            ngo = MyUser.objects.get(id = user.ngo.id)
        except:
            return ""
        
        serializer = NgosSerializer(ngo)
        return serializer.data
    
    def get_location_set(self, user):

        try:
            UserLocation.objects.get(user=user,is_primary=True)
        except:
            return False
        
        return True

    def get_currency_icon(self,user):
        flag = get_map_for_currency(user.currency.iso_code)
        return flag
    
    def get_currency(self,user):
        return user.currency.iso_code


class ChangePasswordSerializer(serializers.Serializer):
    current_password = serializers.CharField(required=True)
    new_password = serializers.CharField(required=True)
    confirm_password = serializers.CharField(required=True)

    class Meta:
        fields = ['current_password', 'new_password', 'confirm_password']

    def validate(self, attrs):
        current_password = attrs.get('current_password', '')
        new_password = attrs.get('new_password', '')
        confirm_password = attrs.get('confirm_password', '')

        if not current_password:
            raise serializers.ValidationError({"current_password": [_("current_password is required")]})

        if not new_password:
            raise serializers.ValidationError({"new_password": [_("new_password is required")]})

        if not confirm_password:
            raise serializers.ValidationError({"confirm_new_password": [_("confirm_new_password is required")]})

        if new_password!=confirm_password:
            raise serializers.ValidationError({"error": [_("Passwords do not match!")]})

        if len(new_password) < 8:
            raise serializers.ValidationError({"error": [_("Password must be more then 8 digits long")]})
        
        return attrs
    

class FamilyMemberCreateSerializer(serializers.ModelSerializer):

    parent = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = MyUser
        fields = ('email','phone','parent','firstname','lastname','relation','image')


class FamilyMemberSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('email','phone','firstname','lastname','relation','image')


class NgosSerializer(serializers.ModelSerializer):

    referal_token = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id','name','image','referal_token')

    def get_referal_token(self,user):
        try:
            ref = NgoReferalToken.objects.get(user=user)
        except:
            return ""
        return ref.referal_token


class UserProfileSerializer(serializers.ModelSerializer):

    average_review = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    is_flagged = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    cover_pic = serializers.SerializerMethodField()
    is_hamza = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id','firstname','lastname','name','image','cover_pic','average_review','total_reviews','created_at','website_url','facebook_url','twitter_url','instagram_url','youtube_url','added_to_wishlist','business_contact','business_email','email','phone','user_type','is_flagged','business_category','user_type_category','is_hamza','reservation_walkin','service_provider_type')

    def get_average_review(self, user):
        total_reviews = user.reviews.count()
        all_reviews = Review.objects.filter(user = user).aggregate(Sum("rating"))
        average_review = 0
        if total_reviews > 0:
            average_review = all_reviews["rating__sum"]/total_reviews
        return average_review

    def get_total_reviews(self, user):
        return user.reviews.count()
    
    def get_added_to_wishlist(self, user):
        
        logged_user = self.context.get('user')
        if logged_user and not logged_user.is_anonymous:
            fav_users = [usr.id for usr in logged_user.favourite_user.all()]
            if user.id in fav_users:
                return True
        
        return False
    
    def get_is_flagged(self, user):
        
        logged_user = self.context.get('user')
        if logged_user and not logged_user.is_anonymous:
            try:
                Flagged.objects.get(user=user, flagged_by=logged_user)
            except:
                return False
            
            return True
        
        return False
    
    def get_image(self, user):

        if user.image:
            return user.image.url
        else:
            return "/static/default_profile_pic.jpeg"
        
    def get_cover_pic(self, user):

        if user.cover_pic:
            return user.cover_pic.url
        else:
            return "/media/default_images/default_cover_pic.png"
        
    def get_is_hamza(self, user):

        if user.plan and user.plan.amount > 0:
            return True
        
        return False
    

class CategorySerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    class Meta:
        model = BusinessCategory
        fields = ('id','name','keyword','parent','display_type')

    def get_name(self, category):
        
        try:
            lang_code = self.context.get("request").LANGUAGE_CODE
        except:
            lang_code = 'en'
        
        if lang_code == 'en':
            return category.name
        elif lang_code == 'es':
            return category.name_es
        elif lang_code == 'fr':
            return category.name_fr
        elif lang_code == 'he':
            return category.name_he
        elif lang_code == 'ru':
            return category.name_ru
        elif lang_code == 'ar':
            return category.name_ar
        elif lang_code == 'pt':
            return category.name_pt
        elif lang_code == 'de':
            return category.name_de
        
        return category.name


class UpdateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('firstname','lastname','name','phone','about','business_category','website_url','facebook_url','twitter_url','instagram_url','youtube_url','image','cover_pic','user_type_category','service_provider_type','reservation_walkin')




class ProfileSerializer(serializers.ModelSerializer):

    location = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField()
    business_category_details = serializers.SerializerMethodField()
    family_member = serializers.SerializerMethodField()
    ngo_videos = serializers.SerializerMethodField()
    ngo_referal_token = serializers.SerializerMethodField()
    delivery_partners = serializers.SerializerMethodField()
    average_review = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    business_associated = serializers.SerializerMethodField()
    user_associated = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()
    user_type = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    associated_ngo = serializers.SerializerMethodField()
    currency_icon = serializers.SerializerMethodField()
    currency_iso = serializers.SerializerMethodField()
    currency_sign = serializers.SerializerMethodField()
    is_flagged = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    cover_pic = serializers.SerializerMethodField()
    redeem_points = serializers.SerializerMethodField()
    user_type_category_details = serializers.SerializerMethodField()


    class Meta:
        model = MyUser
        fields = ('id','email','name','firstname','lastname','phone','about','business_category','website_url','facebook_url','twitter_url','instagram_url','youtube_url','image','cover_pic','location','menu','delivery_partners','business_category_details','family_member','ngo_videos','ngo_referal_token','average_review','total_reviews','business_associated','user_associated','plan','user_type','added_to_wishlist','associated_ngo','language','currency_icon','currency','extra_deal','extra_classified','extra_location','currency_iso','currency_sign','is_flagged','redeem_points','parent','user_type_category_details','reservation_walkin','service_provider_type','is_store')


    def get_user_type_category_details(self, user):
        serializer = UserTypeCategorySerializer(user.user_type_category)
        return serializer.data


    def get_location(self, user):
        print("user",user)
        
        try:
            user_location = UserLocation.objects.get(user = user, is_primary = True)
        except:
            return ""
        
        print("user_location",user_location)

        if user_location:
            
            try:
                location = Location.objects.get(id = user_location.location_id)
            except:
                return ""
            
            serializer = LocationSerializer(location, context={"user": user})
            return serializer.data
        
        return ""
    
    def get_menu(self, user):

        menu = RestaurantMenu.objects.filter(user = user).first()
        serializer = MenuSerializer(menu)
        return serializer.data
    
    def get_business_category_details(self, user):
        
        try:
            request = self.context.get("request")
        except:
            request = None

        serializer = CategorySerializer(user.business_category, context={"request": request})
        return serializer.data
    
    
    def get_family_member(self, user):

        # print("family_member_user", user.family_member_user)

        try:
            family_member = MyUser.objects.get(parent=user)
        except:
            return ""
        
        serializer = FamilyMemberSerializer(family_member)
        return serializer.data
    
    def get_ngo_videos(self, user):
        logged_user = self.context.get('user')
        serializers = NgoVideoSerializer(user.ngo_videos.all(), many=True, context={"user": logged_user})
        return serializers.data
    
    def get_ngo_referal_token(self, user):

        if user.user_type == 'ngo':
            try:
                user.ngo_referal
            except:
                return ""
            return user.ngo_referal.referal_token
        else:
            return ""
        
    def get_delivery_partners(self, user):

        serializers = DeliveryPartnerSerializer(user.delivery_partner.all(), many=True)
        return serializers.data
    
    def get_average_review(self, user):
        total_reviews = user.reviews.count()
        all_reviews = Review.objects.filter(user = user).aggregate(Sum("rating"))
        average_review = 0
        if total_reviews > 0:
            average_review = all_reviews["rating__sum"]/total_reviews
        return average_review

    def get_total_reviews(self, user):
        return user.reviews.count()
    
    
    def get_business_associated(self,user):
        if user.user_type != 'ngo':
            return 0
        
        associated_business = active_businesses().filter(ngo=user, user_type='business').count()
        return associated_business

    def get_user_associated(self,user):
        if user.user_type != 'ngo':
            return 0
        
        associated_business = active_businesses().filter(ngo=user, user_type='member').count()
        return associated_business
    
    def get_plan(self, user):
        if user.plan:
            serializer = PlanSerializer(user.plan)
            return serializer.data
        else:
            return ""
        
    def get_user_type(self, user):
        return user.get_user_type_display()
    
    def get_added_to_wishlist(self, user):
        
        logged_user = self.context.get('user')
        if logged_user and not logged_user.is_anonymous:
            fav_users = [usr.id for usr in logged_user.favourite_user.all()]
            if user.id in fav_users:
                return True
        
        return False
    
    def get_associated_ngo(self, user):
        if user.ngo:
            if user.ngo.name:
                data = {
                    "id": user.ngo.id,
                    "name": user.ngo.name,
                    "image": user.ngo.image.url if user.ngo.image else "/static/default_profile_pic.jpeg"
                }
                return data
            else:
                return user.ngo.email
        else:
            return ""
        
    def get_currency_icon(self,user):
        svg = user.currency.sign_svg
        return svg
    
    def get_currency_sign(self,user):
        return user.currency.sign
    
    def get_currency_iso(self,user):
        return user.currency.iso_code
    
    def get_is_flagged(self, user):
        
        logged_user = self.context.get('user')
        if not logged_user.is_anonymous:
            try:
                Flagged.objects.get(user=user, flagged_by=logged_user)
            except:
                return False
        
        return True
    
    def get_image(self, user):

        if user.image:
            return user.image.url
        else:
            return "/static/default_profile_pic.jpeg"
        
    def get_cover_pic(self, user):

        if user.cover_pic:
            return user.cover_pic.url
        else:
            return "/media/default_images/default_cover_pic.png"
    
    def get_redeem_points(self, user):
        user_deal_redeems = DealRedeem.objects.filter(deal__user = user)
        return user_deal_redeems.count()
    
            


class CountrySerializer(serializers.ModelSerializer):

    flag = serializers.SerializerMethodField()

    class Meta:
        model = Country
        fields = ('id','name','flag')

    def get_flag(self, country):

        return '/static/flags/'+country.iso.lower()+".png"


class CurrencySerializer(serializers.ModelSerializer):

    flag = serializers.SerializerMethodField()

    class Meta:
        model = Currency
        fields = '__all__'
        extras = ('flag')

    def get_flag(self, currency):

        return get_map_for_currency(currency.iso_code)


class PlanSerializer(serializers.ModelSerializer):

    features = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()

    class Meta:
        model = Plan
        fields = ('id','user_type','name','amount', 'features')

    def get_features(self, plan):
        features = PlanFeature.objects.filter(plan = plan)
        serializer = PlanFeatureSerializer(features, many = True)
        return serializer.data
    
    def get_amount(self,plan):
        to_currency = self.context.get('to_currency')
        return __(plan.amount,'usd', to_currency)


class PlanFeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = PlanFeature
        fields = '__all__'


class LocationSerializer(serializers.ModelSerializer):

    is_primary = serializers.SerializerMethodField()

    class Meta:
        model = Location
        fields = '__all__'

    def get_is_primary(self, location):
        logged_user = self.context.get('user')
        print('logged_user',logged_user)
        print('location',location)
        
        if logged_user and not logged_user.is_anonymous:
            try:
                UserLocation.objects.get(user=logged_user, location=location, is_primary=True)
            except:
                return False
        
            return True



class StoreLocationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        fields = '__all__'

    def validate(self, attrs):

        store_manager_email = attrs.get('store_manager_email', '')
        store_manager_phone = attrs.get('store_manager_phone', '')

        if not store_manager_email:
            raise serializers.ValidationError(
                { "store_manager_email": [
                    _('This field is required')
                    ]
                }
            ) 
        
        if not store_manager_phone:
            raise serializers.ValidationError(
                { "store_manager_phone": [
                    _('This field is required')
                    ]
                }
            ) 

        try:
            email_already_exist = MyUser.objects.get(email = store_manager_email)
        except:
            email_already_exist = None

        try:
            phone_already_exist = MyUser.objects.get(phone = store_manager_phone)
        except:
            phone_already_exist = None   

        if email_already_exist:
            raise serializers.ValidationError(
                { "email": [
                    _('This email {} is already registered with our system. Please enter a new email.'.format(store_manager_email))
                    ]
                }
            ) 
        
        if phone_already_exist:
            raise serializers.ValidationError(
                { "email": [
                    _('This phone {} is already registered with our system. Please enter a new phone.'.format(store_manager_phone))
                    ]
                }
            ) 

        return super().validate(attrs)


class LocationUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Location
        exclude = ('created_at',)


class MenuSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = RestaurantMenu
        fields = '__all__'


class MenuUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = RestaurantMenu
        fields = ('menu',)


class DeliveryPartnerSerializer(serializers.ModelSerializer):

    class Meta:
        model = DeliveryPartner
        fields = '__all__'


class NgoVideoSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    total_likes = serializers.SerializerMethodField()
    creator_pic = serializers.SerializerMethodField()
    ngo = serializers.SerializerMethodField()
    is_liked = serializers.SerializerMethodField()
    

    class Meta:
        model = NgoVideo
        fields = '__all__'
        extras = ('total_likes','creator_pic','ngo','is_liked')

    def get_total_likes(self, video):

        return video.favourite_ngo_videos.all().count()
    
    def get_creator_pic(self, video):
        if video.user.image:
            return video.user.image.url
        else:
            return "/static/default_profile_pic.jpeg"
    
    def get_ngo(self, video):
        return video.user_id
    
    def get_is_liked(self, user):
        
        logged_user = self.context.get('user')
        if logged_user and not logged_user.is_anonymous:
            fav_ngo_videos = [usr.id for usr in logged_user.favourite_ngo_video.all()]
            if user.id in fav_ngo_videos:
                return True
        
        return False


class AddUserReviewSerializer(serializers.ModelSerializer):

    reviewed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Review
        fields = ('rating','comment','user','reviewed_by')


class UserReviewSerializer(serializers.ModelSerializer):

    reviewed_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Review
        fields = '__all__'


class UserReviewDetailSerializer(serializers.ModelSerializer):

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

class CreatorProfileSerializer(serializers.ModelSerializer):

    average_review = serializers.SerializerMethodField()
    total_reviews = serializers.SerializerMethodField()
    business_category_name = serializers.SerializerMethodField()
    delivery_partners = serializers.SerializerMethodField()
    menu = serializers.SerializerMethodField()
    associated_ngo = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    plan = serializers.SerializerMethodField()
    image = serializers.SerializerMethodField()
    cover_pic = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id','cover_pic','image','user_type','firstname','lastname','name','business_category_name','average_review','total_reviews','about','business_contact','website_url','facebook_url','twitter_url','instagram_url','youtube_url','delivery_partners','menu','email','phone','associated_ngo','location','added_to_wishlist','plan')

    def get_average_review(self, user):
        total_reviews = user.reviews.count()
        all_reviews = Review.objects.filter(user = user).aggregate(Sum("rating"))
        average_review = 0
        if total_reviews > 0:
            average_review = all_reviews["rating__sum"]/total_reviews
        return average_review

    def get_total_reviews(self, user):
        return user.reviews.count()
    
    def get_added_to_wishlist(self, user):
        
        logged_user = self.context.get('user')
        fav_users = [usr.id for usr in logged_user.favourite_user.all()]
        if user.id in fav_users:
            return True
        
        return False
    
    def get_business_category_name(self, user):

        if user.business_category:
            return user.business_category.name
        
    def get_delivery_partners(self, user):

        serializers = DeliveryPartnerSerializer(user.delivery_partner.all(), many=True)
        return serializers.data
    
    def get_menu(self, user):

        menu = RestaurantMenu.objects.filter(user = user).first()
        serializer = MenuSerializer(menu)
        return serializer.data
    
    def get_associated_ngo(self, user):
        if user.ngo:
            if user.ngo.name:
                return user.ngo.name
            else:
                return user.ngo.email
        else:
            return ""
    
    def get_location(self, user):
        try:
            user_location = UserLocation.objects.get(user = user, is_primary = True)
        except:
            return ""
        serializer = LocationSerializer(user_location.location)
        return serializer.data
    
    def get_added_to_wishlist(self, user):
        
        logged_user = self.context.get('user')

        if logged_user and logged_user.id:
            fav_users = [usr.id for usr in logged_user.favourite_users.all()]
            if user.id in fav_users:
                return True
        
        return False
    
    def get_plan(self, user):
        if user.plan:
            if user.plan.name:
                return user.plan.name
            else:
                return user.plan.id
        else:
            return ""
        
    def get_image(self, user):

        if user.image:
            return user.image.url
        else:
            return "/static/default_profile_pic.jpeg"
        
    def get_cover_pic(self, user):

        if user.cover_pic:
            return user.cover_pic.url
        else:
            return "/media/default_images/default_cover_pic.png"
    

class MinimalUserDetailSerializer(serializers.ModelSerializer):

    image = serializers.SerializerMethodField()
    cover_pic = serializers.SerializerMethodField()
    full_name = serializers.SerializerMethodField()

    class Meta:
        model = MyUser
        fields = ('id','cover_pic','image','full_name')

    def get_full_name(self, user):
        return user.get_full_name()
    
    def get_image(self, user):

        if user.image:
            return user.image.url
        else:
            return "/static/default_profile_pic.jpeg"
        
    def get_cover_pic(self, user):

        if user.cover_pic:
            return user.cover_pic.url
        else:
            return "/media/default_images/default_cover_pic.png"

class NewsAgencySerializer(serializers.ModelSerializer):

    class Meta:
        model = MyUser
        fields = ('id','name','image','email')


class AddUserFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = ('reason','user','flagged_by')


class UserFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = '__all__'


class TranzilaTokenSerializer(serializers.ModelSerializer):

    class Meta:

        model = TranzilaToken
        fields = '__all__'


class StripeDetailSerializer(serializers.ModelSerializer):

    class Meta:

        model = StripeDetailNew
        fields = ('payment_method','card_mask','expire_month','expire_year')


class StripePaymentMethodSerializer(serializers.ModelSerializer):

    class Meta:

        model = StripePaymentMethod
        fields = '__all__'


class UserTypeCategorySerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    class Meta:

        model = UserTypeCategory
        fields = ('id','name','user_type')

    def get_name(self, category):
        
        try:
            lang_code = self.context.get("request").LANGUAGE_CODE
        except:
            lang_code = 'en'
        
        if lang_code == 'en':
            return category.name
        elif lang_code == 'es':
            return category.name_es
        elif lang_code == 'fr':
            return category.name_fr
        elif lang_code == 'he':
            return category.name_he
        elif lang_code == 'ru':
            return category.name_ru
        elif lang_code == 'ar':
            return category.name_ar
        elif lang_code == 'pt':
            return category.name_pt
        elif lang_code == 'de':
            return category.name_de
        
        return category.name


class PaymentDetailSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    currency_icon = serializers.SerializerMethodField()
    amount = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:

        model = PaymentDetail
        fields = ('created_at','amount','currency_icon', 'description','status','id')

    def get_description(self, payment_detail):

        item_type = payment_detail.item_type

        description = item_type

        if item_type == 'plan':
            description = _('Monthly Subscription')
        elif item_type == 'deal':
            description = _('Listing')
        elif item_type == 'weekly_deal':
            description = _('Weekly Deal')
        elif item_type == 'classified':
            description = _('Classified')
        elif item_type == 'new_payment_method':
            description = _('New Payment Method')
        elif item_type == 'location':
            description = _('Location')
        
        return _(description)
    
    def get_amount(self,payment_detail):
        to_currency = self.context.get('to_currency')
        amount = round(payment_detail.amount,2)
        return __(amount,'usd', to_currency)
    
    def get_status(self,payment_detail):
        return _(payment_detail.get_status_display())
    
    def get_currency_icon(self, payment_detail):

        try:
            currency = Currency.objects.get(iso_code = payment_detail.currency)
        except:
            return ""

        return currency.sign
    

class NGOPayoutSerializer(serializers.ModelSerializer):

    description = serializers.SerializerMethodField()
    currency_icon = serializers.SerializerMethodField()
    status = serializers.SerializerMethodField()

    class Meta:

        model = NGOPayout
        fields = ('created_at','amount','currency_icon','description','status','id')

    def get_description(self, payout):

        description = "Recieved from "

        if payout.user.user_type == 'business':
            description += 'business '
        if payout.user.user_type == 'member':
            description += 'shop '

        if payout.user.get_full_name:
            description += payout.user.get_full_name()
        else:
            description += payout.user.email

        return description
    
    def get_currency_icon(self,payout):

        currency = Currency.objects.get(iso_code = 'usd')
        return currency.sign
    
    def get_status(self, payout):

        if payout.payout:
            return "Paid"
        else:
            return "Not Paid"
        