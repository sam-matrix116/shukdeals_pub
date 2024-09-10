from rest_framework import serializers,exceptions
from classifieds.models import *
from account.api.serializers import LocationSerializer, CreatorProfileSerializer
import datetime
from django.utils.translation import gettext as _
from account.utils import convert_currency as __


class CreateClassifiedSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    
    class Meta:
        model = Classified
        exclude = ('location',)

    def validate(self,attrs):

        expiry_date = attrs.get('expiry_date', '')
        today = datetime.datetime.now().date()
        expiry_date = datetime.datetime.strptime(str(expiry_date), "%Y-%m-%d").date()

        if expiry_date <= today:
            raise serializers.ValidationError({
                "expiry_date": _("Expiry date should be greater than today")
            })
        
        return attrs


class ClassifiedSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    location_details = serializers.SerializerMethodField()
    images = serializers.SerializerMethodField()
    added_to_wishlist = serializers.SerializerMethodField()
    price = serializers.SerializerMethodField()
    creator_details = serializers.SerializerMethodField()
    is_flagged = serializers.SerializerMethodField()
    
    class Meta:
        model = Classified
        exclude = ('location',)
        extra_field = ('location_details','added_to_wishlist','pinned','creator_details','is_flagged')

    def get_location_details(self, classified):
        location = Location.objects.get(id = classified.location_id)
        serializer = LocationSerializer(location)
        return serializer.data
    
    def get_images(self, classified):
        images = ClassifiedImage.objects.filter(classified = classified)
        serializer = ClassifiedImageSerializer(images, many=True)
        return serializer.data
    
    def get_added_to_wishlist(self, classified):
        
        user = self.context.get('user')
        if user and not user.is_anonymous:
            fav_classifieds = [classified.id for classified in user.favourite_classified.all()]
            if classified.id in fav_classifieds:
                return True
        
        return False
    
    def get_price(self,classified):
        to_currency = self.context.get('to_currency')
        return __(classified.price, classified.user.currency.iso_code, to_currency)
    
    def get_creator_details(self,classified):

        serializer = CreatorProfileSerializer(classified.user, context={'user': self.context.get('user')})
        return serializer.data
    
    def get_is_flagged(self, classified):
        
        logged_user = self.context.get('user')
        if not logged_user.is_anonymous:
            try:
                flagged = Flagged.objects.get(classified=classified, flagged_by=logged_user)
            except:
                return False
            
            if flagged:
                return True
        
        return False
    

class ClassifiedImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClassifiedImage
        fields = '__all__'


class AddClassifiedFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = ('reason','classified','flagged_by')


class ClassifiedFlagSerializer(serializers.ModelSerializer):

    flagged_by = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:

        model = Flagged
        fields = '__all__'


class ClassifiedCategorySerializer(serializers.ModelSerializer):

    name = serializers.SerializerMethodField()

    class Meta:

        model = ClassifiedCategory
        fields = '__all__'

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