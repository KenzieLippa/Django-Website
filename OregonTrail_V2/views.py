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
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
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
    model = Game
    template_name = 'OregonTrail_V2/newGameForm.html'

    def get_login_url(self):
        return reverse('login-O')
    
    
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        '''build the dict of context data for this view'''
        context = super().get_context_data(**kwargs)

        #find pk from url
        # pk = self.kwargs['pk']

        # find corresponding profile
        # profile = Profile.objects.get(pk=pk)
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)

        #add profile to context data
        context['profile'] = profile
        return context
    
    def form_valid(self, form):
        '''handle the form submission and set a foreign key by attaching the profile to the status, can find the profile pk in url'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        form.instance.profile = profile
        #save the status msg to the db
        form.save()

        #read the file from the form
        

        return super().form_valid(form)
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
        '''return a url to redirect to after successfully submitting form'''
        user = self.request.user
        profile = Profile.objects.get(user=user)
        print(profile.pk)
        return reverse('profile-O', kwargs={'pk':profile.pk})
    
    # TODO make this the main game screen
    
    

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

class DeleteGameView(LoginRequiredMixin, DeleteView):
    '''a view to delete our status messages'''
    template_name = "OregonTrail_V2/delete_game.html"
    model = Game
    context_object_name = 'game'

    def get_login_url(self):
        return reverse('login')

    def get_success_url(self):
        '''return the url to redirect to when we've completed'''

        #get the pk
        pk= self.kwargs.get('pk')
        game = Game.objects.filter(pk=pk).first()

        #find the profile
        profile = game.profile

        return reverse('profile-O', kwargs={'pk':profile.pk})
    

class GameDetailView(DetailView):
    '''a view to populate the fields for the game, hopefully everything will work smoothly'''

    model = Game
    template_name = "OregonTrail_V2/game.html"
    context_object_name = 'game'

# 
# @csrf_exempt
def update_game(req, game_id):
    if req.method == "POST":

        try:
            data = json.loads(req.body)
            miles = data.get("miles")
            print(miles) #program is able to get the miles
            game = Game.objects.get(pk = game_id)
            # print(game.pk)
            game.miles = int(miles)
            game.save()
            print(f"after update:{game.miles}")
            gameR = Game.objects.get(pk=game_id)
            print(f"but really its: {gameR.miles}")
            return JsonResponse({"success": True}, status=200)
        except Game.DoesNotExist:
            return JsonResponse({"success":False, "error":"Game not found"})
        except Exception as e:
            return JsonResponse({"success": False, "error": str(e)})
    return JsonResponse({"success": False, "error": "Invalid Response"}) 


# class UpdateStatusMessageView(UpdateView):
#     '''update our game with information when we hit the save button, this way we can keep track of our stats'''
#     form_class = UpdateGameForm
#     template_name = "mini_fb/update_status_form.html" # TODO fix this to go to our main form
#     model = Game
#     context_object_name = "status_msg"

#     def form_valid(self, form):
#         return super().form_valid(form)
    
    
#     def get_success_url(self):
#         '''return the url to redirect to when we've completed'''

#         #get the pk
#         pk= self.kwargs.get('pk')
#         game = Game.objects.filter(pk=pk).first()

#         #find the profile
#         profile = game.profile

#         return reverse('profile', kwargs={'pk':profile.pk})