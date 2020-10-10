import uuid
import numpy as np
import pickle
import base64

from game_api.utils.constants import Constants
from game_api.utils.utils import Utils
from game_api.models import Game, Move


class GameHandler:

    @staticmethod
    def start_game():
        # new_game_id = str()
        new_game = Game()
        new_game.game_id = uuid.uuid4()
        new_game.game_over = False
        new_game.board = GameHandler.serialize_board(Connect4Game.create_board())
        new_game.save()

        return Utils.build_reponse(Constants.STATUS_OK, Constants.GAME_READY, {'game_id': new_game.game_id})

    @staticmethod
    def serialize_board(board):
        board_bytes = pickle.dumps(board)
        board_base64 = base64.b64encode(board_bytes)
        return board_base64

    @staticmethod
    def make_move(game_id, move_data):
        try:
            current_game = Game.objects.get(game_id=game_id)
        except Game.DoesNotExist:
            return Utils.build_reponse(Constants.STATUS_FORBIDDEN, Constants.INVALID_GAME_ID)
        
        board = pickle.loads(base64.b64decode(current_game.board))
        column = move_data.get(Constants.COLUMN, None)
        if not column:
            return Utils.build_reponse(Constants.STATUS_BAD_REQUEST, Constants.NO_COLUMN)    
        
        indexed_column = column - 1
        if not Connect4Game.is_valid_move(board, indexed_column):
            return Utils.build_reponse(Constants.STATUS_BAD_REQUEST, Constants.INVALID_MOVE)
        
        current_player = current_game.player
        board = Connect4Game.next_move(board, indexed_column, current_player)
        move_data = {
            Constants.PLAYER: current_player,
            Constants.COLUMN: column,
            Constants.BOARD: Connect4Game.get_board(board)
        }
        GameHandler.save_move(current_game, current_player, column)
        if Connect4Game.winning_move(board, current_player):
            current_game.game_over = True
            response = Utils.build_reponse(Constants.STATUS_OK, "Player {} Wins!".format(current_player), move_data)
        else:
            current_game.player = [Constants.PLAYER_1, Constants.PLAYER_2][current_player == Constants.PLAYER_1]
            response = Utils.build_reponse(Constants.STATUS_OK, Constants.VALID_MOVE, move_data)
        current_game.board = GameHandler.serialize_board(board)
        current_game.save()   

        return response

    @staticmethod
    def save_move(game_id, player, column):
        move = Move()
        move.game_id = game_id
        move.player = player
        move.column = column
        move.save()


class Connect4Game:
    """Game class.
    Logic inspired from: https://github.com/KeithGalli/Connect4-Python.git
    """

    @staticmethod
    def create_board():
        board = np.zeros((Constants.ROW_COUNT, Constants.COLUMN_COUNT))
        return board

    @staticmethod
    def drop_piece(board, row, col, player):
        board[row][col] = player
        return board
    
    @staticmethod
    def is_valid_move(board, col):
        return col < Constants.COLUMN_COUNT and board[Constants.ROW_COUNT - 1][col] == 0
    
    @staticmethod
    def get_next_open_row(board, col):
        for row in range(Constants.COLUMN_COUNT):
            if board[row][col] == 0:
                return row

    @staticmethod
    def get_board(board):
        return np.flip(board, 0)
    
    @staticmethod
    def winning_move(board, player):
        # Check horizontal locations for win
        for col in range(Constants.COLUMN_COUNT - 3):
            for row in range(Constants.ROW_COUNT):
                if (
                    board[row][col] == player 
                    and board[row][col + 1] == player 
                    and board[row][col + 2] == player 
                    and board[row][col + 3] == player
                ):
                    return True

        # Check vertical locations for win
        for col in range(Constants.COLUMN_COUNT):
            for row in range(Constants.ROW_COUNT - 3):
                if (
                    board[row][col] == player 
                    and board[row + 1][col] == player 
                    and board[row + 2][col] == player 
                    and board[row + 3][col] == player
                ):
                    return True

        # Check positively sloped diaganols
        for col in range(Constants.COLUMN_COUNT - 3):
            for row in range(Constants.ROW_COUNT - 3):
                if (
                    board[row][col] == player 
                    and board[row + 1][col + 1] == player 
                    and board[row + 2][col + 2] == player 
                    and board[row + 3][col + 3] == player
                ):
                    return True

        # Check negatively sloped diaganols
        for col in range(Constants.COLUMN_COUNT - 3):
            for row in range(3, Constants.ROW_COUNT):
                if (
                    board[row][col] == player 
                    and board[row - 1][col + 1] == player 
                    and board[row - 2][col + 2] == player 
                    and board[row - 3][col + 3] == player
                ):
                    return True

    @staticmethod
    def next_move(board, col, player):
        row = Connect4Game.get_next_open_row(board, col)
        board = Connect4Game.drop_piece(board, row, col, player)
        return board
