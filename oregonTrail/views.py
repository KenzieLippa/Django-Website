from django.shortcuts import render
from django.views.generic import ListView, DetailView, View

# Create your views here.

# start with base game view
def GameView(req):
    # model = Profile
    template_name = 'oregonTrail/oregon.html'
    # is_running = False
    # context = {
    #     'is_running': False,
        
    # }
    return render(req, template_name)




### EXPERIMENT
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import GameState

@csrf_exempt
# no tokens needed

def toggle_game_state(req):
    '''a method to test whether or not we can stop and start running from here
    this will determine if we are able to manage from the backend or not'''

    # start with the post
    if req.method == "POST":
        # retrieve the state from db or create if not there
        state,created = GameState.objects.get_or_create(id=1)

        #toggle the is running
        state.is_running = not state.is_running
        # save new value to the database
        state.save()

        return JsonResponse({'is_running': state.is_running})

    elif req.method == "GET":
        # return the current game state so we know it
        state,created = GameState.objects.get_or_create(id=1)
        return JsonResponse({'is_running': state.is_running})
    

