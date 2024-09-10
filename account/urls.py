from django.urls import path
from account.views import *

from .import views

# app_name='account'

urlpatterns = [

    # ..........admin User URL.......................
    path('', views.LoginPage, name='hello_world'),
    path('login/', views.LoginPage, name='user_login'),
    path('dashboard', DashboardView.as_view(), name='dashboard'),
    path('users', UserListView.as_view(), name='users'),
    
    path('member-accounts', MemberAccountListView.as_view(), name='member_accounts'),
    path('member-accounts-list', member_accounts_list, name='member_accounts_list'),
    path('business-accounts', BusinessAccountListView.as_view(), name='business_accounts'),
    path('ngo-accounts', NgoAccountListView.as_view(), name='ngo_accounts'),
    path('news-agencies-accounts', NewsAgencyAccountListView.as_view(), name='news_agencies_accounts'),
    
    path('cancel-user/<int:pk>', views.cancelUser, name='cancel-user'),

    path('approve-business/<int:pk>', views.approveBusinessUser, name='approve_business'),
    path('approve-ngo/<int:pk>', views.approveNgoUser, name='approve_ngo'),
    path('make-ngo-default/<int:pk>', views.makeNgoDefault, name='make_ngo_default'),
    
    
    path('user-detail/<int:pk>', UserDetailView.as_view(), name='user-details'),
    path('user-delete/<int:pk>', delete_user_modal, name='user-delete'),
    path('user-delete-confirm/<int:pk>', delete_user_confirm, name='user-delete-confirm'),
    path('logout/', views.logoutUser, name="logout"),
    path('activate-deactivate-user/<int:pk>', views.activateDeactivateUser, name='activate_deactivate_user'),
    
    path('family-members', FamilyMembersListView.as_view(), name='family_members'),
    
    path('plans', PlanListView.as_view(), name='plans'),
    path('plan/add', PlanCreateView.as_view(), name='plan_add'),
    path('plan/update/<int:pk>', PlanUpdateView.as_view(), name='plan_update'),
    path('plan/delete/<int:pk>', PlanDeleteView.as_view(), name='plan_delete'),
    path('plan/features/<int:pk>', PlanFeatureListView.as_view(), name='plan_features'),
    path('product-prices', ProductPriceListView.as_view(), name='product_prices'),
    path('product-price/update/<int:pk>', ProductPriceUpdateView.as_view(), name='product_price_update'),
    path('delivery-partners', DeliveryPartnerListView.as_view(), name='delivery_partners'),
    path('delivery-partner/add', DeliveryPartnerCreateView.as_view(), name='delivery_partner_add'),
    path('delivery-partner/update/<int:pk>', DeliveryPartnerUpdateView.as_view(), name='delivery_partner_update'),
    path('delivery-partner/delete/<int:pk>', DeliveryPartnerDeleteView.as_view(), name='delivery_partner_delete'),

    path('deals', DealListView.as_view(), name='deals'),
    path('weekly-deals', WeeklyDealListView.as_view(), name='weekly_deals'),
    path('deal-detail/<int:pk>', DealDetailView.as_view(), name='deal_details'),
    path('deal-delete/<int:pk>', deal_delete, name='deal_delete'),
    path('activate-deactivate-deal/<int:pk>', views.activateDeactivateDeal, name='activate_deactivate_deal'),


    path('classifieds', ClassifiedListView.as_view(), name='classifieds'),
    path('classified-detail/<int:pk>', ClassifiedDetailView.as_view(), name='classified_details'),
    path('classified-delete/<int:pk>', classified_delete, name='classified_delete'),
    path('activate-deactivate-classified/<int:pk>', views.activateDeactivateClassified, name='activate_deactivate_classified'),

    path('flagged-accounts', FlaggedAccountsListView.as_view(), name='flagged_accounts'),
    path('flagged-deals', FlaggedDealsListView.as_view(), name='flagged_deals'),
    path('flagged-classifieds', FlaggedClassifiedsListView.as_view(), name='flagged_classifieds'),
    path('flagged-reviews', FlaggedReviewsListView.as_view(), name='flagged_reviews'),

    path('content/faqs', FaqListView.as_view(), name='admin_faqs'),
    path('content/faq/add', FaqCreateView.as_view(), name='faq_add'),
    path('faq/update/<int:pk>', FaqUpdateView.as_view(), name='faq_update'),
    path('faq/delete/<int:pk>', FaqDeleteView.as_view(), name='faq_delete'),

    path('contact-us', ContactUsListView.as_view(), name='contact_us'),


    path('content/about-us', AboutUsListView.as_view(), name='about_us'),
    path('content/about-us/add', AboutUsCreateView.as_view(), name='about_us_add'),
    path('content/about-us/update/<int:pk>', AboutUsUpdateView.as_view(), name='about_us_update'),

    path('content/about-us-journeys', AboutUsJourneysListView.as_view(), name='about_us_journeys'),
    path('content/about-us-journey/add', AboutUsJourneyCreateView.as_view(), name='about_us_journey_add'),
    path('content/about-us-journey/update/<int:pk>', AboutUsJourneyUpdateView.as_view(), name='about_us_journey_update'),
    path('content/about-us-journey/delete/<int:pk>', AboutUsJourneyDeleteView.as_view(), name='about_us_journey_delete'),



    path('content/about-us-teams', AboutUsTeamsListView.as_view(), name='about_us_teams'),
    path('content/about-us-team/add', AboutUsTeamCreateView.as_view(), name='about_us_team_add'),
    path('content/about-us-team/update/<int:pk>', AboutUsTeamUpdateView.as_view(), name='about_us_team_update'),
    path('content/about-us-team/delete/<int:pk>', AboutUsTeamDeleteView.as_view(), name='about_us_team_delete'),


    path('content/terms-and-conditions', TermsAndConditionsListView.as_view(), name='terms_and_conditions'),
    path('content/terms-and-conditions/add', TermsAndConditionsCreateView.as_view(), name='terms_and_conditions_add'),
    path('content/terms-and-conditions/update/<int:pk>', TermsAndConditionsUpdateView.as_view(), name='terms_and_conditions_update'),

    path('content/privacy-policies', PrivacyPolicyListView.as_view(), name='privacy_policies'),
    path('content/privacy-policy/add', PrivacyPolicyCreateView.as_view(), name='privacy_policy_add'),
    path('content/privacy-policy/update/<int:pk>', PrivacyPolicyUpdateView.as_view(), name='privacy_policy_update'),


    path('news-articles', NewsListView.as_view(), name='news'),
    path('update-news-status', views.update_news_status, name='update_news_status'),
    path('update-news-deleted', views.update_news_deleted, name='update_news_deleted'),

    path('payment/all-orders', views.AllOrdersListView.as_view(), name='all_orders'),
    path('payment/order-payment-details/<int:pk>', views.OrderPaymentDetailView.as_view(), name='order_payment_details'),
    path('payment/update-exchange-rates', views.update_all_exchange_rates, name='update_all_exchange_rates'),

    path('payment/ngo-payouts', PayoutListView.as_view(), name='ngo_payout'),
    path('payment/ngo-payout-details', PayoutDetailListView.as_view(), name='ngo_payout_details'),
    path('payment-payout-mark-paid/<int:pk>', views.markPayoutPaid, name='mark_payout_paid'),

    path('payment/vendors', VendorListView.as_view(), name='vendors'),
    path('payment/vendor/add', VendorCreateView.as_view(), name='vendor_add'),
    path('payment/vendor/update/<int:pk>', VendorUpdateView.as_view(), name='vendor_update'),
    path('payment/vendor/delete/<int:pk>', VendorDeleteView.as_view(), name='vendor_delete'),

    path('payment/expenses', ExpenseListView.as_view(), name='expenses'),
    path('payment/expense/add', ExpenseCreateView.as_view(), name='expense_add'),
    path('payment/expense/update/<int:pk>', ExpenseUpdateView.as_view(), name='expense_update'),
    path('payment/expense/delete/<int:pk>', ExpenseDeleteView.as_view(), name='expense_delete'),
    path('payment/expense/mark-paid/<int:pk>', views.markExpensePaid, name='mark_expense_paid'),
    
    path('payment/revenue', RevenueListView.as_view(), name='revenue'),

    
]
