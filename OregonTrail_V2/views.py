from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from typing import Any
from django.contrib.auth import login
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .forms import CreateProfileForm
def base(req):
    '''show the main page'''
    template_name = "OregonTrail_V2/home.html"
    return render(req, template_name)


class Create_Game_View(CreateView):
    # adding the login mixin to both this and the other
    '''a view to create a new profile and save to the database'''
    form_class = CreateProfileForm


    # TODO: mofify the form to actually reflect creating a new game instead
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
    
