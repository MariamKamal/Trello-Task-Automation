import requests
from config import API_KEY, API_TOKEN,BOARD_NAME,card_titles,LIST_NAME





# Construct the API URL for fetching boards
boards_url = f"https://api.trello.com/1/members/me/boards?key={API_KEY}&token={API_TOKEN}"

# Make the API request to get the boards
response = requests.get(boards_url)

if response.status_code == 200:
    boards = response.json()
    
    board_id = None
    for board in boards:
        if board['name'] == BOARD_NAME:
            board_id = board['id']
            break
    
    if board_id:
        # Construct the API URL for fetching lists on the board
        lists_url = f"https://api.trello.com/1/boards/{board_id}/lists?key={API_KEY}&token={API_TOKEN}"
        
        # Make the API request to get the lists on the board
        response = requests.get(lists_url)
        
        if response.status_code == 200:
            lists = response.json()
            
            list_id = None
            for lst in lists:
                if lst['name'] == LIST_NAME:
                    list_id = lst['id']
                    break
            
            if list_id:
                print(f"List ID of '{LIST_NAME}': {list_id}")
            else:
                print(f"List with name '{LIST_NAME}' not found.")
        else:
            print("Failed to retrieve lists on the board.")
    else:
        print(f"Board with name '{BOARD_NAME}' not found.")
else:
    print("Failed to retrieve boards.")

# Construct the API URL for fetching cards in the specified list
url = f"https://api.trello.com/1/lists/{list_id}/cards?key={API_KEY}&token={API_TOKEN}"

# Make the API request to get the list of cards in the list
response = requests.get(url)

if response.status_code == 200:
    cards_in_list = [card['name'] for card in response.json()]
    
    cards_added = []
    cards_not_added = []
    
    for card in card_titles:
        if card in cards_in_list:
            cards_added.append(card)
        else:
            cards_not_added.append(card)
    
    if cards_added:
        print("Cards added:", ', '.join(cards_added))
    else:
        print("No cards have been added.")
    
    if cards_not_added:
        print("Cards not added:", ', '.join(cards_not_added))
    else:
        print("All cards have been added.")
else:
    print("Failed to retrieve cards in the list.")




