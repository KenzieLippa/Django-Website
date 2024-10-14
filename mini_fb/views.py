from django.shortcuts import render
from .models import Profile
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse

from .forms import CreateProfileForm, CreateStatusMsg
from typing import Any

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
    
class Create_Status_View(CreateView):
    '''a view to create a new status and save it to the database'''
    form_class = CreateStatusMsg
    template_name = "mini_fb/create_status.html"
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''build the dict of context data for this view'''
        context = super().get_context_data(**kwargs)

        #find pk from url
        pk = self.kwargs['pk']

        # find corresponding profile
        profile = Profile.objects.get(pk=pk)

        #add profile to context data
        context['profile'] = profile
        return context
    def form_valid(self, form):
        '''handle the form submission and set a foreign key by attaching the profile to the status, can find the profile pk in url'''
        profile = Profile.objects.get(pk=self.kwargs['pk'])
        form.instance.profile = profile
        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        '''return a url to redirect to after successfully submitting form'''
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})
    