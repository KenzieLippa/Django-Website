from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns =[
    path('', kenoBase, name="kenoBase"),
    path('card/', kenoCard, name='kenoCard'),
    path('keno_game/', createKeno, name="keno_game")
]