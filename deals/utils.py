from .models import Deal
import datetime
from django.conf import settings
import geopy.distance
from account.models import Location
from django.db.models import Func, F, FloatField, ExpressionWrapper, Min


class Sin(Func):
    function = 'SIN'


class Cos(Func):
    function = 'COS'


class Acos(Func):
    function = 'ACOS'


class Radians(Func):
    function = 'RADIANS'


def active_deals():
    today = datetime.datetime.now().date()
    deals = Deal.objects.filter(active=True, expiry_date__gt=today,
                                is_deleted=False, user__active=True, user__is_deleted=False)
    return deals



def nearest_deals(deals, latitude, longitude):
    radlat = Radians(float(latitude))  # given latitude
    radlong = Radians(float(longitude))  # given longitude
    radflat = Radians(F('location__latitude'))
    radflong = Radians(F('location__longitude'))

    distance_expression = ExpressionWrapper(3959.0 * Acos(Cos(radlat) * Cos(radflat) *
                                        Cos(radflong - radlong) +
                                        Sin(radlat) * Sin(radflat)), output_field=FloatField())

    deals = deals.annotate(distance=distance_expression).order_by('distance')

    return deals


def nearest_classifieds(classifieds, latitude, longitude):

    radlat = Radians(float(latitude))  # given latitude
    radlong = Radians(float(longitude))  # given longitude
    radflat = Radians(F('location__latitude'))
    radflong = Radians(F('location__longitude'))

    distance_expression = ExpressionWrapper(3959.0 * Acos(Cos(radlat) * Cos(radflat) *
                                        Cos(radflong - radlong) +
                                        Sin(radlat) * Sin(radflat)), output_field=FloatField())

    classifieds = classifieds.annotate(distance=distance_expression).order_by('distance')

    return classifieds


def nearest_users(users, latitude, longitude):

    radlat = Radians(float(latitude))  # given latitude
    radlong = Radians(float(longitude))  # given longitude
    radflat = Radians(F('user_locations__location__latitude'))
    radflong = Radians(F('user_locations__location__longitude'))

    distance_expression = ExpressionWrapper(3959.0 * Acos(Cos(radlat) * Cos(radflat) *
                                        Cos(radflong - radlong) +
                                        Sin(radlat) * Sin(radflat)), output_field=FloatField())
    
    users = users.annotate(distance=distance_expression).filter(distance__gt = 0).order_by('distance').distinct()

    return users