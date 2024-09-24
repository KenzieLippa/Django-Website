from django.urls import path
from .views import *


'''provides us the url patterns so that we can navigate the pages'''
urlpatterns = [
    # initial suggestion?
    # path("/", base_page_view),
    path('', quote_view, name="home"),
    path('quote/', quote_view, name='quote'),
    path('show_all/', show_all_view, name="show_all"),
    path('about/', about_view, name="about")
    # path('show_all/', )
]