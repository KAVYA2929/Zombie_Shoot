from django.urls import path
from . import views

urlpatterns = [
    path('weapons/', views.WeaponListView.as_view(), name='weapon_list'),
    path('inventory/', views.player_inventory, name='player_inventory'),
    path('unlock/<int:weapon_id>/', views.unlock_weapon, name='unlock_weapon'),
    path('equip/<int:weapon_id>/', views.equip_weapon, name='equip_weapon'),
]