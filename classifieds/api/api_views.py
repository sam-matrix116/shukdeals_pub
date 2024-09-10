from classifieds.models import *
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import *
from account.api.serializers import LocationSerializer
from django.utils.translation import gettext as _
from shuktv.utils.customPermissionClass import IsNormalUser
from shuktv.utils.customPaginations import paginated_data
from django.db.models import Q
from account.utils import check_plan_exceeded
from django.conf import settings
from account.models import PaymentDetail
from account.utils import convert_currency as __, get_single_product_cost
from classifieds.utils import active_classifieds
from deals.utils import *


class ClassifiedCategoryView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        categories = ClassifiedCategory.objects.all()
        serializer = ClassifiedCategorySerializer(categories, many=True, context={"request": request})

        return Response({
            "status": True,
            "data": serializer.data
        })


class CreateClassifiedView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self,request):

        # check if the user's limit has not reached based on plan
        if request.user.user_type == 'business' or request.user.user_type == 'member':
            if not request.user.plan:
                return Response({
                    "status": False,
                    "message":_("Please upgrade your plan")
                })

            plan_exceeded = check_plan_exceeded(request.user, 'classified')
            if plan_exceeded and not request.user.extra_classified:
                
                main_amount_in_usd = get_single_product_cost(request.user,'classified', '', 'main_amount')
                single_classified_cost_with_tax = main_amount_in_usd + int(settings.SHUKTV_TAX_COST)

                print('main_amount_in_usd',main_amount_in_usd)
                
                currency = 'usd'
                amount = single_classified_cost_with_tax
                if request.user.currency.iso_code != 'usd':
                    currency = request.user.currency.iso_code
                    amount = __(amount, 'usd', currency)

                # create a row in table payment details to store the payment details
                if main_amount_in_usd > 0:
                    payment_detail = PaymentDetail.objects.create(
                        user = request.user,
                        item_type = 'classified',
                        main_amount_in_usd = main_amount_in_usd,
                        amount = amount,
                        currency = currency
                    )

                    return Response({
                        'status': True,
                        'go_to': 'payment',
                        'payment_detail': payment_detail.id
                    })

        to_currency = self.request.GET.get('to_currency')

        if "images" not in request.data:
            return Response({
                'status': False,
                'field': 'images',
                'message':_("Image is required")
            })

        serializer = CreateClassifiedSerializer(data=request.data, context={'request': request, 'user': request.user, 'to_currency': to_currency})
        serializer.is_valid(raise_exception=True)
            
        # store location
        location_serializer = LocationSerializer(data=request.data, context={"request": request})
        location_serializer.is_valid(raise_exception=True) 
        location = location_serializer.save()
        
        # save classified
        classified = serializer.save(active=True)
        classified.location = location
        classified.save()

        # save images
        images = request.FILES.getlist('images')
        for image in list(images):
            cf_img = ClassifiedImage(classified = classified, image = image)
            cf_img.save()

        if (request.user.user_type == 'business' or request.user.user_type == 'member') and request.user.extra_classified:
            request.user.extra_classified = False
            request.user.save()

            classified.paid = True
            classified.shuk_fee = get_single_product_cost(request.user,'classified', '', 'shuk_fee')
            classified.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message':_("Classified created successfully")
        })

            
class MyClassifiedListView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')

        classifieds = active_classifieds().filter(user=request.user)
        
        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            classifieds = classifieds.filter(Q(title__icontains = search_key)|Q(description__icontains = search_key))

        # filters start
        filter_by = request.GET.get('filter_by')
        if filter_by == "recent":
            classifieds = classifieds.order_by("-id")
        elif filter_by == "oldest":
            classifieds = classifieds.order_by("id")
        # filters end

        return paginated_data(classifieds,ClassifiedSerializer,request,items_per_page)


class UpdateClassifiedView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self,request, classified_id):

        to_currency = self.request.GET.get('to_currency')

        try:
            classified = Classified.objects.get(id = classified_id, user=request.user,active=True)
        except:
            return Response({
                'status': False,
                'message':_("Invalid classified")
            })

        serializer = CreateClassifiedSerializer(classified, data=request.data, context={'request': request, 'user': request.user, 'to_currency': to_currency})
        serializer.is_valid(raise_exception=True)

        # store location
        location_serializer = LocationSerializer(classified.location, data=request.data, context={"request": request})
        location_serializer.is_valid(raise_exception=True) 
        location_serializer.save()

        serializer.save(active=True)

        # check if user wants to pin this classified, remove pin from other classifieds
        if "pinned" in request.data and request.data.get("pinned"):
            my_pinned_classifieds = active_classifieds().filter(pinned=True,user=request.user)
            for pinned_classified in my_pinned_classifieds:
                pinned_classified.pinned=False
                pinned_classified.save()

            classified.pinned = True
            classified.save()


        # save images
        if "images" in request.data:
            images = request.FILES.getlist('images')
            for image in list(images):
                cf_img = ClassifiedImage(classified = classified, image = image)
                cf_img.save()

        return Response({
            'status': True,
            'data': serializer.data,
            'message':_("Classified updated successfully")
        })
        

class DeleteClassifiedView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self,request, classified_id):

        try:
            classified = Classified.objects.get(id = classified_id, user=request.user,active=True)
        except:
            return Response({
                'status': False,
                'message':_("Invalid classified")
            })

        classified.delete()

        return Response({
            'status': True,
            'message':_("Classified deleted successfully")
        })


class ClassifiedDetailView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request, classified_id):

        to_currency = self.request.GET.get('to_currency')

        try:
            classified = Classified.objects.get(id = classified_id,active=True)
        except:
            return Response({
                'status': False,
                'message':_("Invalid classified")
            })
        
        # if we have a logged in user, increment its view-count
        if not request.user.is_anonymous and classified.user != request.user:
            try:
                ClassifiedClick.objects.get(classified=classified,user=request.user)
            except:
                ClassifiedClick.objects.create(
                    classified=classified,
                    user=request.user
                )

        serializer = ClassifiedSerializer(classified, context={'request': request, 'user': request.user, 'to_currency': to_currency})
        return Response({
            'status': True,
            'data': serializer.data,
            'message':_("Classified updated successfully")
        })
    

class OthersClassifiedListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request):

        items_per_page = self.request.GET.get('items_per_page')
        classified_category = request.GET.get('classified_category')
        date_listed = request.GET.get('date_listed')
        hamsa_members = request.GET.get('hamsa_members')
        price_range_min = request.GET.get('price_range_min')
        price_range_max = request.GET.get('price_range_max')
        product_condition = request.GET.get('product_condition')
        search_lat = request.GET.get('search_lat')
        search_lon = request.GET.get('search_lon')

        if request.user.is_anonymous:
            classifieds = active_classifieds()
        else:
            classifieds = active_classifieds().exclude(user=request.user)

        
        if classified_category:
            classifieds = classifieds.filter(category_id=classified_category)
        if date_listed:
            classifieds = classifieds.order_by("-created_at")
        if hamsa_members:
            classifieds = classifieds.filter(user__plan_id=2)
        if price_range_min and price_range_max:
            classifieds = classifieds.filter(price__gte=price_range_min, price__lte = price_range_max)
        if product_condition:
            classifieds = classifieds.filter(product_condition=product_condition)
        if search_lat and search_lon:
            classifieds = nearest_classifieds(classifieds, search_lat, search_lon)
        

        # search start
        search_key = self.request.GET.get('search_key')
        if search_key and search_key != '':
            classifieds = classifieds.filter(Q(title__icontains = search_key)|Q(description__icontains = search_key))

        search_by_ngo = request.GET.get('ngo')
        if search_by_ngo:
            business_user_ids = [usr.id for usr in MyUser.objects.filter(ngo = search_by_ngo)]
            if business_user_ids:
                classifieds = classifieds.filter(user__in = business_user_ids)
            else:
                classifieds = classifieds.none()
        # search end

        return paginated_data(classifieds,ClassifiedSerializer,request,items_per_page)
    

class UserClassifiedListView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, user_id):

        to_currency = self.request.GET.get('to_currency')
        pagination_on = self.request.GET.get('pagination_on')
        items_per_page = self.request.GET.get('items_per_page')

        try:
            user = MyUser.objects.get(pk=user_id)
        except:
            return Response({
                "status": False,
                "message": _("Invalid User")
            })

        classifieds = active_classifieds().filter(user=user).order_by("-pinned","-created_at")
        
        
        if pagination_on:
            return paginated_data(classifieds,ClassifiedSerializer,request, items_per_page)
        else:
            serializer = ClassifiedSerializer(classifieds, many=True, context={'request': request, 'user': request.user, 'to_currency': to_currency})
            return Response({
                'status': True,
                'data': serializer.data
            })
        

class UserPinnedClassifiedView(APIView):

    permission_classes = (AllowAny,)

    def get(self, request, user_id):

        to_currency = self.request.GET.get('to_currency')

        try:
            user = MyUser.objects.get(pk=user_id)
        except:
            return Response({
                "status": False,
                "message":_("Invalid User")
            })

        classified = active_classifieds().filter(user=user,pinned=True).last()
        if classified:
            serializer = ClassifiedSerializer(classified, context={'request': request, 'user': request.user, 'to_currency': to_currency})
            data = serializer.data
        else:
            data = []
        return Response({
            'status': True,
            'data': data
        })


class AddRemoveFavouriteClassifiedView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def get(self, request, classified_id):

        try:
            classified = Classified.objects.get(id = classified_id,active=True)
        except:
            return Response({
                'status': False,
                'message':_("This classified does not exist.")
            })

        if classified in request.user.favourite_classified.all():
            request.user.favourite_classified.remove(classified)
            status = "removed from"
        else:
            request.user.favourite_classified.add(classified)
            status = "added to"

        message = "Classified {} favourite classifieds".format(status)

        return Response({
            'status': True,
            'message': _(message)
        })
    

class AddClassifiedFlagView(APIView):

    permission_classes = (IsAuthenticated, IsNormalUser)

    def post(self, request):

        try:
            classified = Classified.objects.get(id = request.data["classified"],active=True)
        except:
            return Response({
                'status': False,
                'message':_("This classified does not exist.")
            })

        serializer = AddClassifiedFlagSerializer(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        
        
        try:
            already_flagged = Flagged.objects.get(classified = classified, flagged_by = request.user)
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
                'message':_("Already flagged.")
            })