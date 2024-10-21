from django.db import models
from django.urls import reverse

# Create your models here.
class Profile(models.Model):
    '''include details of the profile'''
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.EmailField(blank=False)
    # for profile url
    profile_img = models.URLField(blank=False)



    def __str__(self):
        '''Return the string of the profile?'''
        return f'{self.first_name} {self.last_name}'

    def get_stat_msg(self):
        '''return status message'''
        status = StatusMsg.objects.filter(profile = self)
        return status
        
    def get_absolute_url(self):
        '''return url that displays instance of itself'''
        #self.pk is the primary key to this article instancce
        return reverse('profile',kwargs={'pk': self.pk})

class StatusMsg(models.Model):
    '''allow users to include a status message'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    timeStamp = models.DateTimeField(auto_now=True)
    #add here the ability to add an image?

    def __str__(self) -> str:
        return f'{self.text}'
    
    def get_images(self):
        '''attempts to figure out how to return a query of images'''
        return self.image_set.all()
    
class Image(models.Model):
    '''define an image model'''
    # may not require the profile
    # profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    status_msg = models.ForeignKey("StatusMsg", on_delete=models.CASCADE)
    image = models.ImageField(blank=True)
    timeStamp = models.DateTimeField(auto_now=True)