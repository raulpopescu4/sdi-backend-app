from . import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', views.home, name="home"),
    path('football_league/', FootballLeagueList.as_view()),
    path('football_league/<int:pk>/', FootballLeagueDetail.as_view()),
    path('football_team/', FootballTeamList.as_view()),
    path('football_team/<int:pk>/', FootballTeamDetail.as_view()),
    path('football_player/', FootballPlayerList.as_view()),
    path('football_player/<int:pk>/', FootballPlayerDetail.as_view()),
    path('competition/', CompetitionList.as_view()),
    path('competition/<int:pk>', CompetitionDetail.as_view()),
    path('competes_in/', CompetesInList.as_view()),
    path('competes_in/<int:pk>', CompetesInDetail.as_view()),
    path('avg_age_statistics/', AverageAgeTeamsView.as_view()),
    path('teams_by_number_of_players/', TeamsNumberOfPlayersView.as_view()),

]
