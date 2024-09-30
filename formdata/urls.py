# our file with the urls lol
# define the urls for the app
from django.urls import path
from django.conf import settings
from . import views

# list of valid url patterns
urlpatterns = [
    # included into the proj level urls, everything related to thte form data url shows up here
    path(r'', views.show_form, name="show_form"),
    path(r'submit', views.submit, name="submit")

]