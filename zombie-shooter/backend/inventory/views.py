from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Weapon, PlayerInventory, Upgrade, PlayerUpgrade
from .serializers import WeaponSerializer, PlayerInventorySerializer, UpgradeSerializer

class WeaponListView(generics.ListAPIView):
    queryset = Weapon.objects.all()
    serializer_class = WeaponSerializer

@api_view(['GET'])
def player_inventory(request):
    inventory, created = PlayerInventory.objects.get_or_create(player=request.user)
    serializer = PlayerInventorySerializer(inventory)
    return Response(serializer.data)

@api_view(['POST'])
def unlock_weapon(request, weapon_id):
    try:
        weapon = Weapon.objects.get(id=weapon_id)
        inventory, created = PlayerInventory.objects.get_or_create(player=request.user)
        inventory.unlocked_weapons.add(weapon)
        return Response({'message': f'{weapon.name} unlocked!'})
    except Weapon.DoesNotExist:
        return Response({'error': 'Weapon not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def equip_weapon(request, weapon_id):
    try:
        weapon = Weapon.objects.get(id=weapon_id)
        inventory, created = PlayerInventory.objects.get_or_create(player=request.user)
        
        if weapon in inventory.unlocked_weapons.all():
            inventory.current_weapon = weapon
            inventory.save()
            return Response({'message': f'{weapon.name} equipped!'})
        else:
            return Response({'error': 'Weapon not unlocked'}, status=status.HTTP_400_BAD_REQUEST)
    except Weapon.DoesNotExist:
        return Response({'error': 'Weapon not found'}, status=status.HTTP_404_NOT_FOUND)