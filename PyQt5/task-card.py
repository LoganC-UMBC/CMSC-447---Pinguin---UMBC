# returns dictionary storing 
def dict_generate():
    dict_board = {}
    dict_card = {}
    all_boards = ping_boards()

    # iterate through all possible boards
    for i in range(len(all_boards)):
        print("BOARD NAME: ", all_boards[i].name)
        all_lists = all_boards[i].list_lists()
        # reset the dict list for a new board
        dict_list = {}
        # iterate through all of this boards lists
        for j in range(len(all_lists)):
            print("LIST NAME: ", all_lists[j].name)
            all_cards = all_lists[j].list_cards()
            # reset the cards list
            cards = []
            # iterate through all of this lists cards
            for k in range(len(all_cards)):
                print("CARD NAME: ", all_cards[k].name)
                # make a collection of all cards for this list
                cards.append(all_cards[k].name)
            # assign said collection of cards to this list
            dict_list[all_lists[j].name] = cards
        
        dict_board[all_boards[i].name] = dict_list

    #print(dict_board)
    return dict_board


# returns all boards for this user
def ping_boards():
    print("ping_boards")
    return client.list_boards()

# returns all lists under a board
def ping_lists(board_name):
    print("ping_lists")
    # store the index for the specified board
    i = board_index(board_name)
    
    all_boards = ping_boards()
    # return all lists for a board
    return all_boards[i].list_lists()

# returns all cards under a list
def ping_cards(board_name, list_name):
    print("ping_cards")
    # store all boards for this client
    all_boards = ping_boards()

    # store the index for the specified board
    i = board_index(board_name)
    # store the index for the specified list
    j = list_index(board_name, list_name, i)

    # store all lists under a board
    board_lists = all_boards[i].list_lists()
    # return all cards under a list
    return board_lists[j].list_cards()

# returns the index of the desired board
def board_index(board_name):
    # store all boards for this client
    all_boards = ping_boards()

    # locate the proper board
    for i in range(len(all_boards)):
        # if we have located the board
        if board_name == all_boards[i].name:
            return i
    return None

# returns the index of the desired list
def list_index(board_name, list_name, i):
    # store all boards for this client
    all_boards = ping_boards()
    # store all lists for this board
    board_lists = all_boards[i].list_lists()

    # locate the proper list
    for j in range(len(board_lists)):
        # if we have located the list
        if list_name == board_lists[j].name:
            return j
    return None

# returns the index of the desired card
def card_index(board_name, list_name, card_name, i, j):
    print("card_index")
    # store all boards for this client
    all_boards = ping_boards()

    # store all lists for this board
    board_lists = all_boards[i].list_lists()
    # store all the cards for this list
    card_list = board_lists[j].list_cards()
    # locate the proper card
    for k in range(len(card_list)):
        if card_name == card_list[k].name:
            return k
    return None

# create a task card
def ping_card_create(board_name, list_name, card_name, card_description):
    
    # store the boards index
    i = board_index(board_name)
    if i == None:
        return False
    # store the lists index
    j = list_index(board_name, list_name, i)
    if j == None:
        return False

    # store all lists for a board
    board_lists = ping_lists(board_name)
    # add card to the desired list
    board_lists[j].add_card(card_name, desc=card_description)
    print(board_lists[j])
    print("Creation Successful")
    return True

# delete a task card
# returns True if the task card has been deleted
# returns False if the task card cannot be deleted
def ping_card_delete(board_name, list_name, card_name):
    print("Delete")

    # store the boards index
    i = board_index(board_name)
    if i == None:
        return False
    # store the lists index
    j = list_index(board_name, list_name, i)
    if j == None:
        return False
    # store the cards index
    k = card_index(board_name, list_name, card_name, i, j)
    if k == None:
        return False

    # store all lists for this board
    board_lists = ping_lists(board_name)
    # store all cards for this list
    card_list = board_lists[j].list_cards()
    # delete this card
    card_list[k].delete()
    print("Successful Deletion")
    return True

# modify a task card's contents
def ping_card_modify(board_name, list_name, card_name):
    """
    board_name = ""
    list_name = ""
    card_name = ""
    """
    print("Modify")

# move a task card to a specified list
def ping_card_move(board_name, list_name, card_name, new_list_name):
    # store the boards index
    i = board_index(board_name)
    if i == None:
        return False
    # store the lists index
    j = list_index(board_name, list_name, i)
    if j == None:
        return False
    # store the new lists index
    new_list_index = list_index(board_name, new_list_name, i)
    if new_list_index == None:
        return False
    # store the cards index
    k = card_index(board_name, list_name, card_name, i, j)
    if k == None:
        return False 

    # store all lists for this board
    board_lists = ping_lists(board_name)
    # store all cards for this list
    card_list = board_lists[j].list_cards()
    print(board_lists[new_list_index].name)
    
    # change the list this card is under
    card_list[k].change_list(board_lists[new_list_index].id)
    print("Card Movement Successful")
    return True

# Using: https://pypi.org/project/py-trello/
# https://github.com/sarumont/py-trello
# PDF documentation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwji5eCS7OXvAhX-M1kFHeVGADMQFjAAegQIBxAD&url=https%3A%2F%2Freadthedocs.org%2Fprojects%2Fpy-trello-dev%2Fdownloads%2Fpdf%2Flatest%2F&usg=AOvVaw1-vlt-k1FXhBt1uslG60E7
from trello import TrelloClient
from trello.util import create_oauth_token
import authorization
import os


# store our applications API key/secret
os.environ["TRELLO_API_KEY"] = '2e0161c01eca7ad03bda843f811dac8b'
os.environ["TRELLO_API_SECRET"] = 'd4446e39644f0992f6db9859c77441754f0085ad5725d86699780d1ba86dfeea'
# get the users unique tokens
user_token = create_oauth_token()
print(user_token)
#print(user_token.get('oauth_token'))
#print(user_token.get('oauth_token_secret'))


# These need to be replaced with each user's information
# user: PinguinDevelopment447@gmail.com
# pass: Piw2amhhPy7DFng
client = TrelloClient(
    api_key = '2e0161c01eca7ad03bda843f811dac8b',
    api_secret = 'd4446e39644f0992f6db9859c77441754f0085ad5725d86699780d1ba86dfeea',
    #token = '3e412495cb8cb892871070726e2d289a4dbf781f0a8deb37bd04a39dbebf62de'
    token = user_token.get('oauth_token'),
    token_secret = user_token.get('oauth_token_secret')
)

board_name = "Base Board"
list_name = "To Do"
card_name = "Added Card"
# call delete function
#ping_card_delete(board_name, list_name, card_name)

board_name = "Base Board"
list_name = "To Do"
card_name = "Added Card"
card_description = "Added Description"
# call create function
#ping_card_create(board_name, list_name, card_name, card_description)

# call modify function
#ping_card_modify(board_name, list_name, card_name)

# find all boards
#print(ping_boards())

# find all lists for the specified board
#print(ping_lists(board_name))

# find all cards for the specified lsit
#print(ping_cards(board_name, list_name))

full_dict = dict_generate()
print(full_dict)

board_name = "Base Board"
list_name = "To Do"
card_name = "To Do Base Card"
new_list_name = "Done"
# move a card to a different list
ping_card_move(board_name, list_name, card_name, new_list_name)