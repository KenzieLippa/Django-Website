from django.urls import path
from . import views 

urlpatterns = [
    path(r'', views.VoterListView.as_view(), name='voters'),
    path(r'voter', views.VoterListView.as_view(), name='voter_list'),
    path(r'voter/<int:pk>', views.VoterDetailView.as_view(), name='voter_detail'),
    path(r'graphs', views.GraphView.as_view(), name="graphs"),
    
]