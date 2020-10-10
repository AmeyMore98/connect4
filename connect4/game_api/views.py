from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView

from .utils.constants import Constants
from .utils.utils import Utils
from .services.game_handler import GameHandler
from .models import Game, Move
from .serializers import serializers

@api_view(['GET'])
def start_game(request):
    if request.method == 'GET':
        response = GameHandler.start_game()
        return Response(response)


@api_view(['POST'])
def make_move(request):
    if request.method == 'POST':
        request_data = request.data
        
        game_id = request_data.get(Constants.GAME_ID, None)
        if not game_id:
            return Response(Utils.build_reponse(Constants.STATUS_BAD_REQUEST, Constants.NO_GAME_ID))
        
        move_data = request_data.get(Constants.MOVE_DATA, None)
        if not move_data:
            return Response(Utils.build_reponse(
                status=Constants.STATUS_BAD_REQUEST,
                message=Constants.NO_MOVE_DATA
            )) 
        
        response = GameHandler.make_move(game_id, move_data)
        return Response(response)

@api_view(['GET'])
def list_moves(request, game_id):

    moves = Move.objects.filter(game_id=game_id).order_by('id')
    serialized_moves = serializers.MoveSerializer(moves, many=True)
    return Response(serialized_moves.data)

class GamesView(ListAPIView):

    queryset = Game.objects.all()
    serializer_class = serializers.GameSerializer
    # lookup_field = 'game_id'
