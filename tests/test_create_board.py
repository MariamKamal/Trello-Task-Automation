import requests
import json
import os
import time
from config import API_KEY, API_TOKEN,BOARD_NAME


# Create a directory named 'response' if it doesn't exist
if not os.path.exists("response"):
    os.makedirs("response")

# Path to the response JSON file
response_file_path = os.path.join("response", "response_data.json")

# Create a dictionary to store the response data
response_data = {
    "board_id": None
}


# Create a new board
#BOARD_NAME = "Test Board1"
create_board_url = "https://api.trello.com/1/boards/"
create_board_params = {
    "key": API_KEY,
    "token": API_TOKEN,
    "name": BOARD_NAME
}

response = requests.post(create_board_url, params=create_board_params)
board_data = response.json()
board_id = board_data["id"]
response_data["board_id"] = board_id



print("Response data h:", response_data)   
# Write the response data to a JSON file
with open(response_file_path, "w") as json_file:
    json.dump(response_data, json_file, indent=4, default=str)



    
print("Board with lists created successfully!")
