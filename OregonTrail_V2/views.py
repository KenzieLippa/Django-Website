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
    boo = None
    if req.user.is_authenticated:
        profile = get_object_or_404(Profile, user=req.user)
        boo =req.session['profile_pk'] = profile.pk
    return render(req, template_name, {'profile': profile, 'profile_pk':boo})

class Create_Full_Profile_View(CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm
    template_name = 'OregonTrail_V2/createFullProfile.html'
    # user_create = UserCreationForm #not sure if this is the right place

    

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('profile-O', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        # form.instance.profile = profile
        print(f'CreateProfileView: form.cleaned_data={form.cleaned_data}')
        # if self.request.POST:
        user_create = UserCreationForm(self.request.POST)
        if not user_create.is_valid():
            print(f"form.errors={user_create.errors}")
            return super().form_invalid(form)
            
        user = user_create.save()
        
        # form.instance.user = user

            # login the user
        print(f"Create_Profile_View user={user} profile.user={user}")
        form.instance.user = user
        login(self.request, user)


        
        return super().form_valid(form)
    

    def get_context_data(self, **kwargs):
        # gets teh context dictionary from the base class
        context = super().get_context_data(**kwargs)

        #creates the instance of the form which can be passed through
        # user_create_form = self.user_create(self.request.POST) #there is no way this is gonna work lol

        # add user form to the context
        context['user_create_form'] = UserCreationForm()
        return context
    
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
        game = form.save(commit = False)
        party = ['player1', 'player2', 'player3', 'player4', 'player5']
        for playerg in party:
            player = getattr(game, playerg)
            print(player)
            # playerx = Character.objects.get(pk=player)
            if player:
                print(player.name)
                player.reset()
            
        game.save()

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
        # dont commit yet we have to reset the players
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
    '''the place where the post request from the save js comes'''
    if req.method == "POST":

        try:
            data = json.loads(req.body)
            miles = data.get("miles")
            p1_dead = data.get("p1_dead")
            # print(p1_dead)
            p2_dead = data.get("p2_dead")
            # print(p2_dead)
            p3_dead = data.get("p3_dead")
            # print(p3_dead)
            p4_dead = data.get("p4_dead")
            # print(p4_dead)
            p5_dead = data.get("p5_dead")
            day = data.get("days")
            # print(p5_dead)

            # get the game
            # print(miles) #program is able to get the miles
            game = Game.objects.get(pk = game_id)
            # print(game.pk)
            game.miles = int(miles)
            game.player1.dead = p1_dead
            # print(game.player1.dead)
            # set the stats with the data sent back
            game.player2.dead = p2_dead
            game.player3.dead = p3_dead
            game.player4.dead = p4_dead
            game.player5.dead = p5_dead

            game.days = day
            game.save()
            game.player1.save()
            game.player2.save()
            game.player3.save()
            game.player4.save()
            game.player5.save()
            # print(f"after update:{game.miles}")
            gameR = Game.objects.get(pk=game_id)
            # print(f"but really its: {gameR.miles}")
            # print(gameR.player1.dead)
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


class LeaderboardView(ListView):
    '''view to display the leaderboards'''
    template_name='OregonTrail_V2/leaderboard.html'
    model = Game
    context_object_name = 'res'
    paginate_by = 50
    def get_queryset(self):
        '''get the query set and search if queries '''
        qs = super().get_queryset().order_by('-miles')
        if 'player1Name' in self.request.GET:
            print("found")
            player1Name = self.request.GET['player1Name'].strip()
            if player1Name:
                print(player1Name)
                qs = qs.filter(player1__name=player1Name)
                print(len(qs))
         
       
        if 'high-day' in self.request.GET:
            day = self.request.GET['high-day']
            if day:
                print(day) #not sure what this prints
                qs = qs.order_by('-days')

        if 'high-mile' in self.request.GET:
            mile = self.request.GET['high-mile']
            if mile:
                print(mile) #not sure what this prints
                qs = qs.order_by('-miles')

    
        return qs
       
       
    
    def get_context_data(self, **kwargs):
        '''need to get the profile pk because its not redirecting properly'''
        context = super().get_context_data(**kwargs)
        profile_pk = self.request.session.get('profile_pk')
        context['session_profile_pk'] = profile_pk
        return context
    