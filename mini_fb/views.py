from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.views.generic import ListView, DetailView, View
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreateProfileForm, CreateStatusMsg, UpdateProfileForm, UpdateStatusMessageForm
from typing import Any

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

class ShowProfile(DetailView):
    '''show the profile that was clicked on'''
    model = Profile
    template_name = 'mini_fb/show_profile.html'
    context_object_name = 'profile'

class Create_Profile_View(LoginRequiredMixin, CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm
    template_name = 'mini_fb/create_profile_form.html'

    def get_login_url(self):
        return reverse('login')
    

    def get_success_url(self) -> str:
        '''redirect the url after successfully submitting form'''
        return reverse('profile', kwargs={'pk': self.object.pk})
    
    def form_valid(self, form):
        '''handle the form submission and get the foreign key?'''
        # profile = Profile.objects.get(pk=self.kwargs['pk'])
        # form.instance.profile = profile
        print(f'CreateProfileView: form.cleaned_data={form.cleaned_data}')

        # find logged in user
        user = self.request.user
        print(f"Create_Profile_View user={user} profile.user={user}")

        # attach user to form instance article object
        form.instance.user = user

        return super().form_valid(form)
    
class Create_Status_View(LoginRequiredMixin, CreateView):
    # do the login mixins here too for now
    '''a view to create a new status and save it to the database'''
    form_class = CreateStatusMsg
    template_name = "mini_fb/create_status_form.html"

    def get_login_url(self):
        return reverse('login')
    

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
        return reverse('profile', kwargs={'pk': self.kwargs['pk']})
    

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
class CreateFriendView(View):
    '''view for friends, plan is to intercept the parameters in the url and
    then steal them to create the friend'''

    # override dispatch
    def dispatch(self, request, *args, **kwargs):
        #retrieve profile and friend id from url
        profile_id = self.kwargs.get('pk')

        friend_id = self.kwargs.get('other_pk')
        # print(f'{profile_id}  {friend_id}')
        #retrieve profile
        # profile = get_object_or_404(Profile, pk=profile_id)
        # friend = get_object_or_404(Profile, pk=friend_id)
        profile = Profile.objects.filter(pk=profile_id).first()
        friend = Profile.objects.filter(pk=friend_id).first()
        print("CALLED")
        if not profile or not friend:
            print("no")
        # print(f'{profile.first_name}  {friend}')
        profile.add_friend(friend)

        return redirect('profile', pk=profile_id)
        # return super().dispatch(request, *args, **kwargs)
    #read url parameters


    #add friend
class ShowNewsFeedView(DetailView):
    '''a view for our wonderous feed'''
    template_name = "mini_fb/news_feed.html"
    model = Profile
    # context_object_name = 'status_msg'

    # def get_queryset(self):
    #     profile = Profile.objects.get(pk=self.kwargs['pk'])
    #     return profile.get_news_feed()

