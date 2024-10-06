from django.urls import path
from .views import ShowAllView 

urlpatterns= [
    #map the url to the view
    path('', ShowAllView.as_view(), name='show_all'), #generic class-based view
]