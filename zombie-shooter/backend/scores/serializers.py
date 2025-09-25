from rest_framework import serializers
from .models import Score

class ScoreSerializer(serializers.ModelSerializer):
    player_name = serializers.CharField(source='player.username', read_only=True)

    class Meta:
        model = Score
        fields = ['id', 'player', 'player_name', 'score', 'wave_reached', 'zombies_killed', 'created_at']
        read_only_fields = ['player']