from rest_framework import generics, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Score
from .serializers import ScoreSerializer

class LeaderboardView(generics.ListAPIView):
    queryset = Score.objects.all()[:10]
    serializer_class = ScoreSerializer

@api_view(['POST'])
def submit_score(request):
    serializer = ScoreSerializer(data=request.data)
    if serializer.is_valid():
        score = serializer.save(player=request.user)
        
        # Update player high score
        if score.score > request.user.high_score:
            request.user.high_score = score.score
            request.user.save()
        
        request.user.games_played += 1
        request.user.save()
        
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)