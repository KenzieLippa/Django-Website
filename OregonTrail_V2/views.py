from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from typing import Any
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import *
from .models import *
from django.dispatch import receiver
from django.contrib.auth.signals import user_logged_in
from django.shortcuts import redirect, get_object_or_404

# # make sure the user has a profile for this part of the website
# @receiver(user_logged_in)
# def ensure_profile(sender, request, user, **kwargs):
#     if not hasattr(request.user, 'profile'):
#         return redirect(reverse('create_profile'))
    

def base(req):
    '''show the main page'''
    template_name = "OregonTrail_V2/home.html"
    profile = None
    if req.user.is_authenticated:
        profile = get_object_or_404(Profile, user=req.user)
    return render(req, template_name, {'profile': profile})


class Create_Profile_View(LoginRequiredMixin, CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm


    # TODO: mofify the form to actually reflect creating a new game instead
    template_name = 'OregonTrail_V2/create_profile_form.html'
    # user_create = UserCreationForm #not sure if this is the right place

    def get_login_url(self):
        return reverse('login-O')

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('profile-O', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        # form.instance.profile = profile
        # print(f'CreateProfileView: form.cleaned_data={form.cleaned_data}')
        # # if self.request.POST:
        # user_create = UserCreationForm(self.request.POST)
        # if not user_create.is_valid():
        #     print(f"form.errors={user_create.errors}")
        #     return super().form_invalid(form)
            
        # user = user_create.save()
        
        # # form.instance.user = user

        #     # login the user
        # print(f"Create_Profile_View user={user} profile.user={user}")
        form.instance.user = self.request.user
        # login(self.request, user)


        
        return super().form_valid(form)
    
    def dispatch(self, request, *args, **kwargs):
        if hasattr(request.user, 'profile'):
            return redirect('base')
        return super().dispatch(request, *args, **kwargs)
    # def get_context_data(self, **kwargs):
    #     # gets teh context dictionary from the base class
    #     context = super().get_context_data(**kwargs)

    #     #creates the instance of the form which can be passed through
    #     # user_create_form = self.user_create(self.request.POST) #there is no way this is gonna work lol

    #     # add user form to the context
    #     context['user_create_form'] = UserCreationForm()
    #     return context
    
class ShowProfile(DetailView):
    '''show the profile that was clicked on'''
    model = Profile
    template_name = 'OregonTrail_V2/show_profile.html'
    context_object_name = 'profile'

class Create_Game_View(LoginRequiredMixin, CreateView):

    # adding the login mixin to both this and the other
    '''a view to create a new game based on existing players'''
    form_class = CreateGameForm
    template_name = 'OregonTrail_V2/newGameForm.html'

    def get_login_url(self):
        return reverse('login-O')
    
    def dispatch(self, request, *args, **kwargs):
        if not Profile.objects.filter(user=request.user).exists():
            return redirect('create_profile')
        return super().dispatch(request, *args, **kwargs)
    # def get_object(self):
    # # get logged in user
    #     # maybe add an if pk but idk
    #     user = self.request.user

    #     #use the profile to get the profile corresponding to this user
    #     profile = Profile.objects.get_or_create(user=user)
    #     return profile

    # TODO: mofify the form to actually reflect creating a new game instead
   
    # user_create = UserCreationForm #not sure if this is the right place

    

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('base')
    # TODO make this the main game screen
    
    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        # form.instance.profile = profile
        print(f'CreateGameView: form.cleaned_data={form.cleaned_data}')
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        # profile = Profile.objects.get_or_create(user=user)
        # form.instance.profile = profile
        #save the status msg to the db
        sm = form.save()

        #read the file from the form
        # files = self.request.FILES.getlist('files')
        # for img in files:
        #     #create image object
        #     new_img = Image()
        #     new_img.image = img
        #     # hopefully this works lol
        #     new_img.status_msg = sm
        #     new_img.save()

        return super().form_valid(form)
    

class Create_Player_View(CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new player and add it to the database'''
    form_class = CreatePlayerForm


    # TODO: mofify the form to actually reflect creating a new game instead
    template_name = 'OregonTrail_V2/createPlayer.html'
    # user_create = UserCreationForm #not sure if this is the right place



    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
       
        return reverse('create_game')
    # TODO make this the main game screen

    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
       
        # user = self.request.user

        #use the profile to get the profile corresponding to this user
        # profile = Profile.objects.get(user=user)
        # form.instance.profile = profile
        #save the character to the db
        form.save()

      
       

        return super().form_valid(form)


    # TODO fix context data stuff
        # def get_context_data(self, **kwargs):
        #     # gets teh context dictionary from the base class
        #     context = super().get_context_data(**kwargs)

        #     #creates the instance of the form which can be passed through
        #     # user_create_form = self.user_create(self.request.POST) #there is no way this is gonna work lol

        #     # add user form to the context
        #     context['user_game_form'] = UserCreationForm()
        #     return context