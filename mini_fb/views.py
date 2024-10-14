from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import CreateProfileForm

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

class Create_Profile_View(CreateView):
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile.html'

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('profile', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        # form.instance.profile = profile
        return super().form_valid(form)
    