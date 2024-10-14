from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView

class ShowAllView(ListView):
    '''create a view to show all the portraits'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'
# Create your views here.

class ShowProfile(DetailView):
    '''show the profile that was clicked on'''
    model = Profile
    template_name = 'mini_fb/profile.html'
    context_object_name = 'profile'
