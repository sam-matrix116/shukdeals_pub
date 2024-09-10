from django import forms
from content.models import *

class FaqForm(forms.ModelForm):

    class Meta:

        model = Faq
        fields = ('question','answer')

        widgets = {
            'question': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Question"}),
            'answer': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Answer"})
        }


class AboutForm(forms.ModelForm):

    class Meta:

        model = About
        fields = '__all__'

        widgets = {
            'heading': forms.TextInput(attrs={"class":"form-control", 'placeholder': "About Us Heading"}),
            'description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter About Us", 'id': "editor"}),
            'sub_heading': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Sub Heading"}),
            'sub_description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Sub Description"}),
            'team_heading': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Team Heading"}),
            'team_description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Team Description"}),
        }


class AboutJourneyForm(forms.ModelForm):

    class Meta:

        model = AboutJourney
        fields = '__all__'

        widgets = {
            'counter': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Counter"}),
            'title': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Title"}),
            'description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Description"}),
        }


class AboutTeamForm(forms.ModelForm):

    class Meta:

        model = AboutTeam
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Name"}),
            'designation': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Designation"}),
            'facebook_link': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Facebook Link"}),
            'twitter_link': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Twitter Link"}),
            'instagram_link': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Instagram Link"}),
            'linkedin_link': forms.TextInput(attrs={"class":"form-control", 'placeholder': "Enter Linkedin Link"}),
        }

class TermsAndConditionForm(forms.ModelForm):

    class Meta:

        model = TermsAndCondition
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Terms and Conditions", 'id': "editor"})
        }


class PrivacyPolicyForm(forms.ModelForm):

    class Meta:

        model = PrivacyPolicy
        fields = ('description',)

        widgets = {
            'description': forms.Textarea(attrs={"class":"form-control", 'placeholder': "Enter Privacy Policy", 'id': "editor"})
        }