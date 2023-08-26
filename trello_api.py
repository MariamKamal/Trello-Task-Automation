import requests
import configparser

class TrelloAPI:
    def __init__(self):
        config = configparser.ConfigParser()
        config.read("config.ini")
        self.api_key = config.get("Trello", "API_KEY")
        self.token = config.get("Trello", "TOKEN")

    def create_board(self, board_name):
        url = "https://api.trello.com/1/boards"
        params = {
            "key": self.api_key,
            "token": self.token,
            "name": board_name,
        }
        response = requests.post(url, json=params)
        response.raise_for_status()  # Raise an exception if the request was not successful
        return response.json()
