from django.urls import path

from .views import start_game, make_move, list_moves, GamesView

urlpatterns = [
    # path('', GameController.as_view())
    path('start_game', start_game, name='start_game'),
    path('make_move', make_move, name='make_move'),
    path('list_moves/<str:game_id>', list_moves, name='list_moves'),
    path('list_games', GamesView.as_view(), name='list_games')
]
