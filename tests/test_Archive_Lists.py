import requests
import json
from config import API_KEY, API_TOKEN, BOARD_NAME

# API endpoint to get boards by name
boards_url = "https://api.trello.com/1/members/me/boards"
query_params = {
    "key": API_KEY,
    "token": API_TOKEN
}

# Get all boards
response = requests.get(boards_url, params=query_params)
boards = response.json()

board_id = None

# Find the board by name
for board in boards:
    if board["name"] == BOARD_NAME:
        board_id = board["id"]
        print(f"Board with name '{BOARD_NAME}' found. Board ID: {board_id}")
        break

if board_id:
    # API endpoint to get lists from the board
    lists_url = f"https://api.trello.com/1/boards/{board_id}/lists"
    
    # Get lists from the board
    response = requests.get(lists_url, params=query_params)
    lists = response.json()

    # Archive lists
    for list_data in lists:
        list_id = list_data["id"]
        archive_list_url = f"https://api.trello.com/1/lists/{list_id}/closed"
        response = requests.put(archive_list_url, params=query_params, json={"value": "true"})
        if response.status_code == 200:
            print(f"List with ID {list_id} archived successfully.")
        else:
            print(f"Failed to archive list with ID {list_id}. Error content: {response.content}")

    print("All lists archived on the board.")
else:
    print(f"Board with name '{BOARD_NAME}' not found.")
