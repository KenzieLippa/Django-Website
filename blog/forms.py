# has to be forms.py and to match
from django import forms
from .models import Comment,Article

class CreateCommentForm(forms.ModelForm):
    '''A form to add a comment on an article to the database'''

    # have to define this class
    class Meta:
        '''assosciate this html form with a comment model'''
        model = Comment #specify our model, super class reads the attributes and knows all the fields it has to create
        # dont want to fill out the date so we specify what we want the author to fill out
        fields = ['author', 'text'] #removed the articles one
        # we want the article to contain information about a url

# new form to create new stuff
class CreateArticleForm(forms.ModelForm):
    '''A form to add a new Article to the database'''

    class Meta:
        '''associate this html form with the article data model'''
        model = Article
        fields = ['author', 'title', 'text', 'image_file']