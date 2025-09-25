from rest_framework import serializers
from .models import Weapon, PlayerInventory, Upgrade, PlayerUpgrade

class WeaponSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weapon
        fields = '__all__'

class PlayerInventorySerializer(serializers.ModelSerializer):
    unlocked_weapons = WeaponSerializer(many=True, read_only=True)
    current_weapon = WeaponSerializer(read_only=True)
    
    class Meta:
        model = PlayerInventory
        fields = ['unlocked_weapons', 'current_weapon', 'health_upgrades', 'speed_upgrades']

class UpgradeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Upgrade
        fields = '__all__'

class PlayerUpgradeSerializer(serializers.ModelSerializer):
    upgrade = UpgradeSerializer(read_only=True)
    
    class Meta:
        model = PlayerUpgrade
        fields = ['upgrade', 'level']