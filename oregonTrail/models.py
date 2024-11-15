from django.db import models

# Create your models here.

class GameState(models.Model):
    is_running = models.BooleanField(default=False)