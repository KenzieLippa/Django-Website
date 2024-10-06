from django.shortcuts import render
from .models import Article
from django.views.generic import ListView
# Create your views here.

class ShowAllView(ListView):
    '''create a subclass of list view to display all blog articles'''

    model = Article #retrieve objects of type article from db
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #how to find the data in the template files

    

