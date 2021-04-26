# file generated by .ui of qt creator
from GUI.Uis.Main_Window_Ui.main_window_ui import *

# GUI library
from PyQt5 import QtCore, QtGui, QtWidgets, Qt

# Still haven't used drive
from Functions.google_drive.drive_test import *

# client for trello
from Functions.trello_api.task_card import *


# invites menu for a group, needs fixing to work properly
from GUI.Uis.Invite_Menu_Ui.invites_menu import *

import datetime

########################################################################################################################
#                                                         Main Window Class                                            #
########################################################################################################################
class Main_Window(Ui_main_window):

    def __init__(self, db):
        super().__init__()
        self.db = db
        self.user = self.db.user
        self.invites_signal = QtCore.pyqtSignal()
        self.current_group = None

        self.user_id = self.db.user.user_id
        self.trello = Trello()
        self.trello.action_setup(self.user_id)


    def setupUi(self, main_window):
        super().setupUi(main_window)

########################################################################################################################
#                                                         Menu bar setup                                               #
########################################################################################################################
        # adding menu bar items
        self.exit_menu = QtWidgets.QMenu("&Exit",main_window)
        self.help_menu = QtWidgets.QMenu("&Help",main_window)
        self.menubar.addMenu(self.exit_menu)
        self.menubar.addMenu(self.help_menu)

        # defining some QActions for menubar - NEED

########################################################################################################################
#                                                         Groups Tree model setup                                      #
########################################################################################################################
        # setting group tree model
        self.groups_tree.setHeaderHidden(True)
        self.groups_model = QtGui.QStandardItemModel()
        self.groups_node = self.groups_model.invisibleRootItem()

        self.groups_tree.setModel(self.groups_model)
        self.groups_tree.expandAll()

########################################################################################################################
#                                                         Forum tree model setup                                       #
########################################################################################################################
        # setting forum tree model
        self.forum_tree.setHeaderHidden(True)
        self.forum_model = QtGui.QStandardItemModel()
        self.forum_node = self.forum_model.invisibleRootItem()

        """# test data to work with
        item = StandardItem("")
        for i in range(10):
            item = StandardItem("group"+str(i))
            self.forum_node.appendRow(item)
            for j in range(6):
                item2 = StandardItem("member"+str(j))
                item.appendRow(item2)
        # end test data"""

        self.forum_tree.setModel(self.forum_model)
        self.forum_tree.expandAll()
########################################################################################################################
#                                                         adding test data for invites list                            #
########################################################################################################################
        """for i in range(10):
            item = GroupsListItem("user"+str(i),"group"+str(i))
            self.invites_list.addItem(item)"""

########################################################################################################################
#                                                         trello tree model setup                                      #
########################################################################################################################
        self.trello_tree.setHeaderHidden(True)
        self.trello_model = QtGui.QStandardItemModel()
        self.trello_node = self.trello_model.invisibleRootItem()

        """board = StandardItem("Board")
        list = StandardItem("list")
        card = StandardItem("task card")

        self.trello_node.appendRow(board)

        for i in range(5):
            list = StandardItem("list"+str(i))

            for j in range(5):
                card = StandardItem("task card"+str(j))
                list.appendRow(card)
            board.appendRow(list)
        """

        self.trello_tree.setModel(self.trello_model)
        self.trello_tree.expandAll()



########################################################################################################################
#                                                         error frame hiding                                           #
########################################################################################################################
        # hiding all error frames
        self.groups_error_frame.hide()
        self.forums_error_frame.hide()
        self.calendar_error_frame.hide()
        self.tasks_error_frame.hide()
        self.docs_error_frame.hide()

########################################################################################################################
#                                                         connecting all buttons                                       #
########################################################################################################################
        #connecting buttons
        self.connect_all_error_frames()
        self.connect_groups_buttons()
        self.connect_forums_buttons()
        self.connect_calendar_buttons()
        self.connect_tasks_buttons()
        self.connect_docs_buttons()


########################################################################################################################
#                                               connecting all buttons function                                        #
########################################################################################################################

    # connecting all error closing buttons
    def connect_all_error_frames(self):
        self.groups_close_popup_button.clicked.connect(lambda:self.error_frame_hide(self.groups_error_frame))
        self.forums_close_popup_button.clicked.connect(lambda:self.error_frame_hide(self.forums_error_frame))
        self.calendar_close_popup_button.clicked.connect(lambda:self.error_frame_hide(self.calendar_error_frame))
        self.tasks_close_popup_button.clicked.connect(lambda:self.error_frame_hide(self.tasks_error_frame))
        self.docs_close_popup_button.clicked.connect(lambda:self.error_frame_hide(self.docs_error_frame))


    # connecting all group tab buttons
    def connect_groups_buttons(self):
        self.create_group_button.clicked.connect(self.create_group)
        self.invite_button.clicked.connect(self.invite_members)
        self.delete_group_button.clicked.connect(self.delete_group)
        self.accept_invite_button.clicked.connect(self.accept_invite)
        self.decline_invite_button.clicked.connect(self.decline_invite)
        self.groups_tree.clicked.connect(self.view_group_description)


    # connecting all forum tab buttons
    def connect_forums_buttons(self):
        self.message_button.clicked.connect(self.send_message)
        self.forum_tree.clicked.connect(self.forum_change)
        """self.forum_timer = QtCore.QTimer(self.forum_view)
        self.forum_timer.timeout.connect(self.populate_forum_view)
        self.forum_timer.start(1000)"""


    # connecting all calendar tab buttons
    def connect_calendar_buttons(self):
        self.add_event_button.clicked.connect(self.add_event)


    # connecting all task tab buttons
    def connect_tasks_buttons(self):
        self.add_list_button.clicked.connect(self.add_list)
        self.delete_list_button.clicked.connect(self.delete_list)
        self.move_card_button.clicked.connect(self.move_card)
        self.edit_task_description_button.clicked.connect(self.edit_description)
        self.delete_task_button.clicked.connect(self.delete_task)
        self.card_add_button.clicked.connect(self.add_task)
        self.trello_tree.clicked.connect(self.get_description)


    # connecting all doc tab buttons
    def connect_docs_buttons(self):
        self.doc_create_button.clicked.connect(self.create_doc)
        self.doc_share_button.clicked.connect(self.share_link)
        self.doc_delete_button.clicked.connect(self.delete_doc)
        self.document_list.itemDoubleClicked.connect(self.hyperlink_doc)

    # error displaying func - don't really need but wth
    def error_frame_show(self, error_frame):
        error_frame.setVisible(True)


    # error hiding func - ^ you know what's up there
    def error_frame_hide(self, error_frame):
        error_frame.setVisible(False)


########################################################################################################################
#                                               Groups Tab                                                             #
########################################################################################################################

    # group create button function
    def create_group(self):
        # getting edit data
        group_name = self.group_name_edit.text()
        group_description = self.group_description_edit.toPlainText()
        group_invites = self.email_edit.toPlainText().split(',')

        # parse input
        if group_name+group_description == "":
            error_text = "Missing group name/group description"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)

        elif group_name != "" and group_description == "":
            error_text = "Missing group description"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)

        elif group_name == "" and group_description != "":
            error_text = "Missing group name"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)

        else:
            # clearing edits
            self.group_name_edit.clear()
            self.group_description_edit.clear()
            self.email_edit.clear()

            # creating group with or without invites
            if group_invites[0] == '':
                self.db.create_group(group_name,None)

            else:
                # need this function to have group invites
                # self.db.create_group(group_name,group_invites)
                pass


    # invite member button function
    # -currently not working
    def invite_members(self):
        invites_menu = QtWidgets.QWidget()
        invites_menu_ui = invites_menu_ext(self.invites_signal)
        invites_menu_ui.setupUi(invites_menu)
        invites_menu.show()


    # delete group button function
    # currently not connected to the db
    def delete_group(self):
        index = self.groups_tree.currentIndex()

        if index.data() == None:
            error_text = "Select a group to delete"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)

        elif (self.groups_model.parent(index).data() == None):
            self.groups_node.removeRow(index.row())


    # return all invites the user has
    # not yet working
    def get_invite(self):
        return


    # accept invite button function
    # accept an invite to a group
    # currently not connected to the db
    def accept_invite(self):
        if self.invites_list.currentItem() != None:
            invite = self.invites_list.takeItem(self.invites_list.row(self.invites_list.currentItem()))
            self.groups_node.appendRow(StandardItem(invite.text()))

        else:
            error_text = "No invite selected to accept"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)


    # decline invite button function
    # decline an invite to a group
    # not currently connected to the db
    def decline_invite(self):
        if self.invites_list.currentItem() != None:
            self.invites_list.takeItem(self.invites_list.row(self.invites_list.currentItem()))

        else:
            error_text = "No invite selected to decline"
            self.groups_error_label.setText(error_text)
            self.error_frame_show(self.groups_error_frame)


    # connected to groups_tree
    # get description of group from either the group item or member item and output to screen
    # i guess anything that is connected to a tree widget passes the index selected automatically
    def view_group_description(self, index):
        self.group_description_view.clear()
        item = self.groups_model.itemFromIndex(index)

        if item.role == "group":
            self.group_description_view.insertPlainText(item.description)

        elif item.role == "member" or item.role == "owner":
            self.group_description_view.insertPlainText(item.parent().description)


    # populate the group tree widget from db
    # will need a timer or refresh button
    def populate_groups_tree(self):
        groups = self.db.get_groups()
        for group in groups:
            new_group = StandardItem(group['name'], "group", group['description'])
            group_owner = StandardItem(group['owner'], "owner")
            new_group.appendRow(group_owner)
            members = group['members']
            members.remove(group['owner'])
            for member in members:
                new_group.appendRow(StandardItem(member, 'member'))

            self.groups_node.appendRow(new_group)



########################################################################################################################
#                                               Forums Tab                                                             #
########################################################################################################################

    # post a message to the database and repopulate the forum
    def send_message(self):
        # owner should be changed to User.name
        owner = self.db.user.name
        time = datetime.datetime.now().strftime("%H:%M:%S")
        message = self.message_edit.toPlainText()

        if message == "":
            error_text = "Enter a message to send to the group"
            self.forums_error_label.setText(error_text)
            self.error_frame_show(self.forums_error_frame)

        elif self.current_group == None:
            error_text = "Select a group to send a message to"
            self.forums_error_label.setText(error_text)
            self.error_frame_show(self.forums_error_frame)

        elif message == "" and self.current_group == None:
            error_text = "Select a group / Enter a message to the group"
            self.forums_error_label.setText(error_text)
            self.error_frame_show(self.forums_error_frame)

        else:
            self.db.send_post(self.current_group)
            self.populate_forum_view(self.current_group)
            # self.forum_view.insertPlainText((owner+"("+time+"): "+message)+"\n")


    # whenever a group is selected, the forum group label will change and the forum view repopulate
    def forum_change(self):
        index = self.forum_tree.currentIndex()

        if (self.forum_model.parent(index).data() == None):
            self.group_in_label.setText(index.data())
            self.current_group = index.data()
            self.populate_forum_view(self.current_group)

        elif index == None:
            self.group_in_label.setText("No Group selected")


    # get all forum posts from db for a particular group
    # probably should be from self.current_group
    # time format not included in the message
    # formatting between messages not included
    def populate_forum_view(self, group):
        self.forum_view.clear()
        messages = self.db.retrieve_all_posts(group)

        for message in messages:
            self.forum_view.insertPlainText(message['author']+ ":  " +message['message']+"\n")

########################################################################################################################
#                                               Calendar Tab                                                           #
########################################################################################################################

    # Yet to be worked on, only parsing for empty strings
    def add_event(self):
        start_time = "12:00AM"
        end_time = "11:59PM"
        event_date = self.date_edit.date()
        event_year = event_date.year()
        event_month = event_date.month()
        event_day = event_date.day()

        event_name = self.event_name_edit.text()
        event_description = self.event_description_edit.toPlainText()

        if event_name + event_description == "":
            error_text = "Missing event name/event description"
            self.calendar_error_label.setText(error_text)
            self.error_frame_show(self.calendar_error_frame)

        elif event_name == "" and event_description != "":
            error_text = "Missing event name"
            self.calendar_error_label.setText(error_text)
            self.error_frame_show(self.calendar_error_frame)

        elif event_name != "" and event_description == "":
            error_text = "Missing event description"
            self.calendar_error_label.setText(error_text)
            self.error_frame_show(self.calendar_error_frame)

        # might need to add date edit checker
        else:

            pass




########################################################################################################################
#                                               Tasks Tab                                                              #
########################################################################################################################

    # add a list to the trello client
    # not yet connected to trello
    def add_list(self):
        list_name = self.add_list_edit.text()
        duplicate = self.trello_model.findItems(list_name, QtCore.Qt.MatchExactly)

        if list_name == "":
            error_text = "Missing a list name to add"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "":
            if len(duplicate) == 0:
                print("here")
                # self.top_level.appendRow(new list)
                # update group trello board
                pass
            else:
                error_text = "List " + list_name + " already exists"
                self.tasks_error_label.setText(error_text)
                self.error_frame_show(self.tasks_error_frame)


    # delete a list to the trello client
    # not yet connected to trello
    def delete_list(self):
        list_name = self.add_list_edit.text()
        duplicate = self.trello_model.findItems(list_name, QtCore.Qt.MatchExactly)

        if list_name == "":
            error_text = "Missing a list name to delete"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "" and len(duplicate) == 1:
            print("task card exists")


    # move a card to another list
    # not yet connected to trello
    def move_card(self):
        board_from = self.board_move_edit.text()
        list_from = self.list_move_from_edit.text()
        card_from = self.card_move_edit.text()
        list_to = self.list_move_to_edit.text()

        if board_from+list_from+card_from+list_to == "":
            error_text = "Missing board(from) / list(from) / task card / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and list_from+card_from+list_to == "":
            error_text = "Missing list(from) / task card / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_from != "" and board_from+card_from+list_to == "":
            error_text = "Missing board(from) / task card / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif card_from != "" and board_from+list_from+list_to == "":
            error_text = "Missing board(from) / list(from) / list(to) "
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_to != "" and board_from+list_from+card_from == "":
            error_text = "Missing board(from) / list(from) / task card"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and list_from != "" and card_from+list_to == "":
            error_text = "Missing task card / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and card_from != "" and list_from+list_to == "":
            error_text = "Missing list(from) / list (to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and list_to != "" and list_from+card_from == "":
            error_text = "Missing list(from) / task card"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_from != "" and card_from != "" and board_from+list_to == "":
            error_text = "Missing board(from) / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_from != "" and list_to != "" and board_from+card_from == "":
            error_text = "Missing board(from) / task card"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif card_from != "" and list_from != "" and board_from+list_to == "":
            error_text = "Missing board(from) / list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif card_from != "" and list_to != "" and board_from+list_from == "":
            error_text = "Missing board(from) / list(from)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and list_from != "" and card_from != "" and list_to == "":
            error_text = "Missing list(to)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and list_from != "" and list_to != "" and card_from == "":
            error_text = "Missing task card"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_from != "" and card_from != "" and list_to != "" and list_from == "":
            error_text = "Missing list(from)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_from != "" and card_from != "" and list_to != "" and board_from == "":
            error_text = "Missing board(from)"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        else:
            # trello call to switch cards
            # call to update trello tree
            pass


    # change a cards description
    # not yet connected to trello
    def edit_description(self):
        index = self.trello_tree.currentIndex()

        if index.data() == None:
            error_text = "Select a task card to edit"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif index.data() != None:
            if self.trello_model.itemFromIndex(index).role != "card":
                error_text = "Select a task card to edit"
                self.tasks_error_label.setText(error_text)
                self.error_frame_show(self.tasks_error_frame)

            else:
                if self.edit_task_description_button.text() == "Edit Description":
                    self.task_card_view.setReadOnly(False)
                    self.edit_task_description_button.setText("Save Description")

                elif self.edit_task_description_button.text() == "Save Description":
                    self.task_card_view.setReadOnly(True)
                    self.edit_task_description_button.setText("Edit Description")



    # save new description to task card
    # not yet connected to trello client
    def save_description(self):
        pass


    # delete a task card from a list
    # not yet connected to trello
    def delete_task(self):
        index = self.trello_tree.currentIndex()

        if index.data() == None:
            error_text = "Select a task card to delete"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif index.data() != None:
            if self.trello_model.itemFromIndex(index).role != "card":
                error_text = "Select a task card to delete"
                self.tasks_error_label.setText(error_text)
                self.error_frame_show(self.tasks_error_frame)

            else:
                # call to trello client to delete card
                # remove from tree
                pass



    # add a task card to a list
    # not yet connected to trello
    def add_task(self):
        board_name = self.card_add_board_edit.text()
        list_name = self.card_add_list_edit.text()
        card_name = self.card_add_edit.text()
        task_description = self.card_description_edit.toPlainText()

        if board_name+list_name+card_name+task_description == "":
            error_text = "Missing board name / list name / task card name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and list_name+card_name+task_description == "":
            error_text = "Missing list name / task card name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "" and board_name+card_name+task_description == "":
            error_text = "Missing board name / task card name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif card_name != "" and board_name+list_name+task_description == "":
            error_text = "Missing board name / list name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif task_description != "" and board_name+list_name+card_name == "":
            error_text = "Missing board name / list name / task card name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and list_name != "" and card_name+task_description == "":
            error_text = "Missing task card name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and card_name != "" and list_name+task_description == "":
            error_text = "Missing list name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and task_description != "" and list_name+card_name == "":
            error_text = "Missing list name / task card name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "" and card_name != "" and board_name+task_description == "":
            error_text = "Missing board name / task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "" and task_description != "" and board_name+card_name == "":
            error_text = "Missing board name / task card name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif card_name != "" and task_description != "" and board_name+list_name == "":
            error_text = "Missing board name / list name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and list_name != "" and card_name != "" and task_description == "":
            error_text = "Missing task card description"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and list_name != "" and task_description != "" and card_name == "":
            error_text = "Missing task card name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif board_name != "" and card_name != "" and task_description != "" and list_name == "":
            error_text = "Missing list name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        elif list_name != "" and card_name != "" and task_description != "" and board_name == "":
            error_text = "Missing board name"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        else:
            # add task card to trello and add to tree view
            # or add to trello and use an update function

            new_board = StandardItem(board_name,"board")
            new_list = StandardItem(list_name, "list")
            new_card = StandardItem(card_name,"card", task_description)

            new_list.appendRow(new_card)
            new_board.appendRow(new_list)
            self.trello_node.appendRow(new_board)


    # get all trello boards, lists, and task cards to insert
    # pretty sure n^3 is what is making it run slow, not the connection to trello
    # would be better to run as something else lol
    def set_trello_tree(self):
        boards = self.trello.ping_boards()
        for board in boards:
            new_board = StandardItem(board.name, "board")

            lists = self.trello.ping_lists(board.name)
            for list in lists:
                new_list = StandardItem(list.name, "list")

                cards = self.trello.ping_cards(board.name, list.name)
                for card in cards:
                    new_card = StandardItem(card.name, "card", card.desc)
                    new_list.appendRow(new_card)
                new_board.appendRow(new_list)
            self.trello_node.appendRow(new_board)


    # when a user clicks on a task card this function runs
    # checking what mode the edit task button is in
    # wont allow a user to click on another card while editing the description
    def get_description(self, index):
        if self.edit_task_description_button.text() == "Save Description":
            error_text = "Save your task card description before you select another task card"
            self.tasks_error_label.setText(error_text)
            self.error_frame_show(self.tasks_error_frame)

        else:
            if self.trello_model.itemFromIndex(index).role == "card":
                self.task_card_view.clear()
                self.task_card_view.insertPlainText(self.trello_model.itemFromIndex(index).description)


########################################################################################################################
#                                               Docs Tab                                                               #
########################################################################################################################

    # create a new google doc
    # not yet connected to the db or gdrive
    def create_doc(self):
        # get data from edits
        doc_name = self.doc_create_edit.text()

        # clear edits
        self.doc_create_edit.clear()

        # list of all docs that match the name edit data
        docs = self.document_list.findItems(doc_name, QtCore.Qt.MatchExactly)

        if doc_name == "":
            error_text = "Enter a name for the new document"
            self.docs_error_label.setText(error_text)
            self.error_frame_show(self.docs_error_frame)

        else:
            if len(docs) != 0:
                error_text = "Document name already exists."
                self.docs_error_label.setText(error_text)
                self.error_frame_show(self.docs_error_frame)

            else:
                self.add_link(doc_name, "create")


    # share a user populated link
    # the user must use the https:// format to any link
    # not yet connected to the database
    def share_link(self):
        # get data from edits
        doc_name = self.doc_share_name_edit.text()
        doc_link = self.doc_share_link_edit.text()

        # clear edits
        self.doc_share_name_edit.clear()
        self.doc_share_link_edit.clear()

        # list of all docs that match the name edit data
        docs = self.document_list.findItems(doc_name, QtCore.Qt.MatchExactly)

        if doc_name + doc_link == "":
            error_text = "Enter a name and a link to share."
            self.docs_error_label.setText(error_text)
            self.error_frame_show(self.docs_error_frame)

        elif doc_name == "" and doc_link != "":
            error_text = "Enter a name to share link."
            self.docs_error_label.setText(error_text)
            self.error_frame_show(self.docs_error_frame)

        elif doc_name != "" and doc_link == "":
            error_text = "Enter a link to share."
            self.docs_error_label.setText(error_text)
            self.error_frame_show(self.docs_error_frame)

        else:
            if len(docs) != 0:
                error_text = "Document name already exists."
                self.docs_error_label.setText(error_text)
                self.error_frame_show(self.docs_error_frame)

            else:
                self.add_link(doc_name, "share", doc_link)


    # deletes the document by name
    # not yet connected to the database
    def delete_doc(self):
        # get data from edits
        doc_name = self.doc_delete_edit.text()

        # clear edits
        self.doc_delete_edit.clear()

        # list of all docs that match the name edit data
        docs = self.document_list.findItems(doc_name, QtCore.Qt.MatchExactly)

        if doc_name == "":
            error_text = "Enter the name of a doc you want to delete"
            self.docs_error_label.setText(error_text)
            self.error_frame_show(self.docs_error_frame)

        else:

            if len(docs) == 0:
                error_text = "No document by the name "+doc_name
                self.docs_error_label.setText(error_text)
                self.error_frame_show(self.docs_error_frame)

            else:
                for doc in docs:
                    self.document_list.takeItem(self.document_list.row(doc))


    # helper function to insert a document to the list widget
    # not yet connected to the database
    def add_link(self, doc_name, doc_type, doc_url=None):
        if doc_type == "create":
            # add doc to database
            self.document_list.addItem(DocListItem(doc_name))

        elif doc_type == "share":
            # add doc to database
            self.document_list.addItem(DocListItem(doc_name, doc_url))


    # if a document is double clicked on the url will be opened
    def hyperlink_doc(self):
        for doc in self.document_list.selectedItems():
            if doc.url != None:
                QtGui.QDesktopServices.openUrl(doc.url)

            else:
                pass


# QListWidgetItem for groups list
# may not be needed
class GroupsListItem(Qt.QListWidgetItem):
    def __init__(self, user_name, group_name):
        super().__init__(group_name)
        self.user_name = user_name

# Extension of QListWidgetItem to include link for document
# Used for insertion in the documents tab QListWidget self.document_list
class DocListItem(Qt.QListWidgetItem):
    def __init__(self, text,url=None):
        super().__init__(text)
        self.url = QtCore.QUrl(url)

# A QStandardItem for tree widgets
class StandardItem(QtGui.QStandardItem):
    def __init__(self,  txt='', role=None, description=None, font_size=12, set_bold=False, color=Qt.QColor(0, 0, 0)):
        super().__init__()
        self.role = role
        self.description = description
        fnt = Qt.QFont('Open Sans', font_size)
        fnt.setBold(set_bold)
        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)



"""if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)

    main_window = QtWidgets.QMainWindow()
    ui = Main_Window()
    ui.setupUi(main_window)
    main_window.show()
    sys.exit(app.exec_())"""