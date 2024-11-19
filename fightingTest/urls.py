from django.urls import path
from .views import *


urlpatterns = [
    path('', BaseView, name='base_view'),
]