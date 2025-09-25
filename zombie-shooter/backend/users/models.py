from django.contrib.auth.models import AbstractUser
from django.db import models

class Player(AbstractUser):
    high_score = models.IntegerField(default=0)
    games_played = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)