from django.urls import path
from .views import *


urlpatterns = [
    path('', GameView, name='game_view'),
]