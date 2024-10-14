from django.db import models

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
        
    

class StatusMsg(models.Model):
    '''allow users to include a status message'''
    profile = models.ForeignKey("Profile", on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f'{self.text}'