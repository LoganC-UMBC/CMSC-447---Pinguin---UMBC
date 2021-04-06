# create a task card
def ping_card_create():
    """
    board_name = ""
    list_name = ""
    card_name = ""
    card_description = ""
    """
    print("Create")

# delete a task card
# returns True if the task card has been deleted
# returns False if the task card cannot be deleted
def ping_card_delete(client):
    """
    board_name = ""
    list_name = ""
    card_name = ""
    """
    board_name = "Base Board"
    list_name = "To Do"
    card_name = "To Do Base Card"

    print("Delete")
    # store all the boards for this client
    all_boards = client.list_boards()

    # locate the proper boards
    for i in range(len(all_boards)):
        print("Board Name: ", all_boards[i].name)
        # if we have located the board
        if board_name == all_boards[i].name:
            board_lists = all_boards[i].list_lists()
            print("Lists Name: ", board_lists)
            # locate the proper list
            for j in range(len(board_lists)):
                print("List Name: ", board_lists[j].name)
                # if we have located the list
                if list_name == board_lists[j].name:
                    card_list = board_lists[j].list_cards()
                    # locate the proper card
                    for k in range(len(card_list)):
                        print("Card: ", card_list[k].name)
                        if card_name == card_list[k].name:
                            card_list[k].delete()
                            return True

    print("Failed Deletion")
    return False

# modify a task card's contents
def ping_card_modify():
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

# call my delete function
ping_card_delete(client)
