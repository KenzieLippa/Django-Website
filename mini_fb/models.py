from django.db import models

# Create your models here.
class Profile(models.Model):
    '''include details of the profile'''
    first_name = models.TextField(blank=False)
    last_name = models.TextField(blank=False)
    city = models.TextField(blank=False)
    email_address = models.TextField(blank=False)
    # for profile url
    profile_img = models.URLField(blank=False)


def __str__(self):
    '''Return the string of the profile?'''
    return f'{self.first_name} {self.last_name}'