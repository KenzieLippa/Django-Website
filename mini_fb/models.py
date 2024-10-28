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
    
    def get_friends(self):
        '''return a list of the friends profiles so we can display them'''
        #will be modeled after the status message display image thingy
        # perhaps update this later depending on whether or not this proves to be accurate
        friends = Friend.objects.all()
        friend_return = []

        mingus_friends = friends.filter(profile1__pk=self.pk)
        mingus_friends2 = friends.filter(profile2__pk=self.pk)
        # if not mingus_friends.exists():
        #     print("no")
        # #     # return []
        # elif not mingus_friends2.exists():
        #     print("no 2")
        # #     # return []
        
        # # print(mingus_friends2)
        # if mingus_friends.exists():
        #     for friend in mingus_friends2:
        #         mingus_friends.append(friend)

        # else:
        #     mingus_friends = mingus_friends2
        for friend in mingus_friends:
            friend_return.append(friend)
        for friend in mingus_friends2:
            friend_return.append(friend)

        
        # print("Was called")
        # for friend in mingus_friends:
        #     print(friend.profile2)

        return friend_return
        # friends = []
        # for friend in Friend.objects:
        #     if friend.profile1 == self or friend.profile2 == self:
        #         print("tru")


    def add_friend(self, other):
        '''will allow the user to add another friend'''

        # make sure the friend does not already exist
        curr = self.get_friends()
        can_add = True
        if other == self:
            can_add = False
        # keep can add as true and see if it cannot be added
        for foo in curr:
            # print(foo)
            if foo.profile1 == other:
                # print("already added!")
                can_add = False
            elif foo.profile2 == other:
                # print("already added too")
                can_add = False


        if can_add:
            # print("WE CAN ADD THIS YAY!")
            print(self)
            print(other)

            # forgot to add
            Friend.objects.create(profile1=self, profile2=other)
    
    def get_friend_suggestions(self):
        '''figure out what friends we could make'''
        # start by getting our current friends so we dont suggest them
        curr = self.get_friends()
        new = []
        for foo in curr:
            if not foo.profile1.pk == self.pk:
                new.append(foo.profile1)
            elif not foo.profile2.pk == self.pk:
                new.append(foo.profile2)

        friend_ids = [friend.pk for friend in new]
        friend_ids.append(self.pk)
            # print(foo)
        # print("CALLED")
        # friend_ids = [friend.pk for friend in curr]
        # for id in friend_ids:
        #     print(id)

        new_friends = Profile.objects.exclude(pk__in=friend_ids)

        # for friend in new:
        #     print(friend)
            # new_friends = new_friends.exclude(first_name__startswith=friend.first_name)
        # all_friend = Profile.objects.all()
        # # new_friend = []
        # for foo in curr:
        #     all_friend.exclude(first_name__exact=foo.first_name)
        #     print(foo)
        for friend in new_friends: 
           pass # print(friend)
        return new_friends


        


    



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


#new model for friends
class Friend(models.Model):
    '''allows profiles to connect with one another and see stuff in the feed'''
    #stores a relation of which profiles are friends
    profile1 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile1")
    profile2 = models.ForeignKey("Profile", on_delete=models.CASCADE, related_name="profile2")
    timeStamp = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.profile1.first_name} & {self.profile2.first_name} are friends!'
