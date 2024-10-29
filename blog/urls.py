from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
#gives generic views for the stuff we want

urlpatterns= [
    #map the url to the view
    path('show_all', ShowAllView.as_view(), name='show_all_a'), #generic class-based view
    path(r'article/<int:pk>', ArticleView.as_view(), name='article'), #generic class-based view
    path('', RandomArticleView.as_view(), name='random'), #generic class-based view
    path(r'article/<int:pk>/create_comment', CreateCommentView.as_view(), name="create_comment"), #see our comment form
    path(r'create_article', CreateArticleView.as_view(), name='create_article'),
    
    #authentication urls
    # create directly within the blog app, gives flexibility
    # specify the template in the as_view
    # need to tell it where to go after the fact
    path('login/', auth_views.LoginView.as_view(template_name = 'blog/login.html'), name="login"),
    path('logout/', auth_views.LogoutView.as_view(next_page = 'show_all_a'), name="logout"),

]