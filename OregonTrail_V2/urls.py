from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns =[
    path('', base, name="base"),
    path('login/', auth_views.LoginView.as_view(template_name='OregonTrail_V2/login.html'), name='login-O'),
    path('logout/', auth_views.LogoutView.as_view(template_name='OregonTrail_V2/logged_out.html'), name='logout-O'),
    path('create_profile', Create_Profile_View.as_view(), name='create_profile-O'),
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile-O'),
    path('create_game', Create_Game_View.as_view(), name='create_game'),
    path('create_player', Create_Player_View.as_view(), name='create_player'),
    path('game/<int:pk>/delete', DeleteGameView.as_view(), name='delete_game',),
    path('game/<int:pk>', GameDetailView.as_view(), name="play_game"),
    path('update_game/<int:game_id>/', update_game, name='update_game'),
    path('leaderboard/', LeaderboardView.as_view(), name='leaderboard'),
    path('create_full_profile/', Create_Full_Profile_View.as_view(), name='create_full_profile')
]