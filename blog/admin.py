from django.contrib import admin

# Register your models here.

# have to reg the model here
from .models import *

admin.site.register(Article)
# forgot to register the comments lol
admin.site.register(Comment)




# after this part we manage this stuff
'''python manage.py makemigrations blog
python manage.py migrate
then create a superuser?
python manage.py createsuperuser'''