from rest_framework.pagination import PageNumberPagination
from collections import OrderedDict
from rest_framework.response import Response
from django.conf import settings


class FourItemsPagination(PageNumberPagination):
    page_size = 4


class SixItemsPagination(PageNumberPagination):
    page_size = 6


class EightItemsPagination(PageNumberPagination):
    page_size = 8


class SixteenItemsPagination(PageNumberPagination):
    page_size = 16


class TenItemsPagination(PageNumberPagination):
    page_size = 10


def paginated_data(queryset,serializer,request,items, extra_data=None):

    if items:
        items = int(items)

    to_currency = request.GET.get('to_currency')
    
    if items == 4:
        paginator = FourItemsPagination()
    elif items == 6:
        paginator = SixItemsPagination()
    elif items == 8:
        paginator = EightItemsPagination()
    elif items == 16:
        paginator = SixteenItemsPagination()
    else:
        paginator = TenItemsPagination()
    
    p = paginator.paginate_queryset(queryset=queryset, request=request)
    serializer = serializer(p, many=True, context={'user':request.user,'to_currency': to_currency})

    response = paginator.get_paginated_response(serializer.data)
    response.data['extra_data'] = extra_data

    return response