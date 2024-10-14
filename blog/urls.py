from django.urls import path
from .views import *

urlpatterns= [
    #map the url to the view
    path('show_all', ShowAllView.as_view(), name='show_all_a'), #generic class-based view
    path(r'article/<int:pk>', ArticleView.as_view(), name='article'), #generic class-based view
    path('', RandomArticleView.as_view(), name='random'), #generic class-based view
    path(r'article/<int:pk>/create_comment', CreateCommentView.as_view(), name="create_comment"), #see our comment form
]