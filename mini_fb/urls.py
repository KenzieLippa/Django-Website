from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('show_all', ShowAllView.as_view(), name='show_all'),
    path('', ShowAllView.as_view(), name="show_all"),
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('create_profile', Create_Profile_View.as_view(), name='create_profile'),
]