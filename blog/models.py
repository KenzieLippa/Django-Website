from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
#need django user account



# Create your models here.

# here is where we create the models ig
# this is from the class assignment
class Article(models.Model):
    '''encapsulate the idea of an article by some author'''
    #data attributse of an article
    #every article has one user:
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    # file type that is not text
    image_file = models.ImageField(blank=True) #makes it optional
    # when changing have to make migrations and migreate
# assosciate existing ones in minifb with admin

    def __str__(self):
        '''return a string rep of this article object'''
        return f'{self.title} by {self.author}' 
    
    def get_comments(self):
        '''Return all of the comments about this article.'''
        comments = Comment.objects.filter(article=self)
        return comments
    
    def get_absolute_url(self):
        '''return url that displays instance of itself'''
        #self.pk is the primary key to this article instancce
        return reverse('article',kwargs={'pk': self.pk})
    
class Comment(models.Model):
    '''encapsulate the idea of a comment on an article'''

    # model the 1 to many relationship with the article (foreign key)
    # what happens if the article gets deleted?
    # can leave orphan comments, protect the comments by not deleting the article, or delete all the comments with CASCADE
    article = models.ForeignKey("Article", on_delete=models.CASCADE)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        '''Return a string representation of this Comment object.'''
        return f'{self.text}'
    
