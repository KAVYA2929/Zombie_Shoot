from django.urls import path
from . import views

urlpatterns = [
    path('leaderboard/', views.LeaderboardView.as_view(), name='leaderboard'),
    path('submit/', views.submit_score, name='submit_score'),
]