from django.db import models

# Create your models here.

# here is where we create the models ig
# this is from the class assignment
class Article(models.Model):
    '''encapsulate the idea of an article by some author'''
    #data attributse of an article
    title = models.TextField(blank=False)
    author = models.TextField(blank=False)
    text = models.TextField(blank=False)
    published = models.DateTimeField(auto_now=True)

    def __str__(self):
        '''return a string rep of this article object'''
        return f'{self.title} by {self.author}' 