from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('show_all', ShowAllView.as_view(), name='show_all'),
    path('', ShowAllView.as_view(), name="show_all"),
    path('profile/<int:pk>', ShowProfile.as_view(), name='profile'),
    path('create_profile', Create_Profile_View.as_view(), name='create_profile'),
    # path('create_status', CreateStatusMsg.as_view(), name='create_status'),
    path('profile/<int:pk>/create_status', Create_Status_View.as_view(), name = 'create_status'),
    path('profile/<int:pk>/update', UpdateProfileView.as_view(), name="update_profile"),
    path('delete_status_message/<int:pk>', DeleteStatusMessageView.as_view(), name='delete_status',),
    path('update_status_message/<int:pk>', UpdateStatusMessageView.as_view(), name="update_status"),
    path('profile/<int:pk>/add_friend/<int:other_pk>', CreateFriendView.as_view(), name='add_friend')
]