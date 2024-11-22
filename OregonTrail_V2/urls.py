from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

urlpatterns =[
    path('', base, name="base"),
    path('login/', auth_views.LoginView.as_view(template_name='OregonTrail_V2/login.html'), name='login-O'),
    path('logout/', auth_views.LogoutView.as_view(template_name='OregonTrail_V2/logged_out.html'), name='logout-O'),
]