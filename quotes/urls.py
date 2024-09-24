from django.urls import path
from .views import *


urlpatterns = [

    # initial suggestion?
    # path("/", base_page_view),
    path('', quote_view, name="home"),
    path('quote/', quote_view, name='quote'),
    path('show_all/', show_all_view, name="show_all"),
    path('about/', about_view, name="about")
    # path('show_all/', )
]