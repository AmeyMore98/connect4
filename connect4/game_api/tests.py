import json
from rest_framework.test import APITestCase
from django.urls import reverse

from game_api.utils.constants import Constants

class StartGameAPITestCase(APITestCase):
    
    def setUp(self):
        self.url = reverse("start_game")
        self.valid_message = Constants.GAME_READY

    def test_start_game(self):
        response = self.client.get(self.url)
        response_data = json.loads(response.content)
        self.assertEqual(200, response.status_code, "Recieved non-200 response")
        self.assertEqual(200, response_data["status"], "Recieved non-200 response status")
        self.assertEqual(self.valid_message, response_data["message"], "Recieved invalid message")


class MakeMoveAPITestCase(APITestCase):

    def setUp(self):
        start_game_url = reverse("start_game")
        start_game_response = self.client.get(start_game_url)
        self.start_game_response_data = json.loads(start_game_response.content)
        self.valid_move_msg = Constants.VALID_MOVE
        self.invalid_move_msg = Constants.INVALID_MOVE
    
    def test_valid_move(self):
        
        make_move_url = reverse("make_move")
        make_move_request_body = {
            "game_id": self.start_game_response_data["data"]["game_id"],
            "move_data": {
                "column": 2
            }
        }
        make_move_response = self.client.post(make_move_url, make_move_request_body, format='json')
        make_move_response_data = json.loads(make_move_response.content)
        self.assertEqual(200, make_move_response.status_code, "Recieved non-200 response")
        self.assertEqual(200, make_move_response_data["status"], "Recieved non-200 response status")
        self.assertEqual(self.valid_move_msg, make_move_response_data["message"], "Recieved invalid message")

    def test_invalid_move(self):
    
        make_move_url = reverse("make_move")
        make_move_request_body = {
            "game_id": self.start_game_response_data["data"]["game_id"],
            "move_data": {
                "column": 14
            }
        }
        make_move_response = self.client.post(make_move_url, make_move_request_body, format='json')
        make_move_response_data = json.loads(make_move_response.content)
        self.assertEqual(200, make_move_response.status_code, "Recieved non-200 response")
        self.assertEqual(400, make_move_response_data["status"], "Recieved non-200 response status")
        self.assertEqual(self.invalid_move_msg, make_move_response_data["message"], "Recieved invalid message")
