from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('game', views.game, name='game'),
    path('player_hit', views.player_hit, name='player_hit'),
    path('stand', views.stand, name='stand'),
    path('place_bet', views.place_bet, name='place_bet'),
    path('lost_round', views.lost_round, name='lost_round'),
    path('won_round', views.won_round, name='won_round'),
    path('blackjack', views.blackjack, name='blackjack'),
]