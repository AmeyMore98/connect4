class Constants:
    '''Class for all constants used by game_api
    '''
    
    # Status
    STATUS_OK = 200
    STATUS_FORBIDDEN = 403
    STATUS_UNAUTHORIZED = 401
    STATUS_BAD_REQUEST = 400
    STATUS_ERROR = 500

    # Messages
    SUCCESS = 'Success'
    FAILURE = 'Server Error'
    INVALID_ACTION = 'Invalid Action'
    GAME_READY = 'Ready'
    VALID_MOVE = 'Valid Move'
    INVALID_MOVE = 'Invalid Move'
    NO_COLUMN = 'No Column present'
    INVALID_GAME_ID = 'Invalid game id'
    NO_GAME_ID = 'No game id received'
    NO_PLAYER = 'No player specified'

    # Keys
    DATA = 'data'
    CREDENTIALS = 'credentials'
    STATUS = 'status'
    MESSAGE = 'message'
    ERROR = 'error'
    TOKEN = 'token'
    ACTION = 'action'
    COLUMN = 'column'
    GAME_ID = 'game_id'
    GAME_OVER = 'game_over'
    CURRENT_PLAYER = 'current_player'
    STATE = 'state'
    PLAYER = 'player'
    BOARD = 'board'

    # Values
    START_GAME = 'start'
    PLAY_GAME = 'play'
    ACTIONS = (START_GAME, PLAY_GAME)
    PLAYER_1 = 1
    PLAYER_2 = 2
    ROW_COUNT = 6
    COLUMN_COUNT = 7
