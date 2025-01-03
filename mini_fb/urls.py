from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

from .views import *

urlpatterns = [
    path('show_all', ShowAllView.as_view(), name='show_all'),
    path('', ShowAllView.as_view(), name="show_all"),
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('create_profile', Create_Profile_View.as_view(), name='create_profile'),
    # path('create_status', CreateStatusMsg.as_view(), name='create_status'),
    path('status/create_status', Create_Status_View.as_view(), name = 'create_status'),
    path('profile/update', UpdateProfileView.as_view(), name="update_profile"),
    path('status/<int:pk>/delete', DeleteStatusMessageView.as_view(), name='delete_status',),
    path('update_status_message/<int:pk>', UpdateStatusMessageView.as_view(), name="update_status"),
    path('profile/add_friend/<int:other_pk>', CreateFriendView.as_view(), name='add_friend'),
    path('profile/friend_suggestions', ShowFriendSuggestionsView.as_view(), name='friend_suggestion'),
    path('profile/news_feed', ShowNewsFeedView.as_view(), name="news_feed"),
    path('login/', auth_views.LoginView.as_view(template_name='mini_fb/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='mini_fb/logged_out.html'), name='logout'),
]