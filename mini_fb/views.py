from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateProfileForm, CreateStatusMsg, UpdateProfileForm, UpdateStatusMessageForm
from typing import Any
from django.contrib.auth import login


class ShowAllView(ListView):
    '''create a view to show all the portraits'''
    model = Profile
    template_name = 'mini_fb/show_all_profiles.html'
    context_object_name = 'profiles'

    # add a dispatch method maybe like from class
    def dispatch(self, req):
        '''add to show the logged in user and to debug it'''
        print(f"Logged in user: req.user={req.user}")
        print(f"Logged in user: req.user.is_authenticated={req.user.is_authenticated}")
        return super().dispatch(req)
# Create your views here.

class ShowProfile(LoginRequiredMixin, DetailView):
    '''show the profile that was clicked on'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

    def get_login_url(self):
        return reverse('login')
    
    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)

        #set the profile pk in the session
        self.request.session['profile_pk'] = self.object.pk

        return context
    

class Create_Profile_View(CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'
    # user_create = UserCreationForm #not sure if this is the right place

    

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('profile', kwargs={'pk': self.object.pk})
    
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
    
class Create_Status_View(LoginRequiredMixin, CreateView):
    # do the login mixins here too for now
    '''a view to create a new status and save it to the database'''
    form_class = CreateStatusMsg
    template_name = "mini_fb/create_status_form.html"

    def get_login_url(self):
        return reverse('login')
    
    def get_object(self):
    # get logged in user
        # maybe add an if pk but idk
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        return profile
    
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
        sm = form.save()

        #read the file from the form
        files = self.request.FILES.getlist('files')
        for img in files:
            #create image object
            new_img = Image()
            new_img.image = img
            # hopefully this works lol
            new_img.status_msg = sm
            new_img.save()

        return super().form_valid(form)
    
    def get_success_url(self) -> str:
        '''return a url to redirect to after successfully submitting form'''
        profile = self.get_object()
        print(profile.pk)
        return reverse('profile', kwargs={'pk':profile.pk})
    

class UpdateProfileView(LoginRequiredMixin, UpdateView):
    '''a view for updating our profiles, we also wanna make sure we have a form valid or something'''
    form_class = UpdateProfileForm
    template_name = "mini_fb/update_profile_form.html"
    #mayve need this too?
    model = Profile

    def get_login_url(self):
        return reverse('login')

    #hasnt been finding our return url
    def form_valid(self, form):
        return super().form_valid(form)
    
    def get_object(self):
    # get logged in user
        # maybe add an if pk but idk
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        return profile
    
class UpdateStatusMessageView(UpdateView):
    '''update the status message the same way as before
    might also have to add something for the images here'''
    form_class = UpdateStatusMessageForm
    template_name = "mini_fb/update_status_form.html"
    model = StatusMsg
    context_object_name = "status_msg"

    def form_valid(self, form):
        return super().form_valid(form)
    
    
    def get_success_url(self):
        '''return the url to redirect to when we've completed'''

        #get the pk
        pk= self.kwargs.get('pk')
        status = StatusMsg.objects.filter(pk=pk).first()

        #find the profile
        profile = status.profile

        return reverse('profile', kwargs={'pk':profile.pk})

class DeleteStatusMessageView(LoginRequiredMixin, DeleteView):
    '''a view to delete our status messages'''
    template_name = "mini_fb/delete_status_form.html"
    model = StatusMsg
    context_object_name = 'status_msg'

    def get_login_url(self):
        return reverse('login')

    def get_success_url(self):
        '''return the url to redirect to when we've completed'''

        #get the pk
        pk= self.kwargs.get('pk')
        status = StatusMsg.objects.filter(pk=pk).first()

        #find the profile
        profile = status.profile

        return reverse('profile', kwargs={'pk':profile.pk})

class ShowFriendSuggestionsView(DetailView):
    template_name = "mini_fb/friend_suggestions.html"
    model = Profile

    
    def get_success_url(self):
        pk = self.kwargs.get('pk')
        return reverse('profile',kwargs={'pk':pk})
    
    def get_object(self):
    # get logged in user
        # maybe add an if pk but idk
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        return profile
class CreateFriendView(View):
    '''view for friends, plan is to intercept the parameters in the url and
    then steal them to create the friend'''

    def get_object(self):
    # get logged in user
        # maybe add an if pk but idk
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        return profile
    
    # override dispatch
    def dispatch(self, request, *args, **kwargs):
        #retrieve profile and friend id from url
        # profile_id = self.kwargs.get('pk')
        user = self.request.user
        profile = Profile.objects.get(user=user)

        friend_id = self.kwargs.get('other_pk')
        # print(f'{profile_id}  {friend_id}')
        #retrieve profile
        # profile = get_object_or_404(Profile, pk=profile_id)
        # friend = get_object_or_404(Profile, pk=friend_id)
        # profile = Profile.objects.filter(user=profile_id).first()
        friend = Profile.objects.filter(pk=friend_id).first()
        print("CALLED")
        if not profile or not friend:
            print("no")
        # print(f'{profile.first_name}  {friend}')
        profile.add_friend(friend)

        return redirect('profile', profile.pk)
        # return super().dispatch(request, *args, **kwargs)
    #read url parameters


    #add friend
class ShowNewsFeedView(LoginRequiredMixin, DetailView):
    '''a view for our wonderous feed'''
    template_name = "mini_fb/news_feed.html"
    model = Profile

    def get_login_url(self):
        return reverse('login')
    # context_object_name = 'status_msg'
    def get_object(self):
    # get logged in user
        # maybe add an if pk but idk
        user = self.request.user

        #use the profile to get the profile corresponding to this user
        profile = Profile.objects.get(user=user)
        return profile
    
    # def get_queryset(self):
    #     profile = Profile.objects.get(pk=self.kwargs['pk'])
    #     return profile.get_news_feed()

