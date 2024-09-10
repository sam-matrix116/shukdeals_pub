from rest_framework.views import APIView
from rest_framework.response import Response
from content.models import *
from content.api.serializers import *
from rest_framework.permissions import AllowAny
from django.utils.translation import gettext as _


class FaqListView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        faqs = Faq.objects.all()
        serializers = FaqSerializer(faqs, many=True)

        return Response({
            'status': True,
            'data': serializers.data
        })


class AboutUsView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        about_us = About.objects.all().first()
        serializer = AboutSerializer(about_us)
        
        
        return Response({
            'status': True,
            'data': serializer.data
        })


class TermsAndConditionsView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        termsandconditions = TermsAndCondition.objects.all().first()

        if termsandconditions:
            termsandconditions = termsandconditions.description
        
        return Response({
            'status': True,
            'terms_and_conditions': termsandconditions
        })
    

class PrivacyPolicyView(APIView):

    permission_classes = (AllowAny,)

    def get(self,request):

        privacy_policy = PrivacyPolicy.objects.all().first()

        if privacy_policy:
            privacy_policy = privacy_policy.description
        
        return Response({
            'status': True,
            'privacy_policy': privacy_policy
        })
    

class ContactUsView(APIView):

    permission_classes = (AllowAny,)

    def post(self,request):

        serializer = ContactUsSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        
        return Response({
            'status': True,
            'message': _('Thank you for the message. We will contact soon.')
        })