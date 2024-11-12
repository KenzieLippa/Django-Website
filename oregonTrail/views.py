from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

# Create your views here.

# start with base game view
def GameView(req):
    # model = Profile
    template_name = 'oregonTrail/oregon.html'
    return render(req, template_name)

    

