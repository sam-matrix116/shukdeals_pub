from rest_framework import serializers
from content.models import *

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = '__all__'


class AboutJourneySerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutJourney
        fields = '__all__'


class AboutTeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = AboutTeam
        fields = '__all__'


class AboutSerializer(serializers.ModelSerializer):

    journeys = serializers.SerializerMethodField()
    teams = serializers.SerializerMethodField()

    class Meta:
        model = About
        fields = '__all__'

    def get_journeys(self, about):

        journeys = AboutJourney.objects.all()
        serializer = AboutJourneySerializer(journeys, many=True)
        return serializer.data
    
    def get_teams(self, about):

        teams = AboutTeam.objects.all()
        serializer = AboutTeamSerializer(teams, many=True)
        return serializer.data
    

class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = '__all__'