from django.urls import path
from .views import *


urlpatterns = [
    path('', GameView, name='game_view'),
    path('toggle_game_state/', toggle_game_state, name="toggle_game_state"),
]