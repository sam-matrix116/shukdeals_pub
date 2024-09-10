from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from shuktv.utils.customPermissionClass import IsNormalUser, IsRealEstateBusinessCategory, IsPlanActivated
from deals.models import *
from deals.api.serializers import *
from account.api.serializers import LocationSerializer, UserProfileSerializer
from rest_framework.response import Response
from django.utils.translation import gettext as _
from django.db.models import Q, Count
from shuktv.utils.customPaginations import paginated_data
import datetime
from django.conf import settings
from django.template.loader import get_template
from account.utils import send_email, check_plan_exceeded, convert_currency as __, active_users, active_businesses, get_single_product_cost
from account.models import PaymentDetail, UserLocation
from classifieds.api.serializers import ClassifiedSerializer
from django.db.models import Sum
from classifieds.utils import active_classifieds
from deals.utils import *
import logging
logger = logging.getLogger('demo_log')
logger = logging.getLogger('django')


class CreateBusinessDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        # charge every weekly deal
        logger.info("user id: {}".format(request.user.id))
        logger.info("request.user.extra_weekly_deal: {}".format(request.user.extra_weekly_deal))
        if request.user.user_type == 'business':

            if not request.user.plan:
                return Response({
                    "status": False,
                    "message":_("You have not activated any plan.Please activate plan to add deal."),
                    "go_to": "plan_activation"
                })

            if "weekly" in request.data and request.data["weekly"]:
                if not request.user.extra_weekly_deal:

                    # create a row in table payment details to store the payment details
                    main_amount_in_usd = get_single_product_cost(
                        request.user, 'deal', 'weekly', 'main_amount')
                    single_deal_cost_with_tax = main_amount_in_usd + \
                        int(settings.SHUKTV_TAX_COST)

                    currency = 'usd'
                    amount = single_deal_cost_with_tax
                    if request.user.currency.iso_code != 'usd':
                        currency = request.user.currency.iso_code
                        amount = __(amount, 'usd', currency)

                    if main_amount_in_usd > 0:
                        
                        payment_detail = PaymentDetail.objects.create(
                            user=request.user,
                            item_type='weekly_deal',
                            main_amount_in_usd=main_amount_in_usd,
                            amount=amount,
                            currency=currency
                        )

                        return Response({
                            'status': True,
                            'go_to': 'payment',
                            'module': 'weekly deal',
                            'payment_detail': payment_detail.id
                        })
                    
                    else:
                        pass

            else:
                # check if the user's limit has not reached based on plan
                plan_exceeded = check_plan_exceeded(request.user, 'deal')
                if plan_exceeded and not request.user.extra_deal:

                    main_amount_in_usd = get_single_product_cost(
                        request.user, 'deal', 'listing', 'main_amount')
                    single_deal_cost_with_tax = main_amount_in_usd + \
                        int(settings.SHUKTV_TAX_COST)

                    # create a row in table payment details to store the payment details
                    currency = 'usd'
                    amount = single_deal_cost_with_tax
                    if request.user.currency.iso_code != 'usd':
                        currency = request.user.currency.iso_code
                        amount = __(amount, 'usd', currency)

                    if main_amount_in_usd > 0:
                        payment_detail = PaymentDetail.objects.create(
                            user=request.user,
                            item_type='deal',
                            main_amount_in_usd=main_amount_in_usd,
                            amount=amount,
                            currency=currency
                        )

                        return Response({
                            'status': True,
                            'go_to': 'payment',
                            'payment_detail': payment_detail.id
                        })
                    else:
                        pass

        if "images" not in request.data:
            return Response({
                'status': False,
                'field': 'images',
                'message': _("Image is required")
            })        

        # print("request.data", request.data)
        serializer = CreateBusinessDealSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        deal = serializer.save(active=True)

        # store location
        if "location" in request.data:
            location_serializer = LocationSerializer(
                data=request.data, context={"request": request})
            location_serializer.is_valid(raise_exception=True)
            loc = location_serializer.save()

            deal.location = loc
            deal.save()

        if "business_location" in request.data:
            try:
                business_location = Location.objects.get(
                    id=request.data["business_location"])
            except:
                business_location = None

            if business_location:
                deal.location = business_location
                deal.save()

        # save images
        images = request.FILES.getlist('images')
        for image in list(images):
            deal_img = DealImage(deal=deal, image=image)
            deal_img.save()

        # save expiry date for weekly deals
        if deal.weekly and request.user.extra_weekly_deal:
            today = datetime.date.today()
            week_ahead = today + datetime.timedelta(days=7)
            deal.expiry_date = week_ahead
            deal.save()

            request.user.extra_weekly_deal = False
            request.user.save()

            deal.paid = True
            deal.shuk_fee = get_single_product_cost(
                request.user, 'deal', 'weekly', 'shuk_fee')
            deal.save()

        if not deal.weekly and request.user.extra_deal:
            request.user.extra_deal = False
            request.user.save()

            shuk_fee = get_single_product_cost(
                request.user, 'deal', 'listing', 'shuk_fee')

            deal.paid = True
            deal.shuk_fee = shuk_fee
            deal.save()

        # if all stores is selected, we will create a child deal for main deal
        if not deal.weekly and "all_stores" in request.data:
            all_stores = UserLocation.objects.filter(user=request.user, is_primary = False)
            for store in all_stores:
                child_serializer = CreateBusinessDealSerializer(data=request.data, context={'request': request})
                child_serializer.is_valid(raise_exception=True)
                child_deal = child_serializer.save(active=True,location=store.location, parent=deal, all_stores=False)

                for image in list(images):
                    deal_img = DealImage(deal=child_deal, image=image)
                    deal_img.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Deal created successfully")
        })


class DealListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        deals = active_deals().filter(user=request.user, weekly=False, parent=None).order_by("-id")

        # filters start
        filter_by = request.GET.get('filter_by')
        if filter_by == "recent":
            deals = deals.order_by("-id")
        elif filter_by == "oldest":
            deals = deals.order_by("id")
        elif filter_by == 'payment_pending':
            deals = deals.filter(status='payment_pending')
        # filters end

        # search start
        search_key = request.GET.get('search_key')
        if search_key:
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))
        # search end

        weekly = request.GET.get('weekly')
        if weekly:
            deals = deals.filter(weekly=weekly)

        return paginated_data(deals, BusinessDealSerializer, request, 6)


class UserDealListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, user_id):

        today = datetime.datetime.now().date()

        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')

        try:
            user = MyUser.objects.get(pk=user_id)
        except:
            return Response({
                "status": False,
                "message": _("Invalid User")
            })

        deals = active_deals().filter(user=user, weekly=False).order_by("-id")

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, 8)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })
        

class NgoDealListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')

        deals = active_deals().filter(user__user_type='ngo', weekly=False).order_by("-id")

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, 8)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })
        

class NgoWeeklyDealListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')

        deals = active_deals().filter(user__user_type='ngo', weekly=True).order_by("-id")

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, 8)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class UpdateDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id, user=request.user, active=True)
        except:
            return Response({
                'status': False,
                'message': _("Invalid deal")
            })

        # location check
        if "location" in request.data:
            try:
                location = Location.objects.get(
                    id=request.data["location"], user=request.user)
            except:
                return Response({
                    'status': False,
                    'field': "location",
                    'message': _("Invalid Location")
                })

        serializer = CreateBusinessDealSerializer(
            deal, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save(active=True)

        # save images
        if "images" in request.data:
            images = request.FILES.getlist('images')
            for image in list(images):
                deal_img = DealImage(deal=deal, image=image)
                deal_img.save()

        child_deals = Deal.objects.filter(parent=deal)
        for child_deal in child_deals:
            serializer = CreateBusinessDealSerializer(child_deal, data=request.data, context={'request': request})
            serializer.is_valid(raise_exception=True)
            serializer.save(active=True)


        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Deal updated successfully")
        })


class DealDetailView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, deal_id):

        to_currency = self.request.GET.get('to_currency')

        try:
            deal = Deal.objects.get(id=deal_id, active=True)
        except:
            return Response({
                'status': False,
                'message': _('Invalid Deal')
            })

        # if we have a logged in user, increment its view-count
        if not request.user.is_anonymous and deal.user != request.user:
            try:
                DealClick.objects.get(deal=deal, user=request.user)
            except:
                DealClick.objects.create(
                    deal=deal,
                    user=request.user
                )

        if deal.user.business_category and deal.user.business_category.keyword == 'real_estate':
            serializer = PropertyDealSerializer(
                deal, context={'user': request.user, 'to_currency': to_currency})
        else:
            serializer = BusinessDealSerializer(
                deal, context={'user': request.user, 'to_currency': to_currency})

        return Response({
            'status': True,
            'data': serializer.data
        })


class DeleteDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id, user=request.user, active=True)
        except:
            return Response({
                'status': False,
                'message': _('Invalid Deal')
            })

        deal.is_deleted = True
        deal.save()

        child_deals = Deal.objects.filter(parent=deal)
        for child_deal in child_deals:
            child_deal.is_deleted = True
            child_deal.save()

        return Response({
            'status': True,
            'message': _("Deal deleted successfully")
        })


class PropertyTypesListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, requests):

        property_types = []

        for key, value in PROPERTY_TYPES:
            property_types.append(
                {
                    "key": key,
                    "value": _(value)
                }
            )

        return Response({
            'status': True,
            'data': property_types
        })


class CreatePropertyDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser,
                          IsRealEstateBusinessCategory)

    def post(self, request):

        # check if the user's limit has not reached based on plan
        plan_exceeded = check_plan_exceeded(request.user, 'deal')
        if plan_exceeded and not request.user.extra_deal:

            main_amount_in_usd = get_single_product_cost(
                request.user, 'deal', 'listing', 'main_amount')
            single_deal_cost_with_tax = main_amount_in_usd + \
                int(settings.SHUKTV_TAX_COST)

            # create a row in table payment details to store the payment details

            currency = 'usd'
            amount = single_deal_cost_with_tax
            if request.user.currency.iso_code != 'usd':
                currency = request.user.currency.iso_code
                amount = __(amount, 'usd', currency)

            if main_amount_in_usd > 0:
                payment_detail = PaymentDetail.objects.create(
                    user=request.user,
                    item_type='deal',
                    main_amount_in_usd=main_amount_in_usd,
                    amount=amount,
                    currency=currency
                )

                return Response({
                    'status': True,
                    'go_to': 'payment',
                    'payment_detail': payment_detail.id
                })

        if "images" not in request.data:
            return Response({
                'status': False,
                'field': 'images',
                'message': _("Image is required")
            })

        # sub category check start
        if "business_sub_category" not in request.data:
            return Response({
                'status': False,
                'field': 'business_sub_category',
                'message': _("Business Sub Category is required")
            })

        business_sub_category = int(request.data["business_sub_category"])

        real_estate_category = BusinessCategory.objects.get(
            keyword='real_estate')
        real_estate_sub_categories = [
            category.id for category in BusinessCategory.objects.filter(parent=real_estate_category)]

        if business_sub_category not in real_estate_sub_categories:
            return Response({
                'status': False,
                'field': 'business_sub_category',
                'message': _("For creating Real Estate deal, the business category can be rent,sale or vacational rental only")
            })

        try:
            sub_category = BusinessCategory.objects.get(
                id=business_sub_category)
        except:
            return Response({
                'status': False,
                'field': 'free_member_discount_type',
                'message': _("Free member discount type is required")
            })

        sub_category = sub_category.keyword

        if sub_category == 'vacation_rental':

            if 'free_member_discount_type' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_discount_type',
                    'message': _("Free member discount type is required")
                })
            if 'free_member_discount_value' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_discount_value',
                    'message': _("Free member discount value is required")
                })
            if 'free_member_code' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_code',
                    'message': _("Free member code is required")
                })
            if 'club_member_discount_type' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_discount_type',
                    'message': _("Club member discount type is required")
                })
            if 'club_member_discount_value' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_discount_value',
                    'message': _("Club member discount value is required")
                })
            if 'club_member_code' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_code',
                    'message': _("Club member code is required")
                })

        if sub_category == 'rent':
            if "offer_text" not in request.data:
                raise serializers.ValidationError({
                    "offer_text": _("Offer text is required")
                })

        if sub_category == 'vacation_rental':
            if "price_type" not in request.data:
                raise serializers.ValidationError({
                    "price_type": _("Price type is required")
                })

        # sub category check end

        # location details check
        location_serializer = LocationSerializer(
            data=request.data, context={"request": request})
        location_serializer.is_valid(raise_exception=True)

        # deal details check
        deal_serializer = CreatePropertyDealSerializer(
            data=request.data, context={'request': request, 'user': request.user})
        deal_serializer.is_valid(raise_exception=True)

        # property details check
        property_serializer = PropertySerializer(data=request.data)
        property_serializer.is_valid(raise_exception=True)

        location = location_serializer.save()
        deal = deal_serializer.save(active=True)
        deal.location = location
        deal.save()

        property_serializer.save(deal=deal)

        if request.user.extra_deal:
            request.user.extra_deal = False
            request.user.save()

            shuk_fee = get_single_product_cost(
                request.user, 'deal', 'listing', 'shuk_fee')

            deal.paid = True
            deal.shuk_fee = shuk_fee
            deal.save()

        # save images
        images = request.FILES.getlist('images')
        for image in list(images):
            deal_img = DealImage(deal=deal, image=image)
            deal_img.save()

        serializer = PropertyDealSerializer(
            deal, context={'request': request, 'user': request.user})
        
        # if all stores is selected, we will create a child deal for main deal
        if not deal.weekly and "all_stores" in request.data:
            all_stores = UserLocation.objects.filter(user=request.user, is_primary = False)
            for store in all_stores:
                child_serializer = CreatePropertyDealSerializer(data=request.data, context={'request': request})
                child_serializer.is_valid(raise_exception=True)
                child_deal = child_serializer.save(active=True,location=store.location, parent=deal, all_stores=False)

                for image in list(images):
                    deal_img = DealImage(deal=child_deal, image=image)
                    deal_img.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Deal created successfully")
        })


class UpdatePropertyDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser,
                          IsRealEstateBusinessCategory)

    def post(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id, user=request.user, active=True)
        except:
            return Response({
                'status': False,
                'message': _("Invalid property deal")
            })

        # sub category check start
        if "business_sub_category" not in request.data:
            return Response({
                'status': False,
                'field': 'business_sub_category',
                'message': _("Business Sub Category is required")
            })

        business_sub_category = int(request.data["business_sub_category"])

        real_estate_category = BusinessCategory.objects.get(
            keyword='real_estate')
        real_estate_sub_categories = [
            category.id for category in BusinessCategory.objects.filter(parent=real_estate_category)]

        if business_sub_category not in real_estate_sub_categories:
            return Response({
                'status': False,
                'field': 'business_sub_category',
                'message': _("For creating Real Estate deal, the business category can be rent,sale or vacational rental only")
            })

        try:
            sub_category = BusinessCategory.objects.get(
                id=business_sub_category)
        except:
            return Response({
                'status': False,
                'field': 'free_member_discount_type',
                'message': _("Free member discount type is required")
            })

        sub_category = sub_category.keyword

        if sub_category == 'vacation_rental':

            if 'free_member_discount_type' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_discount_type',
                    'message': _("Free member discount type is required")
                })
            if 'free_member_discount_value' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_discount_value',
                    'message': _("Free member discount value is required")
                })
            if 'free_member_code' not in request.data:
                return Response({
                    'status': False,
                    'field': 'free_member_code',
                    'message': _("Free member code is required")
                })
            if 'club_member_discount_type' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_discount_type',
                    'message': _("Club member discount type is required")
                })
            if 'club_member_discount_value' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_discount_value',
                    'message': _("Club member discount value is required")
                })
            if 'club_member_code' not in request.data:
                return Response({
                    'status': False,
                    'field': 'club_member_code',
                    'message': _("Club member code is required")
                })

        if sub_category == 'rent':
            if "offer_text" not in request.data:
                raise serializers.ValidationError({
                    "offer_text": _("Offer text is required")
                })

        if sub_category == 'vacation_rental':
            if "price_type" not in request.data:
                raise serializers.ValidationError({
                    "price_type": _("Price type is required")
                })

        # sub category check end

        serializer = CreatePropertyDealSerializer(
            deal, data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()

        property_serializer = PropertySerializer(
            deal.property_detail, data=request.data)
        property_serializer.is_valid(raise_exception=True)
        property_serializer.save()

        location_serializer = LocationSerializer(
            deal.location, data=request.data, context={'request': request})
        location_serializer.is_valid(raise_exception=True)
        location_serializer.save()

        # save images
        images = request.FILES.getlist('images')
        for image in list(images):
            deal_img = DealImage(deal=deal, image=image)
            deal_img.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message': _("Property deal updated successfully")
        })


class OthersWeeklyDealsListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')
        today = datetime.datetime.now().date()

        if not request.user.is_anonymous:
            deals = active_deals().filter(weekly=True).exclude(
                user=request.user).order_by("-id")
        else:
            deals = active_deals().filter(weekly=True).order_by("-id")

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))

        # filters start
        filter_by = request.GET.get('filter_by')
        if filter_by == "recent":
            deals = deals.order_by("-id")
        elif filter_by == "oldest":
            deals = deals.order_by("id")
        # filters end

        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            business_user_ids = [usr.id for usr in MyUser.objects.filter(
                ngo=search_by_ngo, is_deleted=False, is_approved=True, is_verified=True)]
            if business_user_ids:
                deals = deals.filter(user__in=business_user_ids)
            else:
                deals = deals.none()
        # search end

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, 6)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class MyWeeklyDealsListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')
        today = datetime.datetime.now().date()

        deals = active_deals().filter(weekly=True, user=request.user).order_by("-id")

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))

        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            business_user_ids = [
                usr.id for usr in MyUser.objects.filter(ngo=search_by_ngo)]
            if business_user_ids:
                deals = deals.filter(user__in=business_user_ids)
            else:
                deals = deals.none()
        # search end

        # filters start
        filter_by = request.GET.get('filter_by')
        if filter_by == "recent":
            deals = deals.order_by("-id")
        elif filter_by == "oldest":
            deals = deals.order_by("id")
        # filters end

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, 6)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class AddDealReviewView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        serializer = AddDealReviewSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        try:
            already_reviewed = Review.objects.get(
                deal=request.data["deal"], reviewed_by=request.user)
        except:
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review added successfully.")
            })

        if already_reviewed:
            return Response({
                'status': False,
                'message': _("Already reviewed")
            })


class DealReviewListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, deal_id):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')

        try:
            deal = Deal.objects.get(id=deal_id)
        except:
            return Response({
                "staus": False,
                "message": _("Invalid Deal")
            })

        reviews = Review.objects.filter(deal=deal)

        try:
            reviewed_by_logged_user = Review.objects.get(
                deal=deal, reviewed_by=request.user)
        except:
            reviewed_by_logged_user = False

        if reviewed_by_logged_user:
            reviewed_by_logged_user = True

        total_reviews = reviews.count()
        reviews_aggr = reviews.aggregate(Sum('rating'))
        sum_of_reviews = reviews_aggr['rating__sum']
        if sum_of_reviews:
            average_reviews = sum_of_reviews/total_reviews
        else:
            average_reviews = 0

        extra_data = {
            "reviewed_by_logged_user": reviewed_by_logged_user,
            "total_reviews": total_reviews,
            "average_reviews": average_reviews
        }

        if pagination_on:
            return paginated_data(reviews, DealReviewDetailSerializer, request, items_per_page, extra_data=extra_data)
        else:
            serializer = DealReviewDetailSerializer(
                reviews, many=True, context={'user': request.user})
            data = serializer.data

            return Response({
                "status": True,
                "data": data,
                "extra_data": extra_data
            })


class DealReviewMarkUsefulView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            review = Review.objects.get(id=request.data.get("review"))
        except:
            return Response({
                "status": False,
                "message": _("Invalid Review")
            })

        try:
            already_marked = ReviewMark.objects.get(
                user=request.user, review=review)
        except:
            serializer = ReviewMarkSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review marked successfully.")
            })

        if already_marked:
            return Response({
                'status': False,
                'message': _("Already marked")
            })


class DealReviewAddFlagView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            review = Review.objects.get(id=request.data.get("review"))
        except:
            return Response({
                "status": False,
                "message": _("Invalid Review")
            })

        try:
            already_flagged = ReviewFlag.objects.get(
                user=request.user, review=review)
        except:
            serializer = ReviewFlagSerializer(
                data=request.data, context={"request": request})
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Review flagged successfully.")
            })

        if already_flagged:
            return Response({
                'status': False,
                'message': _("Already flagged")
            })


class RecommendedDealsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')
        wishlist_deals = [
            deal.id for deal in request.user.favourite_deal.all()]
        business_deals = active_deals().filter(
            id__in=wishlist_deals, weekly=False).order_by("-id")
        to_currency = self.request.GET.get('to_currency')

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            business_deals = business_deals.filter(
                Q(title__icontains=search_key) | Q(description__icontains=search_key))
        # search end

        if pagination_on:
            return paginated_data(business_deals, BusinessDealSerializer, request, items_per_page)
        else:
            serializer = BusinessDealSerializer(business_deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class UserRecommendedDealsView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, user_id):

        to_currency = self.request.GET.get('to_currency')

        try:
            user = MyUser.objects.get(pk=user_id)
        except:
            return Response({
                "status": False,
                "message": _("Invalid User")
            })

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')
        wishlist_deals = [deal.id for deal in user.favourite_deal.all()]
        print("wishlist_deals", wishlist_deals)
        business_deals = active_deals().filter(
            id__in=wishlist_deals, weekly=False).order_by("-id")

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            business_deals = business_deals.filter(
                Q(title__icontains=search_key) | Q(description__icontains=search_key))
        # search end

        if pagination_on:
            return paginated_data(business_deals, BusinessDealSerializer, request, items_per_page)
        else:
            serializer = BusinessDealSerializer(business_deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class BusinessCategoryDealsView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, business_category):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')
        business_sub_category = request.GET.get('business_sub_category')
        business_sub_sub_category = request.GET.get(
            'business_sub_sub_category')
        date_listed = request.GET.get('date_listed')
        hamsa_business = request.GET.get('hamsa_business')
        price_range_min = request.GET.get('price_range_min')
        price_range_max = request.GET.get('price_range_max')
        star_rating = request.GET.get('star_rating')
        delivery_service = request.GET.get('delivery_service')
        name_of_business = request.GET.get('name_of_business')
        property_class = request.GET.get('property_class')
        number_of_travellers = request.GET.get('number_of_travellers')
        deal_by_discount = request.GET.get('deal_by_discount')
        expiration_date = request.GET.get('expiration_date')
        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')

        deals = active_deals().filter(user__business_category__keyword=business_category,
                                      weekly=False).order_by("-id")

        if business_sub_category:
            deals = deals.filter(business_sub_category=business_sub_category)
        if business_sub_sub_category:
            deals = deals.filter(
                business_sub_sub_category=business_sub_sub_category)
        if date_listed:
            deals = deals.order_by("-created_at")
        if hamsa_business:
            deals = deals.filter(Q(user__plan_id=4) | Q(user__plan_id=5))
        if price_range_min and price_range_max:
            deals = deals.filter(
                actual_price__gte=price_range_min, actual_price__lte=price_range_max)
        if star_rating:
            deals = deals.annotate(average_rating=Avg('deal_reviews__rating')).filter(
                average_rating__gte=star_rating)
            search_lat, search_lon = '', ''
        if delivery_service:
            deals = deals.filter(user__delivery_partner=delivery_service)
        if name_of_business:
            deals = deals.filter(user__name__icontains=name_of_business)
        if expiration_date:
            deals = deals.order_by("expiry_date")
        if number_of_travellers:
            deals = deals.filter(number_of_travellers=number_of_travellers)
        if property_class:
            deals = deals.filter(property_class__icontains=property_class)
        if deal_by_discount:
            deals = deals.order_by(
                "-free_member_discount_value", "-club_member_discount_value")
        if search_lat and search_lon:
            deals = nearest_deals(deals, search_lat, search_lon)

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))
        # search end

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, items_per_page)
        else:
            serializer = BusinessDealSerializer(deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })


class AllBusinessCategoryDealsView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')

        deals = active_deals().filter(weekly=False).order_by("-id")

        # search start
        business_category = request.GET.get('business_category')
        if business_category:
            deals = deals.filter(
                user__business_category__keyword=business_category)

        business_sub_category = request.GET.get('business_sub_category')
        if business_sub_category:
            deals = deals.filter(business_sub_category=business_sub_category)

        search_key = request.GET.get('search_key')
        if search_key:
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))

        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')
        if search_lat and search_lon:
            deals = nearest_deals(deals, search_lat, search_lon)

        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            business_user_ids = [
                usr.id for usr in MyUser.objects.filter(ngo=search_by_ngo)]
            if business_user_ids:
                deals = deals.filter(user__in=business_user_ids)
            else:
                deals = deals.none()
        # search end

        # sort by start
        sort_by = request.GET.get('sort_by')
        if sort_by:
            if sort_by == 'latest':
                deals = deals.order_by('-id')
            elif sort_by == 'oldest':
                deals = deals.order_by('id')
        # sort by end

        if pagination_on:
            return paginated_data(deals, BusinessDealSerializer, request, items_per_page)
        else:
            serializer = BusinessDealSerializer(
                deals, many=True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })


class RealEstateDealsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, business_sub_category):

        to_currency = self.request.GET.get('to_currency')
        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        business_sub_sub_category = request.GET.get(
            'business_sub_sub_category')
        no_of_bedroom = request.GET.get('no_of_bedroom')
        no_of_bathroom = request.GET.get('no_of_bathroom')
        sq_ft = request.GET.get('sq_ft')
        expiration_date = request.GET.get('expiration_date')
        hamsa_business = request.GET.get('hamsa_business')
        date_listed = request.GET.get('date_listed')
        price_range_min = request.GET.get('price_range_min')
        price_range_max = request.GET.get('price_range_max')
        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')

        real_estate_deals = active_deals().filter(business_sub_category=business_sub_category,
                                                  user__business_category__keyword='real_estate').order_by("-id")

        if business_sub_sub_category:
            real_estate_deals = real_estate_deals.filter(
                business_sub_sub_category=business_sub_sub_category)
        if date_listed:
            real_estate_deals = real_estate_deals.order_by("-created_at")
        if hamsa_business:
            real_estate_deals = real_estate_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if price_range_min and price_range_max:
            real_estate_deals = real_estate_deals.filter(
                property_detail__price__gte=price_range_min, property_detail__price__lte=price_range_max)
        if no_of_bedroom:
            real_estate_deals = real_estate_deals.filter(
                property_detail__no_of_bedroom=no_of_bedroom)
        if no_of_bathroom:
            real_estate_deals = real_estate_deals.filter(
                property_detail__no_of_bathroom=no_of_bathroom)
        if sq_ft:
            real_estate_deals = real_estate_deals.filter(
                property_detail__sq_feet__gte=sq_ft)
        if expiration_date:
            real_estate_deals = real_estate_deals.order_by("expiry_date")
        if search_lat and search_lon:
            real_estate_deals = nearest_deals(
                real_estate_deals, search_lat, search_lon)

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            real_estate_deals = real_estate_deals.filter(
                Q(title__icontains=search_key) | Q(description__icontains=search_key))
        # search end

        if pagination_on:
            return paginated_data(real_estate_deals, PropertyDealSerializer, request, items_per_page)
        else:
            serializer = PropertyDealSerializer(real_estate_deals, many=True, context={
                                                'to_currency': to_currency, 'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })


class AllRealEstateDealsView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        business_sub_category = request.GET.get('business_sub_category')
        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')

        deals = active_deals().filter(business_sub_category=business_sub_category,
                                      user__business_category__keyword='real_estate').order_by("-id")

        # search start
        search_key = request.GET.get('search_key')
        if search_key:
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))
        # search end

        # sort by start
        sort_by = request.GET.get('sort_by')
        if sort_by:
            if sort_by == 'latest':
                deals = deals.order_by('-id')
            elif sort_by == 'oldest':
                deals = deals.order_by('id')
        # sort by end

        if pagination_on:
            return paginated_data(deals, PropertyDealSerializer, request, items_per_page)
        else:
            serializer = PropertyDealSerializer(
                deals, many=True, context={'user': request.user})
            return Response({
                'status': True,
                'data': serializer.data
            })


class AddRemoveFavouriteDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id, active=True)
        except:
            return Response({
                'status': False,
                'message': _("This deal does not exist.")
            })

        if deal in request.user.favourite_deal.all():
            request.user.favourite_deal.remove(deal)
            status = "removed from"
        else:
            request.user.favourite_deal.add(deal)
            status = "added to"

        message = "Deal {} favourite deals".format(status)

        return Response({
            'status': True,
            'message': _(message)
        })
    
def send_redeem_email(deal, user):
    subject = '[Shuk.tv] Redeem Deal'
    plaintext = get_template('emails/redeem-deal-email.txt')
    htmly = get_template('emails/redeem-deal-email.html')
    d = {'deal': deal, 'user': user}
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    # print(html_content)
    # print('user.email',user.email)
    try:
        status = send_email(user.email, subject, text_content, html_content)
    except:
        status = False
    return status

def send_redeem_email_to_business(deal, deal_user, user):
    subject = '[Shuk.tv] Redeem Deal'
    plaintext = get_template('emails/redeem-deal-business-email.txt')
    htmly = get_template('emails/redeem-deal-business-email.html')
    d = {'deal': deal, 'user': user, 'deal_user': deal_user}
    text_content = plaintext.render(d)
    html_content = htmly.render(d)
    # return html_content
    try:
        status = send_email(deal_user.email, subject, text_content, html_content)
    except:
        status = False
    return status


class RedeemDealView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, deal_id):

        try:
            deal = Deal.objects.get(id=deal_id, active=True)
        except:
            return Response({
                'status': False,
                'message': _("This deal does not exist.")
            })

        DealRedeem.objects.create(
            deal=deal,
            user=request.user
        )

        send_redeem_email(deal, request.user)
        send_redeem_email_to_business(deal, deal.user, request.user)
        
        return Response({
            'status': True,
            'message': _("Deal redeemed successfully. The redemption details have been sent to your registered email.")
        })


class DealRedeemersView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, deal_id):

        search_key = request.GET.get('search_key')

        try:
            deal = Deal.objects.get(id=deal_id, active=True)
        except:
            return Response({
                'status': False,
                'message': _("This deal does not exist.")
            })

        deal_redeems = DealRedeem.objects.filter(deal=deal)
        
        if search_key:
            deal_redeems = deal_redeems.filter(Q(user__firstname__icontains = search_key)|Q(user__lastname__icontains = search_key) | Q(user__name__icontains = search_key) | Q(user__phone__icontains = search_key))
        
        serializer = DealRedeemSerializer(deal_redeems, many=True)
        
        return Response({
            'status': True,
            'data': serializer.data
        })


class RedeemedDealslist(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')
        to_currency = self.request.GET.get('to_currency')
        start_date = self.request.GET.get('start_date')
        end_date = self.request.GET.get('end_date')

        search_key = request.GET.get('search_key')

        my_redeems = DealRedeem.objects.filter(user=request.user)

        # date filter
        if start_date and end_date:
            try:
                my_redeems = my_redeems.filter(
                    created_at__date__gte=start_date, created_at__date__lte=end_date)
            except:
                return Response({
                    "status": False,
                    "message": _("The date format seems wrong. Please send date as: 2024-02-01")
                })

        deal_ids = [redeem.deal.id for redeem in my_redeems]
        redeemed_deals = Deal.objects.filter(id__in=deal_ids)

        if search_key:
            redeemed_deals = redeemed_deals.filter(
                Q(title__icontains=search_key) | Q(description__icontains=search_key))

        if pagination_on:
            return paginated_data(redeemed_deals, BusinessDealSerializer, request, items_per_page)
        else:
            serializer = BusinessDealSerializer(redeemed_deals, many=True, context={
                                                'user': request.user, 'to_currency': to_currency})
            return Response({
                "status": True,
                "data": serializer.data
            })



class AddDealFlagView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            deal = Deal.objects.get(id=request.data["deal"], active=True)
        except:
            return Response({
                'status': False,
                'message': _("This deal does not exist.")
            })

        serializer = AddDealFlagSerializer(
            data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)

        try:
            already_flagged = Flagged.objects.get(
                deal=deal, flagged_by=request.user)
        except:
            serializer.save()
            return Response({
                'status': True,
                'data': serializer.data,
                'message': _("Flagged successfully.")
            })

        if already_flagged:
            return Response({
                'status': False,
                'message': _("Already flagged.")
            })


class MasterSearchParamView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        param_type = request.GET.get('param_type')
        param_tag = request.GET.get('param_tag')

        params = []

        if param_type == 'ngo':

            params = [
                {"title": _("NGO Category"), "param": "ngo_category",
                    'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Joined(Newest To Oldest)"),
                 "param": "sort_by_date_joined", 'param_tag': 'sort'},
                {"title": "Star Rating", "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Number of Club Members Associated"),
                    "param": "sort_by_members_associated", 'param_tag': 'sort'},
                {"title": _("Number of Businesses Associated"),
                    "param": "sort_by_business_associated", 'param_tag': 'sort'},
            ]

        if param_type == 'businesses':

            params = [
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Joined(Newest To Oldest)"),
                 "param": "sort_by_date_joined", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
            ]

        if param_type == 'member':

            params = [
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Joined(Newest To Oldest)"),
                 "param": "sort_by_date_joined", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
            ]

        if param_type == 'classified':

            params = [
                {"title": _("Classified Category"),
                    "param": "classified_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Members"),
                    "param": "hamsa_members", 'param_tag': 'sort'},
                {"title": _("Price Range (Minimum / Maximum)"), "param1": "price_range_min",
                 "param2": "price_range_max", 'param_tag': 'filter'},
                {"title": _("Condition (New - Used)"),
                 "param": "product_condition", 'param_tag': 'filter'}
            ]

        if param_type == 'product':

            params = [
                {"title": _("Product Category"),
                    "param": "business_sub_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Price Range (Minimum / Maximum)"), "param1": "price_range_min",
                 "param2": "price_range_max", 'param_tag': 'filter'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
            ]

        if param_type == 'service':
            params = [
                {"title": _("Service Category"),
                    "param": "business_sub_category", 'param_tag': 'category'},
                {"title":_("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Price Range (Minimum / Maximum)"), "param1": "price_range_min",
                 "param2": "price_range_max", 'param_tag': 'filter'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Provider Type"), "param": "provider_type",
                    'param_tag': 'filter'},
            ]

        if param_type == 'restaurant':
            params = [
                {"title": _("Restaurant Category"),
                    "param": "business_sub_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Delivery Service"),
                    "param": "delivery_service", 'param_tag': 'filter'},
                {"title": _("Reservation/Walkin"),
                    "param": "reservation_walkin", 'param_tag': 'filter'},
                {"title": _("Deal by Discount"),
                    "param": "deal_by_discount", 'param_tag': 'sort'}
            ]

        if param_type == 'travel':
            params = [
                {"title": _("Restaurant Category"),
                    "param": "business_sub_category", 'param_tag': 'category'},
                {"title": _("Name Of Business"),
                    "param": "name_of_business", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Price Range (Minimum / Maximum)"), "param1": "price_range_min",
                 "param2": "price_range_max", 'param_tag': 'filter'},
                {"title": _("Expiration Date"),
                    "param": "expiration_date", 'param_tag': 'sort'},
                {"title": _("Number Of Travellers"),
                    "param": "number_of_travellers", 'param_tag': 'filter'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Property Class"),
                    "param": "property_class", 'param_tag': 'filter'},
                {"title": _("Deal by Discount"),
                    "param": "deal_by_discount", 'param_tag': 'sort'}
            ]

        if param_type == 'rent':
            params = [
                {"title": _("Rent Category"), "param": "business_sub_sub_category",
                    'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Number Of Bedrooms"),
                    "param": "no_of_bedroom", 'param_tag': 'filter'},
                {"title": _("No Of Bathroom"),
                    "param": "no_of_bathroom", 'param_tag': 'filter'},
                {"title": _("SQ FT"), "param": "sq_ft", 'param_tag': 'filter'}
            ]

        if param_type == 'vacation_rental':
            params = [
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Number Of Bedrooms"),
                    "param": "no_of_bedroom", 'param_tag': 'filter'},
                {"title": _("No Of Bathroom"),
                    "param": "no_of_bathroom", 'param_tag': 'filter'},
                {"title": _("SQ FT"), "param": "sq_ft", 'param_tag': 'filter'},
                {"title": _("Expiration Date"),
                    "param": "expiration_date", 'param_tag': 'sort'}
            ]

        if param_type == 'sale':
            params = [
                {"title": _("Sale Category"), "param": "business_sub_sub_category",
                    'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Price Range (Minimum / Maximum)"), "param1": "price_range_min",
                 "param2": "price_range_max", 'param_tag': 'filter'},
                {"title": _("Number Of Bedrooms"),
                    "param": "no_of_bedroom", 'param_tag': 'filter'},
                {"title": _("No Of Bathroom"),
                    "param": "no_of_bathroom", 'param_tag': 'filter'},
                {"title": _("SQ FT"), "param": "sq_ft", 'param_tag': 'filter'},
                {"title": _("Expiration Date"),
                    "param": "expiration_date", 'param_tag': 'sort'}
            ]

        if param_type == 'venue':
            params = [
                {"title": _("Venue Category"),
                    "param": "business_sub_sub_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Deal by Discount"),
                    "param": "deal_by_discount", 'param_tag': 'sort'}
            ]

        if param_type == 'sports':
            params = [
                {"title": _("Sports Category"),
                    "param": "business_sub_sub_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Deal by Discount"),
                    "param": "deal_by_discount", 'param_tag': 'sort'}
            ]

        if param_type == 'movie':
            params = [
                {"title": _("Movie Category"),
                    "param": "business_sub_sub_category", 'param_tag': 'category'},
                {"title": _("Distance(Near To Far)"),
                 "param": "near_to_far", 'param_tag': 'sort'},
                {"title": _("Date Listed (Newest to Oldest)"),
                 "param": "date_listed", 'param_tag': 'sort'},
                {"title": _("Hamsa Business"),
                    "param": "hamsa_business", 'param_tag': 'sort'},
                {"title": _("Star Rating"), "param": "star_rating", 'param_tag': 'filter'},
                {"title": _("Deal by Discount"),
                    "param": "deal_by_discount", 'param_tag': 'sort'}
            ]

        filtered_tags = []
        if param_tag:
            for param in params:
                if param["param_tag"] == param_tag:
                    filtered_tags.append(param)

            params = filtered_tags

        return Response({
            "status": True,
            "params": params
        })


class MasterSearchView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        search_key = request.GET.get('search_key')
        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')
        business_category = request.GET.get('business_category')
        module_type = request.GET.get('module_type')
        items_per_page = self.request.GET.get('items_per_page')
        pagination_on = self.request.GET.get('pagination_on')

        # deals start
        business_sub_category = request.GET.get('business_sub_category')
        business_sub_sub_category = request.GET.get(
            'business_sub_sub_category')

        deals = active_deals()
        if business_sub_category:
            deals = deals.filter(business_sub_category=business_sub_category)
        if business_sub_sub_category:
            deals = deals.filter(
                business_sub_sub_category=business_sub_sub_category)
        # deals end

        # ngos start
        ngo_category = request.GET.get('ngo_category')
        sort_by_date_joined = request.GET.get('sort_by_date_joined')
        star_rating = request.GET.get('star_rating')
        sort_by_members_associated = request.GET.get(
            'sort_by_members_associated')
        sort_by_business_associated = request.GET.get(
            'sort_by_business_associated')

        ngos = active_users().filter(user_type='ngo')
        if ngo_category:
            ngos = ngos.filter(user_type_category_id=ngo_category)
        if sort_by_date_joined:
            ngos = ngos.order_by("-created_at")
        if star_rating:
            ngos = ngos.annotate(average_rating=Avg('reviews__rating')).filter(
                average_rating__gte=star_rating)
        if sort_by_members_associated:
            ngos = ngos.annotate(total_members=Count('ngos_associated', filter=Q(
                ngos_associated__user_type='member'))).order_by('-total_members')
            search_lat,search_lon = '',''
        if sort_by_business_associated:
            ngos = ngos.annotate(total_members=Count('ngos_associated', filter=Q(
                ngos_associated__user_type='business'))).order_by('-total_members')
            search_lat,search_lon = '',''

        # ngos end

        # classifieds start
        classified_category = request.GET.get('classified_category')
        date_listed = request.GET.get('date_listed')
        hamsa_members = request.GET.get('hamsa_members')
        price_range_min = request.GET.get('price_range_min')
        price_range_max = request.GET.get('price_range_max')
        product_condition = request.GET.get('product_condition')

        classifieds = active_classifieds()

        if classified_category:
            classifieds = classifieds.filter(category_id=classified_category)
        if date_listed:
            classifieds = classifieds.order_by("-created_at")
        if hamsa_members:
            classifieds = classifieds.filter(user__plan_id=2)
        if price_range_min and price_range_max:
            classifieds = classifieds.filter(
                price__gte=price_range_min, price__lte=price_range_max)
        if product_condition:
            classifieds = classifieds.filter(
                product_condition=product_condition)

        # classifieds end

        # businesses start
        business_profiles = active_businesses().filter(
            user_type='business').exclude(id=request.user.id).order_by("-plan")
        member_profiles = active_users().filter(user_type='member').exclude(
            id=request.user.id).order_by("-plan")

        if sort_by_date_joined:
            business_profiles = business_profiles.order_by("-created_at")
            member_profiles = member_profiles.order_by("-created_at")
        if star_rating:
            business_profiles = business_profiles.annotate(average_rating=Avg(
                'reviews__rating')).filter(average_rating__gte=star_rating)
            member_profiles = member_profiles.annotate(average_rating=Avg(
                'reviews__rating')).filter(average_rating__gte=star_rating)

        if business_category:
            classifieds = classifieds.none()
            if business_category == 'ngo':
                deals = deals.none()
                classifieds = classifieds.none()
                business_profiles = business_profiles.none()
            elif business_category == 'business':
                deals = deals.none()
                classifieds = classifieds.none()
                ngos = ngos.none()
            else:
                deals = deals.filter(
                    user__business_category__keyword=business_category)
                ngos = ngos.none()
                business_profiles = business_profiles.none()

        if module_type:
            if module_type == 'ngo':
                deals = deals.none()
                classifieds = classifieds.none()
                business_profiles = business_profiles.none()
                member_profiles = member_profiles.none()
            elif module_type == 'businesses':
                deals = deals.none()
                classifieds = classifieds.none()
                ngos = ngos.none()
                member_profiles = member_profiles.none()
            elif module_type == 'members':
                deals = deals.none()
                classifieds = classifieds.none()
                ngos = ngos.none()
                business_profiles = business_profiles.none()
            elif module_type == 'classified':
                deals = deals.none()
                ngos = ngos.none()
                business_profiles = business_profiles.none()
                member_profiles = member_profiles.none()
            else:
                classifieds = classifieds.none()
                deals = deals.filter(
                    user__business_category__keyword=module_type)
                ngos = ngos.none()
                business_profiles = business_profiles.none()
                member_profiles = member_profiles.none()

        # business end

        # location near to far start
        if search_lat and search_lon:
            deals = nearest_deals(deals, search_lat, search_lon)
            ngos = nearest_users(ngos, search_lat, search_lon)
            classifieds = nearest_classifieds(
                classifieds, search_lat, search_lon)
            business_profiles = nearest_users(
                business_profiles, search_lat, search_lon)
            member_profiles = nearest_users(
                member_profiles, search_lat, search_lon)
        # location near to far end

        if search_key:
            deals = deals.filter(Q(title__icontains=search_key) | Q(
                description__icontains=search_key))

        # real estate deals start
        business_sub_sub_category = request.GET.get(
            'business_sub_sub_category')
        no_of_bedroom = request.GET.get('no_of_bedroom')
        no_of_bathroom = request.GET.get('no_of_bathroom')
        sq_ft = request.GET.get('sq_ft')
        expiration_date = request.GET.get('expiration_date')
        hamsa_business = request.GET.get('hamsa_business')

        real_estate_deals = deals.filter(
            user__business_category__keyword='real_estate')

        if business_sub_sub_category:
            real_estate_deals = real_estate_deals.filter(
                business_sub_sub_category=business_sub_sub_category)
        if date_listed:
            real_estate_deals = real_estate_deals.order_by("-created_at")
        if hamsa_business:
            real_estate_deals = real_estate_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if price_range_min and price_range_max:
            real_estate_deals = real_estate_deals.filter(
                property_detail__price__gte=price_range_min, property_detail__price__lte=price_range_max)
        if no_of_bedroom:
            real_estate_deals = real_estate_deals.filter(
                property_detail__no_of_bedroom=no_of_bedroom)
        if no_of_bathroom:
            real_estate_deals = real_estate_deals.filter(
                property_detail__no_of_bathroom=no_of_bathroom)
        if sq_ft:
            real_estate_deals = real_estate_deals.filter(
                property_detail__sq_feet__gte=sq_ft)
        if expiration_date:
            real_estate_deals = real_estate_deals.order_by("expiry_date")
        # real estate deals end
        weekly_deals = deals.filter(weekly=True)

        # product deals start

        product_deals = deals.filter(
            user__business_category__keyword="product")
        if business_sub_category:
            product_deals = product_deals.filter(
                business_sub_category=business_sub_category)
        if date_listed:
            product_deals = product_deals.order_by("-created_at")
        if hamsa_business:
            product_deals = product_deals.filter(
                Q(user__plan_id=4) | Q(user__plan__id=5))
        if price_range_min and price_range_max:
            product_deals = product_deals.filter(
                actual_price__gte=price_range_min, actual_price__lte=price_range_max)
        if star_rating:
            product_deals = product_deals.annotate(average_rating=Avg(
                'deal_reviews__rating')).filter(average_rating__gte=star_rating)

        # product deals end

        # service deals start
        provider_type = request.GET.get('provider_type')
        service_deals = deals.filter(
            user__business_category__keyword="service")

        if business_sub_category:
            service_deals = service_deals.filter(
                business_sub_category=business_sub_category)
        if date_listed:
            service_deals = service_deals.order_by("-created_at")
        if hamsa_business:
            service_deals = service_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if star_rating:
            service_deals = service_deals.annotate(average_rating=Avg(
                'deal_reviews__rating')).filter(average_rating__gte=star_rating)
        if provider_type:
            service_deals = service_deals.filter(
                user__service_provider_type=provider_type)

        # service deals end

        # restaurant deals start
        delivery_service = request.GET.get('delivery_service')
        restaurant_deals = deals.filter(
            user__business_category__keyword="restaurant")

        if business_sub_category:
            restaurant_deals = restaurant_deals.filter(
                business_sub_category=business_sub_category)
        if hamsa_business:
            restaurant_deals = restaurant_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if star_rating:
            restaurant_deals = restaurant_deals.annotate(average_rating=Avg(
                'deal_reviews__rating')).filter(average_rating__gte=star_rating)
        if delivery_service:
            restaurant_deals = restaurant_deals.filter(
                user__delivery_partner__isnull=False)

        # restaurant deals end

        # travel deal start
        name_of_business = request.GET.get('name_of_business')
        travel_deals = deals.filter(user__business_category__keyword="travel")
        property_class = request.GET.get('property_class')
        number_of_travellers = request.GET.get('number_of_travellers')
        deal_by_discount = request.GET.get('deal_by_discount')

        if business_sub_category:
            travel_deals = travel_deals.filter(
                business_sub_category=business_sub_category)
        if name_of_business:
            travel_deals = travel_deals.filter(
                user__name__icontains=name_of_business)
        if hamsa_business:
            travel_deals = travel_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if price_range_min and price_range_max:
            travel_deals = travel_deals.filter(
                actual_price__gte=price_range_min, actual_price__lte=price_range_max)
        if expiration_date:
            travel_deals = travel_deals.order_by("expiry_date")
        if number_of_travellers:
            travel_deals = travel_deals.filter(
                number_of_travellers=number_of_travellers)
        if property_class:
            travel_deals = travel_deals.filter(
                property_class__icontains=property_class)
        if deal_by_discount:
            travel_deals = travel_deals.order_by(
                "-free_member_discount_value", "-club_member_discount_value")
        if star_rating:
            travel_deals = travel_deals.annotate(average_rating=Avg(
                'deal_reviews__rating')).filter(average_rating__gte=star_rating)
        # travel deal end

        # real estate rent deals start

        rent_deals = real_estate_deals.filter(business_sub_category=10)

        # real estate rent deals end

        # real estate vacational rental deals start
        vacation_deals = real_estate_deals.filter(business_sub_category=11)

        # real estate vacational rental deals end

        # real estate sale deals start
        sale_deals = real_estate_deals.filter(business_sub_category=12)
        # real estate sale deals end

        # sports entertainment deals start
        sports_entertainment_deals = deals.filter(
            user__business_category__keyword='entertainment_sport')

        if business_sub_sub_category:
            sports_entertainment_deals = sports_entertainment_deals.filter(
                business_sub_sub_category=business_sub_sub_category)
        if date_listed:
            sports_entertainment_deals = sports_entertainment_deals.order_by(
                "-created_at")
        if hamsa_business:
            sports_entertainment_deals = sports_entertainment_deals.filter(
                Q(user__plan_id=4) | Q(user__plan_id=5))
        if star_rating:
            sports_entertainment_deals = sports_entertainment_deals.annotate(
                average_rating=Avg('deal_reviews__rating')).filter(average_rating__gte=star_rating)
        if deal_by_discount:
            sports_entertainment_deals = sports_entertainment_deals.order_by(
                "-free_member_discount_value", "-club_member_discount_value")

        venue_deals = sports_entertainment_deals.filter(
            business_sub_category=13)
        sports_deals = sports_entertainment_deals.filter(
            business_sub_category=14)
        movie_deals = sports_entertainment_deals.filter(
            business_sub_category=15)

        # sports entertainment deals end

        # ngo deals start
        ngo_deals = deals.filter(user__user_type='ngo', weekly=False)
        # ngo deals end

        # search start

        if search_key:
            ngos = ngos.filter(name__icontains=search_key)
            classifieds = classifieds.filter(
                Q(title__icontains=search_key) | Q(description__icontains=search_key))
            business_profiles = business_profiles.filter(
                name__icontains=search_key)
            member_profiles = member_profiles.filter(
                Q(firstname__icontains=search_key) |
                Q(lastname__icontains=search_key) |
                Q(fullname__icontains=search_key)
            )

        # search end

        # counting start
        weekly_deals_count = weekly_deals.count()
        ngo_partners_count = ngos.count()
        classifieds_count = classifieds.count()
        business_profiles_count = business_profiles.count()
        member_profiles_count = member_profiles.count()
        product_deals_count = product_deals.count()
        service_deals_count = service_deals.count()
        restaurant_deals_count = restaurant_deals.count()
        travel_deals_count = travel_deals.count()
        venue_deals_count = venue_deals.count()
        sports_deals_count = sports_deals.count()
        movie_deals_count = movie_deals.count()
        vacation_deals_count = vacation_deals.count()
        rent_deals_count = rent_deals.count()
        sale_deals_count = sale_deals.count()
        ngo_deals_count = ngo_deals.count()


        total_count = ngo_deals_count + weekly_deals_count + ngo_partners_count + \
            classifieds_count + business_profiles_count + member_profiles_count
        total_count += product_deals_count + service_deals_count + \
            restaurant_deals_count + travel_deals_count
        total_count += venue_deals_count + sports_deals_count + movie_deals_count
        total_count += vacation_deals_count + rent_deals_count + sale_deals_count

        # counting end

        # limit result start
        if not pagination_on:
            weekly_deals = weekly_deals[0:4]
            ngos = ngos[0:4]
            classifieds = classifieds[0:4]
            business_profiles = business_profiles[0:4]
            member_profiles = member_profiles[0:4]
            product_deals = product_deals[0:4]
            service_deals = service_deals[0:4]
            restaurant_deals = restaurant_deals[0:4]
            travel_deals = travel_deals[0:4]
            venue_deals = venue_deals[0:4]
            sports_deals = sports_deals[0:4]
            movie_deals = movie_deals[0:4]
            vacation_deals = vacation_deals[0:4]
            rent_deals = rent_deals[0:4]
            sale_deals = sale_deals[0:4]
        # limit result end

        if module_type and pagination_on:

            if module_type == 'weekly':
                resp = paginated_data(
                    weekly_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'ngo':
                resp = paginated_data(
                    ngos, UserProfileSerializer, request, items_per_page)
            elif module_type == 'classified':
                resp = paginated_data(
                    classifieds, ClassifiedSerializer, request, items_per_page)
            elif module_type == 'businesses':
                return paginated_data(business_profiles, UserProfileSerializer, request, items_per_page)
            elif module_type == 'members':
                return paginated_data(member_profiles, UserProfileSerializer, request, items_per_page)
            elif module_type == 'product':
                return paginated_data(product_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'service':
                return paginated_data(service_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'restaurant':
                return paginated_data(restaurant_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'travel':
                return paginated_data(travel_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'ngo_deal':
                return paginated_data(ngo_deals, BusinessDealSerializer, request, items_per_page)
            elif module_type == 'real_estate':

                vacation_deals_serializer = paginated_data(
                    vacation_deals, PropertyDealSerializer, request, items_per_page)
                rent_deals_serializer = paginated_data(
                    rent_deals, PropertyDealSerializer, request, items_per_page)
                sale_deals_serializer = paginated_data(
                    sale_deals, PropertyDealSerializer, request, items_per_page)

                resp = {
                    "vacation_deals_count": vacation_deals_count,
                    "vacation_deals": vacation_deals_serializer.data,
                    "rent_deals_count": rent_deals_count,
                    "rent_deals": rent_deals_serializer.data,
                    "sale_deals_count": sale_deals_count,
                    "sale_deals": sale_deals_serializer.data
                }

                return Response({
                    'status': True,
                    'data': resp
                })
            elif module_type == 'entertainment_sport':

                venue_deals_serializer = paginated_data(
                    venue_deals, BusinessDealSerializer, request, items_per_page)
                sports_deals_serializer = paginated_data(
                    sports_deals, BusinessDealSerializer, request, items_per_page)
                movie_deals_serializer = paginated_data(
                    movie_deals, BusinessDealSerializer, request, items_per_page)

                resp = {
                    "venue_deals_count": venue_deals_count,
                    "venue_deals": venue_deals_serializer.data,
                    "sports_deals_count": sports_deals_count,
                    "sports_deals": sports_deals_serializer.data,
                    "movie_deals_count": movie_deals_count,
                    "movie_deals": movie_deals_serializer.data
                }

                return Response({
                    'status': True,
                    'data': resp
                })

            return resp
        else:
            weekly_deals_serializer = BusinessDealSerializer(
                weekly_deals, many=True, context={'user': request.user})
            ngo_partners_serializer = UserProfileSerializer(
                ngos, many=True, context={'user': request.user})
            classified_serializer = ClassifiedSerializer(
                classifieds, many=True, context={'user': request.user})
            business_profile_serializer = UserProfileSerializer(
                business_profiles, many=True, context={'user': request.user})
            member_profile_serializer = UserProfileSerializer(
                member_profiles, many=True, context={'user': request.user})
            product_deals_serializer = BusinessDealSerializer(
                product_deals, many=True, context={'user': request.user})
            service_deals_serializer = BusinessDealSerializer(
                service_deals, many=True, context={'user': request.user})
            restaurant_deals_serializer = BusinessDealSerializer(
                restaurant_deals, many=True, context={'user': request.user})
            travel_deals_serializer = BusinessDealSerializer(
                travel_deals, many=True, context={'user': request.user})

            vacation_deals_serializer = PropertyDealSerializer(
                vacation_deals, many=True, context={'user': request.user})
            rent_deals_serializer = PropertyDealSerializer(
                rent_deals, many=True, context={'user': request.user})
            sale_deals_serializer = PropertyDealSerializer(
                sale_deals, many=True, context={'user': request.user})

            venue_deals_serializer = BusinessDealSerializer(
                venue_deals, many=True, context={'user': request.user})
            sports_deals_serializer = BusinessDealSerializer(
                sports_deals, many=True, context={'user': request.user})
            movie_deals_serializer = BusinessDealSerializer(
                movie_deals, many=True, context={'user': request.user})
            ngo_deals_serializer = BusinessDealSerializer(
                ngo_deals, many=True, context={'user': request.user})

        resp = {
            "total_count": total_count,
            "weekly_deals_count": weekly_deals_count,
            "weekly_deals": weekly_deals_serializer.data,
            "ngo_partners_count": ngo_partners_count,
            "ngo_partners": ngo_partners_serializer.data,
            "classifieds_count": classifieds_count,
            "classifieds": classified_serializer.data,
            "business_profiles_count": business_profiles_count,
            "business_profiles": business_profile_serializer.data,
            "member_profiles_count": member_profiles_count,
            "member_profiles": member_profile_serializer.data,
            "product_deals_count": product_deals_count,
            "product_deals": product_deals_serializer.data,
            "service_deals_count": service_deals_count,
            "service_deals": service_deals_serializer.data,
            "restaurant_deals_count": restaurant_deals_count,
            "restaurant_deals": restaurant_deals_serializer.data,
            "travel_deals_count": travel_deals_count,
            "travel_deals": travel_deals_serializer.data,
            "venue_deals_count": venue_deals_count,
            "venue_deals": venue_deals_serializer.data,
            "sports_deals_count": sports_deals_count,
            "sports_deals": sports_deals_serializer.data,
            "movie_deals_count": movie_deals_count,
            "movie_deals": movie_deals_serializer.data,
            "vacation_deals_count": vacation_deals_count,
            "vacation_deals": vacation_deals_serializer.data,
            "rent_deals_count": rent_deals_count,
            "rent_deals": rent_deals_serializer.data,
            "sale_deals_count": sale_deals_count,
            "sale_deals": sale_deals_serializer.data,
            "ngo_deals_count": ngo_deals_count,
            "ngo_deals": ngo_deals_serializer.data
        }

        return Response({
            'status': True,
            'data': resp
        })
