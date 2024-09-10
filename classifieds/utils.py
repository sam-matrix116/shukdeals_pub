from .models import Classified
import datetime

def active_classifieds():
    today = datetime.datetime.now().date()
    classifieds = Classified.objects.filter(active=True,expiry_date__gt = today, is_deleted=False, user__active=True, user__is_deleted = False)
    return classifieds