from django import forms
from .models import *


class CreateProfileForm(forms.ModelForm):
    '''add a form to create a new profile'''
    class Meta:
        '''associate this with the profile form'''
        model = Profile
        fields = ["name", "age"]
