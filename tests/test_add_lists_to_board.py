import requests
import json
import os
from config import API_KEY, API_TOKEN,BOARD_NAME,list_names


#BOARD_NAME = "Test Board1"

# Create a directory named 'response' if it doesn't exist
if not os.path.exists("response"):
    os.makedirs("response")

# Path to the response JSON file
response_file_path = os.path.join("response", "response_data.json")

# Create a dictionary to store the response data
response_data = {
    "list_ids": []
}


# Get a list of boards that match the provided name
get_boards_url = f"https://api.trello.com/1/members/me/boards"
get_boards_params = {
    "key": API_KEY,
    "token": API_TOKEN,
    "fields": "id,name"
}

response = requests.get(get_boards_url, params=get_boards_params)
boards_data = response.json()

# Find the board with the specified name and retrieve its ID
board_id = None
for board in boards_data:
    if board["name"] == BOARD_NAME:
        board_id = board["id"]
        break

if board_id:
    print(f"Board ID for '{BOARD_NAME}': {board_id}")
else:
    print(f"Board '{BOARD_NAME}' not found.")
    


# Create lists on the board
for list_name in list_names:
    create_list_url = f"https://api.trello.com/1/lists/"
    create_list_params = {
        "key": API_KEY,
        "token": API_TOKEN,
        "name": list_name,
        "idBoard": board_id
    }
    response = requests.post(create_list_url, params=create_list_params)
    list_data = response.json()
    list_id = list_data["id"]
    response_data["list_ids"].append(list_id)
    print(f"List '{list_name}' created with ID: {list_id}")
    
print("Response data h:", response_data)   
# Write the response data to a JSON file
with open(response_file_path, "w") as json_file:
    json.dump(response_data, json_file, indent=4, default=str)
    
print("lists Added to board successfully!")
