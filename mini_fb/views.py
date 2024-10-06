from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView

class ShowAllView(ListView):
    '''create a view to show all the portraits'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'
# Create your views here.
