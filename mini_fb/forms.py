from django import forms
from .models import Profile, StatusMsg

class CreateProfileForm(forms.ModelForm):
    '''add a form to create a new profile'''
    class Meta:
        '''associate this with the profile form'''
        model = Profile
        fields = ['first_name', 'last_name', 'city', 'email_address', "profile_img"]

class CreateStatusMsg(forms.ModelForm):
    class Meta:
        model = StatusMsg
        fields = ['text']

class UpdateProfileForm(forms.ModelForm):
    '''add a form to update the existing profile'''
    class Meta:
        model = Profile
        fields = ['city', 'email_address', 'profile_img']

class UpdateStatusMessageForm(forms.ModelForm):
    '''add a form to update the existing profile'''
    class Meta:
        model = StatusMsg
        fields = ['text']
        