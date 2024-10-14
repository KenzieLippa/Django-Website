from django.forms import BaseModelForm
from django.http import HttpResponse
from django.shortcuts import render
from .models import Article
from django.views.generic import ListView, DetailView, CreateView
from .forms import * ##import the forms for create comment
from django.urls import reverse
from typing import Any

# import random
import random
# Create your views here.

class ShowAllView(ListView):
    '''create a subclass of list view to display all blog articles'''

    model = Article #retrieve objects of type article from db
    template_name = 'blog/show_all.html'
    context_object_name = 'articles' #how to find the data in the template files


class RandomArticleView(DetailView):
    '''where list view shows all, detail shows one, is an object of type article'''
    model = Article #model to displau
    template_name = "blog/article.html"
    context_object_name = "article"

    # attribute error: generic detail view must be called with something else

    def get_object(self):
        '''return one article chosen at random'''
        all_articles = Article.objects.all()
        article = random.choice(all_articles)
        return article

class ArticleView(DetailView):
    model = Article #model to displau
    template_name = "blog/article.html"
    context_object_name = "article"
    
class CreateCommentView(CreateView):
    '''A view to create a comment on an article'''
    '''on GET: send back the form to display'''
    '''on POST read/process the form'''
    form_class = CreateCommentForm
    template_name = "blog/create_comment_form.html"

    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        #get the context from the superclass
        context = super().get_context_data(**kwargs)

        #add article referred to by the url into this context
        article = Article.objects.get(pk=self.kwargs['pk'])
        context['article'] = article

        return context

    # what to do when we have success
    def get_success_url(self) -> str:
        '''can override the base method, return the URL to redirect on success'''
        # return super().get_success_url() #doesnt work because undefined
        # return 'show_all' #a valid url pattern
        article = Article.objects.get(pk=self.kwargs['pk'])
        return reverse('article', kwargs = {'pk':article.pk})
    

    def form_valid(self, form) -> HttpResponse:
        '''once form data is successful and and before adding to the database'''
        print(f"CreateCommentView.form_valid() form = {form}")
        print(f'CreateCommentView.grom_valid(): self.kwargs={self.kwargs}')

        article = Article.objects.get(pk=self.kwargs['pk'])
        form.instance.article = article
        return super().form_valid(form)
    # use the name instead becuase then it doesnt change later