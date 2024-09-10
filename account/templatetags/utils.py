from account.models import MyUser
from django import template

register = template.Library()

@register.simple_tag
def pending_businesses_for_approval():
    pending_approvals = MyUser.objects.filter(user_type = 'business', is_approved = False, is_deleted = False)
    return pending_approvals.count()


@register.simple_tag
def pending_ngos_for_approval():
    pending_approvals = MyUser.objects.filter(user_type = 'ngo', is_approved = False, is_deleted = False)
    return pending_approvals.count()