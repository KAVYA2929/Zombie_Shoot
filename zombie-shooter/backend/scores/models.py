from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Score(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    wave_reached = models.IntegerField(default=1)
    zombies_killed = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-score']