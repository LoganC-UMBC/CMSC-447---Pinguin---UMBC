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
    j = list_index(board_name, list_name)

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

    # store all lists for a board
    board_lists = ping_lists(board_name)
    card_list = board_lists[j].list_cards()
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


# Using: https://pypi.org/project/py-trello/
# https://github.com/sarumont/py-trello
# PDF documentation: https://www.google.com/url?sa=t&rct=j&q=&esrc=s&source=web&cd=&cad=rja&uact=8&ved=2ahUKEwji5eCS7OXvAhX-M1kFHeVGADMQFjAAegQIBxAD&url=https%3A%2F%2Freadthedocs.org%2Fprojects%2Fpy-trello-dev%2Fdownloads%2Fpdf%2Flatest%2F&usg=AOvVaw1-vlt-k1FXhBt1uslG60E7
from trello import TrelloClient

# These need to be replaced with each user's information
# user: PinguinDevelopment447@gmail.com
# pass: Piw2amhhPy7DFng
client = TrelloClient(
    api_key = '2e0161c01eca7ad03bda843f811dac8b',
    api_secret = 'd4446e39644f0992f6db9859c77441754f0085ad5725d86699780d1ba86dfeea',
    token = '3e412495cb8cb892871070726e2d289a4dbf781f0a8deb37bd04a39dbebf62de'
)

"""
JUST SOME SAMPLE CODE TO FIGURE OUT HOW IT WORKS
"""
"""
# store all the boards for this client
all_boards = client.list_boards()
# store the first board
board = client.list_boards()[0]
print(board)
print(board.list_lists())
print(board.list_lists()[0].id)

# grab the ID of the first list within the board
list_id = board.list_lists()[0].id
# store a list of all boards
all_boards = client.list_boards()
# get a list of cards in this list
my_card_list = board.get_list(list_id)

for card in my_card_list.list_cards():
    print(card.name)
"""

board_name = "Base Board"
list_name = "To Do"
card_name = "Added Card"
# call delete function
ping_card_delete(board_name, list_name, card_name)

board_name = "Base Board"
list_name = "To Do"
card_name = "Added Card"
card_description = "Added Description"
# call create function
ping_card_create(board_name, list_name, card_name, card_description)

# call modify function
#ping_card_modify(board_name, list_name, card_name)

# find all boards
print(ping_boards())

# find all lists for the specified board
print(ping_lists(board_name))

# find all cards for the specified lsit
print(ping_cards(board_name, list_name))