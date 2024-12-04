from django import forms
from .models import *


class CreateProfileForm(forms.ModelForm):
    '''add a form to create a new profile'''
    class Meta:
        '''associate this with the profile form'''
        model = Profile
        fields = ["name", "age"]

class CreateGameForm(forms.ModelForm):
    '''add a form to create a new profile'''
    class Meta:
        '''associate this with the profile form'''
        model = Game
        fields = ["player1", "player2", "player3", "player4", "player5", "season"]

       

class CreatePlayerForm(forms.ModelForm):
    '''add a form to create a new profile'''
    class Meta:
        '''associate this with the profile form'''
        model = Character
        fields = ["name", "adult", "gender"]


# class UpdateGameForm(forms.ModelForm):
#     '''add a form to update the existing profile'''
#     class Meta:
#         model = Game
#         fields = ['miles']