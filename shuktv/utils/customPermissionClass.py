from rest_framework import permissions
from django.contrib.auth.mixins import AccessMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404, redirect, render
from django.utils.translation import gettext as _


class NotDjangoAdmin(permissions.BasePermission):

    def has_permission(self, request, view):
        if  request.user.is_anonymous and request.user.is_admin:
            return False
        return True
    
class IsNGO(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'ngo':
            return True
        return False
    
class IsBusinessUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'business':
            return True
        return False
    
class IsDealAllowedUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 'business' or request.user.user_type == 'ngo':
            return True
        return False


class IsPlanActivated(permissions.BasePermission):

    message = _("Please activate your plan to access this module")

    def has_permission(self, request, view):
        if request.user.user_type == 'ngo' and request.user.plan:
            return True
        if request.user.user_type == 'business' and request.user.plan:
            return True
        return False
    

class IsNormalUser(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.is_verified == True and request.user.is_admin == False and request.user.is_superuser == False and request.user.is_staff == False and request.user.is_superuser == False:
            return True
        return False

    
class IsRealEstateBusinessCategory(permissions.BasePermission):

    def has_permission(self, request, view):
        if request.user.business_category.keyword == 'real_estate':
            return True
        return False
    

class IsSuperAdminMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated and request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied('Permission denied')


class IsAdminMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated and request.user.is_admin:
            return super().dispatch(request, *args, **kwargs)
        raise PermissionDenied('Permission denied')


class IsBackendUserMixin(AccessMixin):

    def dispatch(self, request, *args, **kwargs):

        if request.user.is_authenticated and (request.user.is_admin or request.user.is_superuser or request.user.is_staff):
            return super().dispatch(request, *args, **kwargs)
        
        return redirect('user_login')