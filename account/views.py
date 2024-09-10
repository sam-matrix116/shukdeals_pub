from django.shortcuts import render
from django.http import HttpResponse
from django.utils.translation import gettext as _
from account.utils import translate, exchange_rate, active_users, active_businesses, randomize_all_user_data, allocate_members_and_businesses_to_default_ngo
from django.views.generic import TemplateView, ListView, DetailView
from account.models import *
from account.models import Flagged as UserFlag
from deals.models import Deal, Flagged as DealFlag, Review as DealReview, DealClick, DealRedeem, DealClick
from classifieds.models import Classified, Flagged as ClassifiedFlag, ClassifiedClick
from article.models import News, STATUS_TYPES as news_status_types
from django.shortcuts import get_object_or_404, redirect, render
from account.forms import *
from content.forms import *
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.messages.views import SuccessMessageMixin
from shuktv.utils.customPermissionClass import IsSuperAdminMixin, IsAdminMixin, IsBackendUserMixin
from django.http import JsonResponse
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Q
import datetime


# Create your views here.

def LoginPage(request):
    if request.user.is_authenticated and request.user.is_admin:
        return redirect('dashboard')
    else:
        form = AdminLoginForm()

        if request.method == 'POST':

            form = AdminLoginForm(request.POST)

            if form.is_valid():
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                print(email,password)
                user = authenticate(request, username=email, password=password)
                print('user', user)
                if user is not None:
                    if user.is_admin or user.is_staff:
                        login(request, user)
                        return redirect('dashboard')
                    else:
                        messages.warning(
                        request, 'Only staff/admin can login')
                        return redirect('/account/login/')
                else:
                    messages.warning(
                        request, 'Invalid email and/or password.')
                    return redirect('/account/login/')
    context = {'form': form}
    return render(request, 'account/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('/account/login')


def index(request):
    # trans = translate(language='fr')
    # print('trans',trans)
    return render(request, 'account/hello.html')


class DashboardView(IsBackendUserMixin, TemplateView):
    
    template_name = "account/dashboard.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Dashboard"

        # dashboard data

        frontend_users = MyUser.objects.filter(is_admin=False, is_staff = False, is_deleted=False)

        toal_member_users = frontend_users.filter(user_type='member').count()
        toal_business_users = frontend_users.filter(user_type='business').count()
        toal_ngo_users = frontend_users.filter(user_type='ngo').count()
        total_news_agencies_users = frontend_users.filter(user_type='news_agency').count()
        
        context['total_member_users'] = toal_member_users
        context['total_business_users'] = toal_business_users
        context['total_ngo_users'] = toal_ngo_users
        context['total_news_agencies_users'] = total_news_agencies_users

        deals = Deal.objects.all()
        total_weekly_deals = deals.filter(weekly=True).count()
        total_normal_deals = deals.filter(weekly=False).count()
        
        context['total_weekly_deals'] = total_weekly_deals
        context['total_normal_deals'] = total_normal_deals

        classifieds = Classified.objects.all()
        total_classifieds = classifieds.count()

        context['total_classifieds'] = total_classifieds

        total_jobs = 0
        
        revenue = Revenue.objects.all().aggregate(Sum("amount"))
        total_revenue = revenue["amount__sum"]
        context['total_jobs'] = total_jobs
        context['total_revenue'] = total_revenue

        context['basic_member_users'] = MyUser.objects.filter(plan=1).count()
        context['standard_member_users'] = MyUser.objects.filter(plan=2).count()

        context['basic_business_users'] = MyUser.objects.filter(plan=3).count()
        context['standard_business_users'] = MyUser.objects.filter(plan=4).count()
        context['corporate_business_users'] = MyUser.objects.filter(plan=5).count()
        
        return context


class UserListView(IsBackendUserMixin, ListView):
    
    model = MyUser
    template_name = "account/users.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Users"
        user_types = {value:key for value,key in TYPE_OF_USERS}
        context['user_types'] = user_types
        return context
    
    def get_queryset(self):
        user_type = self.request.GET.get("user_type", None)
        paid = self.request.GET.get("paid", None)
        verified = self.request.GET.get("verified", None)
        approved = self.request.GET.get("approved", None)
        
            
        users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False)
        
        if user_type:
            users = users.filter(user_type=user_type)
        if paid == 'yes':
            paid_plans = Plan.objects.filter(amount__gt = 0)
            paid_plan_ids = [plan.id for plan in paid_plans]
            users = users.filter(plan__in = paid_plan_ids)
        if paid == 'no':
            free_plans = Plan.objects.filter(amount = 0)
            free_plan_ids = [plan.id for plan in free_plans]
            users = users.filter(Q(plan__in = free_plan_ids) | Q(plan__isnull = True))
        if verified == 'yes':
            users = users.filter(is_verified=True)
        if verified == 'no':
            users = users.filter(is_verified=False)

        if approved == 'yes':
            users = users.filter(is_approved=True)
        if approved == 'no':
            users = users.filter(is_approved=False)

        return users


def common_filter(users,self):
    paid = self.request.GET.get("paid", None)
    verified = self.request.GET.get("verified", None)
    approved = self.request.GET.get("approved", None)
    location = self.request.GET.get("location", None)
    currency = self.request.GET.get("currency", None)
    language = self.request.GET.get("language", None)
    signup_date_range = self.request.GET.get("signup_date_range", None)
    lastlogin_date_range = self.request.GET.get("lastlogin_date_range", None)
    business_category = self.request.GET.get("business_category", None)
    
    if paid == 'yes':
        paid_plans = Plan.objects.filter(amount__gt = 0)
        paid_plan_ids = [plan.id for plan in paid_plans]
        users = users.filter(plan__in = paid_plan_ids)
    if paid == 'no':
        free_plans = Plan.objects.filter(amount = 0)
        free_plan_ids = [plan.id for plan in free_plans]
        users = users.filter(Q(plan__in = free_plan_ids) | Q(plan__isnull = True))
    if verified == 'yes':
        users = users.filter(is_verified=True)
    if verified == 'no':
        users = users.filter(is_verified=False)

    if approved == 'yes':
        users = users.filter(is_approved=True)
    if approved == 'no':
        users = users.filter(is_approved=False)

    if location:

        # search by country
        users = users.filter(country__name__icontains = location)

        if not users:
            locations = Location.objects.filter(
                Q(location__icontains = location)|
                Q(address__icontains = location)|
                Q(city__icontains = location)|
                Q(state__icontains = location)|
                Q(country__icontains = location)|
                Q(zipcode__icontains = location)
            )

            user_ids = [location.user.id for location in locations if hasattr(location, "user")]
            users = users.filter(id__in = user_ids)

    

    if currency:
        users = users.filter(currency_id=currency)

    if language:
        users = users.filter(language=language)

    if signup_date_range:
        date_range = signup_date_range.split("/")
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()
        users = users.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)

    if lastlogin_date_range:
        date_range = lastlogin_date_range.split("/")
        start_date = date_range[0].strip()
        end_date = date_range[1].strip()
        users = users.filter(last_login__date__gte = start_date, last_login__date__lte = end_date)

    if business_category:
        users = users.filter(business_category_id = business_category)

    return users


class MemberAccountListView(IsBackendUserMixin, ListView):
    
    model = MyUser
    template_name = "account/member_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Member Accounts"
        context['currencies'] = Currency.objects.all()
        context['languages'] = {key:value for key,value in LANGUAGES_ALLOWED}
        return context
    
    def get_queryset(self):

        users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False, user_type = 'member', is_deleted = False)
        users = common_filter(users,self)
        return users
        
        
    
    def render_to_response(self, context, **response_kwargs):
        if self.request.GET.get("datatables"):
            draw = int(self.request.GET.get("draw", "1"))
            length = int(self.request.GET.get("length", "10"))
            start = int(self.request.GET.get("start", "0"))
            sv = self.request.GET.get("search[value]", None)
            qs = self.get_queryset().order_by("id")
            if sv:
                qs = qs.filter(
                    Q(name__icontains=sv)
                    | Q(code__icontains=sv)
                    | Q(name_en__icontains=sv)
                )
            filtered_count = qs.count()
            qs = qs[start : start + length]

            return JsonResponse(
                {
                    "recordsTotal": self.get_queryset().count(),
                    "recordsFiltered": filtered_count,
                    "draw": draw,
                    "data": list(qs.values()),
                },
                safe=False,
            )
        return super().render_to_response(context, **response_kwargs)


@login_required(login_url='user_login')
def cancelUser(request, pk):

    user = MyUser.objects.get(id = pk)
    user.is_deleted = True
    user.save()

    messages.success(request,'Member Canceled Successfully')
    return redirect('/member-accounts')


def member_accounts_list(request):
    from django.http import JsonResponse
    users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False, user_type = 'member').values()
    userserial = list(users)
    return JsonResponse(userserial, safe=False)
    
    
    response = {"data": [(user.id, user.email, user.phone, user.id,user.id) for user in users]}
    return JsonResponse(response)


class BusinessAccountListView(IsBackendUserMixin, ListView):
    
    model = MyUser
    template_name = "account/business_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Business Accounts"
        business_categories = BusinessCategory.objects.all()
        context['business_categories'] = business_categories
        context['currencies'] = Currency.objects.all()
        context['languages'] = {key:value for key,value in LANGUAGES_ALLOWED}
        return context
    
    def get_queryset(self):
        
        users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False, user_type = 'business', is_deleted = False).order_by("is_approved")
        users = common_filter(users,self)
        return users
    

class NgoAccountListView(IsBackendUserMixin, ListView):
    
    model = MyUser
    template_name = "account/ngo_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Non-Profit Organizations"
        return context
    
    def get_queryset(self):
        
        users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False, user_type = 'ngo', is_deleted = False).order_by("-is_default_ngo","is_approved")
        return users
    

class NewsAgencyAccountListView(IsBackendUserMixin, ListView):
    
    model = MyUser
    template_name = "account/newsagency_accounts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "News Agencies"
        return context
    
    def get_queryset(self):
        
        users = MyUser.objects.filter(is_superuser=False, is_admin=False, is_staff = False, user_type = 'news_agency', is_deleted = False).order_by("is_approved")
        return users
    

class UserDetailView(IsBackendUserMixin, DetailView):
    model = MyUser
    template_name = "account/user-detail.html"

    def get_context_data(self, **kwargs):
        user = kwargs['object']

        try:
            family_member = MyUser.objects.get(parent=user)
        except:
            family_member = None

        total_referral_clicks = 0
        total_business_locations = 0
        if user.user_type == 'business':
            total_referral_clicks = DealClick.objects.filter(deal__user=user).count()
            total_business_locations = UserLocation.objects.filter(user=user, is_primary=False).count()

        user_locations = UserLocation.objects.filter(user=user, is_primary=False)
        location_ids = [user_location.location_id for user_location in user_locations]
        business_locations = Location.objects.filter(id__in = location_ids)


        context = super().get_context_data(**kwargs)
        context['page_name'] = "User Details"
        context['user_deals'] = Deal.objects.filter(user=user, weekly=False)
        context['weekly_user_deals'] = Deal.objects.filter(user=user, weekly=True)
        context['user_classifieds'] = Classified.objects.filter(user=user)
        context['user_activity_logs'] = ActivityLog.objects.filter(user=user).order_by("-id")
        context['business_locations'] = business_locations
        context['ngo_businesses'] = MyUser.objects.filter(ngo=user, user_type="business")
        context['ngo_members'] = MyUser.objects.filter(ngo=user, user_type="member")
        context['family_member'] = family_member
        context['user_flags'] = UserFlag.objects.filter(user=user)
        context['total_referral_clicks'] = total_referral_clicks
        context['total_business_locations'] = total_business_locations
        context['free_account_referral_clicks'] = DealClick.objects.filter(user=user, deal__user__plan__amount = 0, deal__user__user_type='business').count()
        context['paid_account_referral_clicks'] = DealClick.objects.filter(user=user, deal__user__plan__amount__gt = 0, deal__user__user_type='business').count()
        return context


@login_required(login_url='user_login')
def delete_user_modal(request, pk):
        
    user_delete_reasons = {k: v for k, v in USER_DELETE_REASONS}
    return render(request, 'account/user-delete-modal.html', context={'pk': pk, 'delete_reasons': user_delete_reasons})


@login_required(login_url='user_login')
def delete_user_confirm(request, pk):
    try:
        user = MyUser.objects.get(pk=pk)
    except:
        return JsonResponse({
            'status': False,
            'msg': 'Invalid User'
        })
    delete_reason = request.POST.get("delete_reason")


    if user.user_type == 'ngo':

        if user.is_default_ngo:
            return JsonResponse({
                'status': False,
                'msg': 'This is the default Non Profitable Organization. Please select some another Non Profitable Organization as default before deleting this user.'
            })

        if not allocate_members_and_businesses_to_default_ngo(user):
            return JsonResponse({
                'status': False,
                'msg': 'Please select some default Non Profitable Organization before deleting this. So that we can assign the members and businesses assigned to this Non Profitable Organization to other.'
            })

    user.is_deleted = True
    user.delete_reason = delete_reason
    user.save()

    randomize_all_user_data(user)

    return JsonResponse({
        'status': True,
        'msg': 'User Deleted Successfully.'
    })


@login_required(login_url='user_login')
def activateDeactivateUser(request, pk):
    
    user = MyUser.objects.get(id = pk)
    status = 'Activated'
    if user.active:
        user.active = False
        status = 'Deactivated'
    else:
        user.active = True

    user.save()

    messages.success(request,'User {} Successfully'.format(status))

    if user.user_type == 'member':
        return redirect('/member-accounts')
    elif user.user_type == 'business':
        return redirect('/business-accounts')
    elif user.user_type == 'ngo':
        return redirect('/ngo-accounts')
    elif user.user_type == 'news_agency':
        return redirect('/news-agencies-accounts')
    


@login_required(login_url='user_login')
def approveBusinessUser(request, pk):

    user = MyUser.objects.get(id = pk)
    user.is_approved = True
    user.save()

    messages.success(request,'Business Approved Successfully')
    return redirect('/business-accounts')


@login_required(login_url='user_login')
def approveNgoUser(request, pk):

    user = MyUser.objects.get(id = pk)
    user.is_approved = True
    user.save()

    messages.success(request,'Non-Profit Organization Approved Successfully')
    return redirect('/ngo-accounts')


@login_required(login_url='user_login')
def makeNgoDefault(request, pk):

    try:
        old_default = MyUser.objects.get(is_default_ngo=True)
    except:
        old_default = None

    if old_default:
        old_default.is_default_ngo = False
        old_default.save()

    user = MyUser.objects.get(id = pk)
    user.is_default_ngo = True
    user.save()

    messages.success(request,'Default NGO changed successfully. Now, {} will be used as default Non profitable Organization.'.format(user.get_full_name()))
    return redirect('/ngo-accounts')


class FamilyMembersListView(IsBackendUserMixin, ListView):
    
    model = FamilyMember
    template_name = "account/family_members.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Family Members"
        return context

    
class PlanListView(IsBackendUserMixin, ListView):
    model = Plan
    template_name = "account/plans.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Plans"
        return context


class PlanCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = PlanForm
    model = Plan

    success_message = _('Plan created successfully')
    success_url = '/plans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Plan"
        return context


class PlanUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = PlanForm
    model = Plan

    success_message = _('Plan updated successfully')
    success_url = '/plans'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Plan"
        return context


class PlanDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = Plan
    success_message = _('Plan deleted successfully')
    success_url = '/plans'


class PlanFeatureListView(IsBackendUserMixin, DetailView):
    model = Plan
    template_name = "account/plan_features.html"

    def get_context_data(self, **kwargs):
        plan = kwargs['object']
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Plan Features"
        context['plan_features'] = PlanFeature.objects.filter(plan=plan)
        return context


class ProductPriceListView(IsBackendUserMixin, ListView):
    model = ProductPrice
    template_name = "account/product-price.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Product Price"
        return context
    

class ProductPriceUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = ProductPriceForm
    model = ProductPrice

    success_message = _('Product Price updated successfully')
    success_url = '/product-prices'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Product Price"
        return context


class DeliveryPartnerListView(IsBackendUserMixin, ListView):
    model = DeliveryPartner
    template_name = "account/delivery_partners.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Delivery Partners"
        return context


class DeliveryPartnerCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    
    form_class = DeliveryPartnerForm
    model = DeliveryPartner

    success_message = _('Delivery partner created successfully')
    success_url = '/delivery-partners'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Delivery Partner"
        return context
    
    
class DeliveryPartnerUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = DeliveryPartnerForm
    model = DeliveryPartner

    success_message = _('Delivery partner updated successfully')
    success_url = '/delivery-partners'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Delivery Partner"
        return context


class DeliveryPartnerDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = DeliveryPartner
    success_message = 'Delivery partner deleted successfully'
    success_url = '/delivery-partners'


class DealListView(IsBackendUserMixin, ListView):
    model = Deal
    template_name = "deals/deals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Deals"
        context['ngos'] = active_users().filter(user_type='ngo')
        context['businesses'] = active_businesses().filter(user_type='business')
        return context

    def get_queryset(self):

        ngo = self.request.GET.get("ngo", None)
        business = self.request.GET.get("business", None)
        
        deals = Deal.objects.filter(weekly=False, is_deleted=False)
        if ngo:
            deals = deals.filter(Q(user__ngo = ngo)|Q(user_id=ngo))
        if business:
            deals = deals.filter(user_id = business)
        return deals
    

class WeeklyDealListView(IsBackendUserMixin, ListView):
    model = Deal
    template_name = "deals/deals.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Weekly Deals"
        context['ngos'] = active_users().filter(user_type='ngo')
        context['businesses'] = active_businesses().filter(user_type='business')
        return context

    def get_queryset(self):

        ngo = self.request.GET.get("ngo", None)
        business = self.request.GET.get("business", None)
        
        deals = Deal.objects.filter(weekly = True, is_deleted=False)

        if ngo:
            deals = deals.filter(Q(user__ngo = ngo)|Q(user_id=ngo))
        if business:
            deals = deals.filter(user_id = business)

        return deals


class DealDetailView(IsBackendUserMixin, DetailView):
    model = Deal
    template_name = "deals/deal-detail.html"

    def get_context_data(self, **kwargs):
        deal = kwargs['object']
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Deal Details"
        context['deal_reviews'] = DealReview.objects.filter(deal=deal)
        context['deal_flags'] = DealFlag.objects.filter(deal=deal)
        context['deal_redeems'] = DealRedeem.objects.filter(deal=deal)
        context['deal_clicks'] = DealClick.objects.filter(deal=deal)
        context['deal_member_clicks'] = DealClick.objects.filter(deal=deal,user__user_type='member').count()
        return context
    

@login_required(login_url='user_login')
def deal_delete(request,pk):
    deal = Deal.objects.get(id = pk)
    deal.is_deleted = True
    deal.save()

    messages.success(request,'Deal Deleted Successfully')
    if deal.weekly:
        return redirect('/weekly-deals')
    else:
        return redirect('/deals')
    

@login_required(login_url='user_login')
def activateDeactivateDeal(request, pk):
    
    deal = Deal.objects.get(id = pk)
    status = 'Deactivated'
    if deal.active:
        deal.active = False
    else:
        deal.active = True
        status = 'Activated'

    deal.save()

    messages.success(request,'Deal {} Successfully'.format(status))
    return redirect('/deals')


class ClassifiedListView(IsBackendUserMixin, ListView):
    model = Classified
    template_name = "classifieds/classifieds.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Classifieds"
        context['ngos'] = active_users().filter(user_type='ngo')
        context['businesses'] = active_businesses().filter(user_type='business')
        return context
    
    def get_queryset(self):
        
        
        
        ngo = self.request.GET.get("ngo", None)
        business = self.request.GET.get("business", None)
        
        classifieds = Classified.objects.filter(is_deleted=False)

        if ngo:
            classifieds = classifieds.filter(Q(user__ngo = ngo)|Q(user_id=ngo))
        if business:
            classifieds = classifieds.filter(user_id = business)

        return classifieds
    


class ClassifiedDetailView(IsBackendUserMixin, DetailView):
    model = Classified
    template_name = "classifieds/classified-detail.html"

    def get_context_data(self, **kwargs):
        classified = kwargs['object']
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Classified Details"
        context['classified_flags'] = ClassifiedFlag.objects.filter(classified=classified)
        context['classified_clicks'] = ClassifiedClick.objects.filter(classified=classified)
        context['classified_member_clicks'] = ClassifiedClick.objects.filter(classified=classified,user__user_type='member').count()
        return context
    

@login_required(login_url='user_login')
def activateDeactivateClassified(request, pk):
    
    classified = Classified.objects.get(id = pk)
    status = 'Deactivated'
    if classified.active:
        classified.active = False
    else:
        classified.active = True

    classified.save()

    messages.success(request,'Classified {} Successfully'.format(status))
    return redirect('/classifieds')


@login_required(login_url='user_login')
def classified_delete(request,pk):
    classified = Classified.objects.get(id = pk)
    classified.is_deleted = True
    classified.save()

    messages.success(request,'Classified Deleted Successfully')
    return redirect('/classifieds')

class FaqCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = FaqForm
    model = Faq

    success_message = _('Faq created successfully')
    success_url = '/content/faqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Faq"
        return context
    

class FaqListView(IsBackendUserMixin, ListView):

    model = Faq


class ContactUsListView(IsBackendUserMixin, ListView):

    model = ContactUs


class FaqUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = FaqForm
    model = Faq

    success_message = _('Faq updated successfully')
    success_url = '/content/faqs'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Faq"
        return context


class FaqDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = Faq
    success_message = _('Faq deleted successfully')
    success_url = '/content/faqs'
    

class AboutUsListView(IsBackendUserMixin, ListView):
    model = About

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "About Us"
        return context
    

class AboutUsCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = AboutForm
    model = About

    success_message = _('About us created successfully')
    success_url = '/content/about-us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create About Us"
        return context
    

class AboutUsUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = AboutForm
    model = About

    success_message = _('About updated successfully')
    success_url = '/content/about-us'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update About Us"
        return context


class AboutUsJourneysListView(IsBackendUserMixin, ListView):
    
    model = AboutJourney

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "About Us Journeys"
        return context
 
    
class AboutUsJourneyCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = AboutJourneyForm
    model = AboutJourney

    success_message = _('About Journey created successfully')
    success_url = '/content/about-us-journeys'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Journey"
        return context
    
    
class AboutUsJourneyUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = AboutJourneyForm
    model = AboutJourney

    success_message = _('Journey updated successfully')
    success_url = '/content/about-us-journeys'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Journey"
        return context


class AboutUsJourneyDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = AboutJourney
    success_message = _('Journey deleted successfully')
    success_url = '/content/about-us-journeys'


class AboutUsTeamsListView(IsBackendUserMixin, ListView):
    
    model = AboutTeam

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "About Us Teams"
        return context
 
    
class AboutUsTeamCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = AboutTeamForm
    model = AboutTeam

    success_message = _('Team created successfully')
    success_url = '/content/about-us-teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Team"
        return context
    
    
class AboutUsTeamUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = AboutTeamForm
    model = AboutTeam

    success_message = _('Team updated successfully')
    success_url = '/content/about-us-teams'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Team"
        return context


class AboutUsTeamDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = AboutTeam
    success_message = _('Team deleted successfully')
    success_url = '/content/about-us-teams'


class TermsAndConditionsListView(IsBackendUserMixin, ListView):
    model = TermsAndCondition

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Terms and Conditions"
        return context


class TermsAndConditionsCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = TermsAndConditionForm
    model = TermsAndCondition

    success_message = _('Terms and conditions created successfully')
    success_url = '/content/terms-and-conditions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Terms and Conditions"
        return context
    

class TermsAndConditionsUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = TermsAndConditionForm
    model = TermsAndCondition

    success_message = _('Terms and conditions updated successfully')
    success_url = '/content/terms-and-conditions'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Terms and Conditions"
        return context
    

class NewsListView(IsBackendUserMixin, ListView):
    model = News

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        news_status = {c[0]:c[1] for c in news_status_types}
        context['status_options'] = news_status
        context['page_name'] = "News"
        return context


@login_required(login_url='user_login')    
def update_news_status(request):
    news_id = request.POST.get('news_id')
    new_status = request.POST.get('new_status')
    try:
        news = News.objects.get(id=news_id)
    except:
        return JsonResponse({
            'status': False,
            'msg': _('Invalid News')
        })
    news.status = new_status
    news.save()
    return JsonResponse({
        'status': True,
        'msg': _('Status Updated Successfully')
    })


@login_required(login_url='user_login')    
def update_news_deleted(request):
    news_id = request.POST.get('news_id')
    try:
        news = News.objects.get(id=news_id)
    except:
        return JsonResponse({
            'status': False,
            'msg': _('Invalid News')
        })
    
    msg = ''
    if news.deleted:
        news.deleted = False
        msg = _('News removed from deleted.')
    else:
        news.deleted = True
        msg = _('News deleted successfully')
    news.save()
    return JsonResponse({
        'status': True,
        'msg': msg
    })


class StripeListView(IsBackendUserMixin, ListView):

    model = StripeDetailNew

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Stripe Transactions"
        return context


class AllOrdersListView(IsBackendUserMixin, ListView):

    model = PaymentDetail

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "All Transactions"
        user_types = {value:key for value,key in TYPE_OF_USERS}
        context['user_types'] = user_types
        context['ngos'] = active_users().filter(user_type='ngo')
        return context
    
    def get_queryset(self):

        user_type = self.request.GET.get("user_type", None)
        item_type = self.request.GET.get("item_type", None)
        ngo = self.request.GET.get("ngo", None)
        status = self.request.GET.get("status", None)
        date_range = self.request.GET.get("date_range", None)
    
        payment_details = PaymentDetail.objects.all().exclude(status='pending')
        
        if user_type:
            payment_details = payment_details.filter(user__user_type = user_type)

        if item_type:
            payment_details = payment_details.filter(item_type = item_type)

        if ngo:
            payment_details = payment_details.filter(user__ngo = ngo)

        if status:
            payment_details = payment_details.filter(status = status)

        if date_range:
            date_range_arr = date_range.split("/")
            start_date = date_range_arr[0].strip()
            end_date = date_range_arr[1].strip()
            payment_details = payment_details.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)
        
        return payment_details


class OrderPaymentDetailView(IsBackendUserMixin, DetailView):
    model = PaymentDetail
    template_name = "account/payment-details.html"

    def get_context_data(self, **kwargs):
        payment_detail = kwargs['object']

        try:
            stripe_detail = StripeDetailNew.objects.filter(payment_detail=payment_detail).last()
        except:
            stripe_detail = None

        try:
            tranzila_detail = TranzilaDetail.objects.filter(payment_detail=payment_detail).last()
        except:
            tranzila_detail = None

        context = super().get_context_data(**kwargs)
        context['page_name'] = "Order Payment Details"
        context['stripe_detail'] = stripe_detail
        context['tranzila_detail'] = tranzila_detail
        return context


def exchange_rate_sync_db(from_curr,to_curr):
    
    resp = exchange_rate(from_curr,to_curr)

    import json
    resp = json.loads(resp)
    if resp:

        rate = resp['from'][0]['mid']
        
        import datetime
        today = datetime.datetime.now().date()
        from_curr = Currency.objects.get(iso_code = from_curr)
        to_curr = Currency.objects.get(iso_code = to_curr)

        try:
            rate_already_exists = CurrencyExchangeRate.objects.get(from_currency = from_curr, to_currency = to_curr)
        except:
            rate_already_exists = None
            
        if rate_already_exists:
            rate_already_exists.exchange_rate = rate
            rate_already_exists.rate_date = today
            rate_already_exists.save()
        else:
            CurrencyExchangeRate.objects.create(
                from_currency = from_curr,
                to_currency = to_curr,
                exchange_rate = rate,
                rate_date = today
            )


def update_all_exchange_rates(request):
    all_currencies = [key for key,value in CURRENCIES_ALLOWED]
    total = len(all_currencies)
    for i in range(0,total):
        for j in range(0,total):
            if all_currencies[i] != all_currencies[j]:
                from_curr = all_currencies[i]
                to_curr = all_currencies[j]
                exchange_rate_sync_db(from_curr,to_curr)
                

    # exchange_rate_sync_db('usd','eur')
    
    return HttpResponse("Exchange rates updated")


class FlaggedAccountsListView(IsBackendUserMixin, ListView):

    model = UserFlag


class FlaggedDealsListView(IsBackendUserMixin, ListView):

    model = DealFlag

class FlaggedClassifiedsListView(IsBackendUserMixin, ListView):

    model = ClassifiedFlag


class FlaggedReviewsListView(IsBackendUserMixin, ListView):

    model = ReviewFlag




class PrivacyPolicyListView(IsBackendUserMixin, ListView):
    model = PrivacyPolicy

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Privacy Policies"
        return context


class PrivacyPolicyCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    form_class = PrivacyPolicyForm
    model = PrivacyPolicy

    success_message = _('Privacy policy created successfully')
    success_url = '/content/privacy-policies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Privacy Policy"
        return context
    

class PrivacyPolicyUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = PrivacyPolicyForm
    model = PrivacyPolicy

    success_message = _('Privacy Policy updated successfully')
    success_url = '/content/privacy-policies'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Privacy Policy"
        return context
    


class PayoutListView(IsBackendUserMixin, ListView):
    model = NGOPayout
    template_name = "account/ngo_payouts.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Non-Profit Organizations Payouts"
        return context
    
    def get_queryset(self):
        
        payouts = NGOPayout.objects.values("ngo").distinct()
        print(payouts)
        ngos_with_payouts = [payout['ngo'] for payout in payouts]
        ngos = MyUser.objects.filter(id__in=ngos_with_payouts)
        return ngos
    

class PayoutDetailListView(IsBackendUserMixin, ListView):
    model = NGOPayout
    template_name = "account/ngo_payout_details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Non-Profit Organizations Payout Details"
        return context
    
    def get_queryset(self):
        ngo = self.request.GET.get("ngo", None)
        payouts = NGOPayout.objects.filter(ngo = ngo)
        return payouts


@login_required(login_url='user_login')
def markPayoutPaid(request, pk):

    payout = NGOPayout.objects.filter(ngo_id = pk, payout=False)
    payout.update(payout = True,payout_date = datetime.datetime.now())
    
    messages.success(request,'All Payouts for the Non-Profit Organizations are marked paid successfully')
    return redirect('/payment/ngo-payouts')
    



class VendorListView(IsBackendUserMixin, ListView):
    model = Vendor
    template_name = "account/vendors.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Vendors"
        return context


class VendorCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    
    form_class = VendorForm
    model = Vendor

    success_message = _('Vendor created successfully')
    success_url = '/payment/vendors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Vendor"
        return context


class VendorUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = VendorForm
    model = Vendor

    success_message = _('Vendor updated successfully')
    success_url = '/payment/vendors'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Vendor"
        return context


class VendorDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = Vendor
    success_message = _('Vendor deleted successfully')
    success_url = '/payment/vendors'


class ExpenseListView(IsBackendUserMixin, ListView):
    model = VendorExpense
    template_name = "account/expenses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Expenses"
        return context


class ExpenseCreateView(IsBackendUserMixin,SuccessMessageMixin, CreateView):
    
    form_class = ExpenseForm
    model = VendorExpense

    success_message = _('Expense created successfully')
    success_url = '/payment/expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Create Expense"
        return context
    
    
class ExpenseUpdateView(IsBackendUserMixin,SuccessMessageMixin, UpdateView):
    
    form_class = ExpenseForm
    model = VendorExpense

    success_message = _('Expense updated successfully')
    success_url = '/payment/expenses'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Update Expense"
        return context


class ExpenseDeleteView(IsBackendUserMixin,SuccessMessageMixin, DeleteView):
    
    model = VendorExpense
    success_message = _('Expense deleted successfully')
    success_url = '/payment/expenses'


@login_required(login_url='user_login')
def markExpensePaid(request, pk):

    expense = VendorExpense.objects.get(id = pk)
    expense.paid = True
    expense.save()

    messages.success(request,'Expense marked paid successfully')
    return redirect('/payment/expenses')


class RevenueListView(IsBackendUserMixin, ListView):

    model = Revenue

    def get_context_data(self, **kwargs):
        created_at_date_range = self.request.GET.get("created_at_date_range", None)
        revenue = Revenue.objects.filter()
        
        if created_at_date_range:
            date_range_arr = created_at_date_range.split("/")
            start_date = date_range_arr[0].strip()
            end_date = date_range_arr[1].strip()
            revenue = revenue.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)

        revenue = revenue.aggregate(Sum("amount"))
        context = super().get_context_data(**kwargs)
        context['page_name'] = "Revenue"
        context['total_revenue'] = revenue["amount__sum"] if revenue["amount__sum"] else 0
        return context
    
    def get_queryset(self):

        created_at_date_range = self.request.GET.get("created_at_date_range", None)
        revenue = Revenue.objects.filter()
        
        if created_at_date_range:
            date_range_arr = created_at_date_range.split("/")
            start_date = date_range_arr[0].strip()
            end_date = date_range_arr[1].strip()
            revenue = revenue.filter(created_at__date__gte = start_date, created_at__date__lte = end_date)
        
        return revenue
