from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Weapon(models.Model):
    name = models.CharField(max_length=50)
    damage = models.IntegerField()
    fire_rate = models.FloatField()
    ammo_capacity = models.IntegerField()
    unlock_wave = models.IntegerField(default=1)
    
    def __str__(self):
        return self.name

class PlayerInventory(models.Model):
    player = models.OneToOneField(User, on_delete=models.CASCADE)
    unlocked_weapons = models.ManyToManyField(Weapon, blank=True)
    current_weapon = models.ForeignKey(Weapon, on_delete=models.SET_NULL, null=True, related_name='current_users')
    health_upgrades = models.IntegerField(default=0)
    speed_upgrades = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.player.username}'s Inventory"

class Upgrade(models.Model):
    UPGRADE_TYPES = [
        ('health', 'Health'),
        ('speed', 'Speed'),
        ('damage', 'Damage'),
    ]
    
    name = models.CharField(max_length=50)
    upgrade_type = models.CharField(max_length=20, choices=UPGRADE_TYPES)
    cost = models.IntegerField()
    effect_value = models.IntegerField()
    max_level = models.IntegerField(default=5)
    
    def __str__(self):
        return self.name

class PlayerUpgrade(models.Model):
    player = models.ForeignKey(User, on_delete=models.CASCADE)
    upgrade = models.ForeignKey(Upgrade, on_delete=models.CASCADE)
    level = models.IntegerField(default=0)
    
    class Meta:
        unique_together = ['player', 'upgrade']