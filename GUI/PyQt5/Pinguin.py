import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QGridLayout, QMenuBar, QMenu, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QFrame, QLabel, QCheckBox, QTreeView, QTableWidget, QFormLayout, QSpacerItem, QListView, QComboBox, QTextEdit, QCalendarWidget, QDateEdit


from PyQt5.QtGui import QIcon, QDesktopServices, QColor, QFont
from PyQt5.QtCore import pyqtSlot, QSize, Qt, QRect, QMetaObject, pyqtSignal
from PyQt5.Qt import QStandardItemModel, QStandardItem, QSizePolicy

from PinguinDB import PinguinDB
from Login_Menu import Ui_Login_Window
MAX_W = 700
MAX_H = 506

DB = PinguinDB()
# This is the login window that will appear first when the application is started.
# We need two line edit objects and two push buttons .
# The push buttons will be to login with the input(user and pass) from the two line edits
# and to let the user create an account.
# We need to add some graphics and maybe a help menu button.
# Send a pop up to the user if the login is wrong
# When the login is successful the main menu should appear and the login window should hide
class Login_Window(QMainWindow):
    def __init__(self,login_signal):
        super(QMainWindow, self).__init__()
        self.ui = Ui_Login_Window(login_signal)
        self.ui.set_up_ui(self)





# This is the main menu window that appears after login is successful
# The default constructor will setup and instance of a Main Window set with the appropiate tabs
class Main_Menu(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()

        self.setMaximumSize(MAX_W, MAX_H)
        self.setMinimumSize(MAX_W, MAX_H)

        self.setWindowIcon(QIcon("447logoicon"))
        self.setWindowTitle("Pinguin")
        self.layout = QGridLayout()
        self.tab_widget = Main_TabWidget()
        # self.tab_widget.setTabShape(self.tab_widget.Rounded)

        self.setCentralWidget(self.tab_widget)
        self.setLayout(self.layout)



# This would be the menu bar above the main UI
# We can have help menus in here or have separate tools related to each tab
class Menu_Bar(QMenuBar):
    def __init__(self):
        super(QMenuBar).__init__()




# This is the tab widget which holds each tab related to a specific functionality
class Main_TabWidget(QTabWidget):

    def __init__(self):
        super(Main_TabWidget, self).__init__()
        self.setStyleSheet("QTabWidget::pane { border: 0; }");

        self.groups_tab = Groups_Tab()
        self.calendar_tab = Calendar_Tab()
        self.forums_tab = Forums_Tab()
        self.tasks_tab = Tasks_Tab()
        self.tasks_tab.sender()
        self.documents_tab = Documents_Tab()

        self.addTab(self.groups_tab, "Groups")
        self.addTab(self.forums_tab, "Forums")
        self.addTab(self.calendar_tab, "Calendar")
        self.addTab(self.tasks_tab, "Tasks")
        self.addTab(self.documents_tab, "Documents")




# Each tab needed to be deisgned to hold the appropiate widgets
class Groups_Tab(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        # Main layout
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)

#############################################################################################

        self.groups_and_users_widget = QWidget()
        self.groups_and_users_layout = QVBoxLayout()
        self.groups_and_users_widget.setLayout(self.groups_and_users_layout)

        # Tree view object to see Groups and users in the group
        self.groups_tree = QTreeView()
        self.groups_tree.setHeaderHidden(True)
        self.tree_model = QStandardItemModel()
        self.rootNode = self.tree_model.invisibleRootItem()
        self.groups_tree_label = QLabel("Groups")

        # This would initially populate the list view with items
        #self.updateTreeView()
        self.groups_tree.setModel(self.tree_model)
        self.groups_tree.expandAll()
        self.groups_tree.clicked.connect(self.getValueTree)
        self.groups_tree.setMaximumSize(300,400)

        self.group_description = QListView()
        self.group_description.setMaximumWidth(300)
        # self.group_description.setMaximumSize(200,200)

        self.group_description_label = QLabel("Description")

        self.set_group_button = QPushButton("Set current group")

        self.groups_and_users_layout.addWidget(self.groups_tree_label)
        self.groups_and_users_layout.addWidget(self.groups_tree)
        self.groups_and_users_layout.addWidget(self.set_group_button)
        self.groups_and_users_layout.addWidget(self.group_description_label)
        self.groups_and_users_layout.addWidget(self.group_description)

#############################################################################################

        self.buttons_widget = QWidget()
        self.buttons_layout = QGridLayout()
        self.buttons_widget.setLayout(self.buttons_layout)

        self.create_groups_button = QPushButton("Create Group")
        self.create_groups_text = QTextEdit()
        self.create_groups_text.setPlaceholderText("Enter your group's name...")
        self.create_groups_text.setMaximumHeight(30)

        self.invite_to_groups_button = QPushButton("Invite users to Group")
        self.invite_text = QTextEdit()
        self.invite_text.setPlaceholderText("email1@example.com, email2@example.com, ...")
        self.invite_text.setMaximumHeight(100)

        self.delete_groups_label = QLabel("This will show current group's name")
        self.delete_groups_label.setFont(QFont('Calibri',13))
        self.delete_groups_label.setStyleSheet("QLabel { background-color : white; color : red; }")
        self.delete_groups_button = QPushButton("Delete Group")

        self.buttons_layout.addWidget(self.create_groups_button,0,0)
        self.buttons_layout.addWidget(self.create_groups_text,0,1)
        self.buttons_layout.addWidget(self.invite_to_groups_button,1,0)
        self.buttons_layout.addWidget(self.invite_text,1,1)
        self.buttons_layout.addWidget(self.delete_groups_button,2,0)
        self.buttons_layout.addWidget(self.delete_groups_label,2,1)

#############################################################################################

        self.main_layout.addWidget(self.groups_and_users_widget,0,0)
        self.main_layout.addWidget(self.buttons_widget,0,1)

    def getValueTree(self, val):
        print(val.data())
        print(val.row())
        print(val.column())

class Forums_Tab(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.setObjectName("forums_tab")
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)


        self.left_forums_widget = QWidget()
        self.setObjectName("left_forums_widget")
        self.left_forums_widget_layout = QVBoxLayout()
        self.left_forums_widget.setLayout(self.left_forums_widget_layout)

        # Still need to connect click to the listview of messages
        self.group_pick_view = QTableWidget()
        self.group_pick_view.setGeometry(0,0,256,607)

        self.left_forums_widget_layout.addWidget(self.group_pick_view)


        self.right_forums_widget = QWidget()
        #self.right_forums_widget.resize(200, 200)
        self.right_forums_layout = QVBoxLayout()
        #self.right_forums_layout.setGeometry(QRect(0,0,200,200))
        self.right_forums_widget.setLayout(self.right_forums_layout)

        self.forum = QListView()
        self.message_edit = QTextEdit()
        self.message_send_button = QPushButton("Send Message")

        self.right_forums_layout.addWidget(self.forum)
        self.right_forums_layout.addWidget(self.message_edit)
        self.right_forums_layout.addWidget(self.message_send_button)



        self.main_layout.addWidget(self.left_forums_widget)
        self.main_layout.addWidget(self.right_forums_widget)



class Calendar_Tab(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()

        # I should be doing this with every widget()
        self.setObjectName("calendar_tab")

        #Main layout as a horizontal layout
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        #Left side widget set to verticak mode
        self.left_calendar_widget = QWidget()
        self.left_calendar_widget_layout = QVBoxLayout()
        self.left_calendar_widget.setLayout(self.left_calendar_widget_layout)


        self.calendar = QCalendarWidget(self)


        self.event_add_widget = QWidget()
        self.event_add_widget_layout = QVBoxLayout()
        self.event_add_widget.setLayout(self.event_add_widget_layout)

        self.date_input_widget = QWidget()
        self.date_input_widget_layout = QHBoxLayout()
        self.date_input_widget.setLayout(self.date_input_widget_layout)

        self.date_input_edit = QDateEdit()
        self.date_name = QLineEdit()

        self.date_input_widget_layout.addWidget(self.date_input_edit)
        self.date_input_widget_layout.addWidget(self.date_name)



        self.date_add_widget = QWidget()
        self.date_add_widget_layout = QVBoxLayout()
        self.date_add_widget.setLayout(self.date_add_widget_layout)

        self.date_description = QTextEdit()

        self.date_add_button_widget = QWidget()
        self.date_add_button_widget_layout = QHBoxLayout()
        self.date_add_button_widget.setLayout(self.date_add_button_widget_layout)

        self.date_add_button = QPushButton("Add Event")
        self.date_add_button_widget_layout.setAlignment(Qt.AlignCenter)
        #self.date_add_button.resize(50,50)

        self.date_add_button_widget_layout.addWidget(self.date_add_button)

        self.date_add_widget_layout.addWidget(self.date_description)
        self.date_add_widget_layout.addWidget(self.date_add_button_widget)

        self.event_add_widget_layout.addWidget(self.date_input_widget)
        self.event_add_widget_layout.addWidget(self.date_add_button)
        self.event_add_widget_layout.addWidget(self.date_description)




        self.left_calendar_widget_layout.addWidget(self.calendar)
        self.left_calendar_widget_layout.addWidget(self.event_add_widget)


        self.right_calender_widget = QWidget()
        self.right_calender_widget_layout = QVBoxLayout()
        self.right_calender_widget.setLayout(self.right_calender_widget_layout)

        self.date_view_text = QListView(self.right_calender_widget)

        self.right_calender_widget_layout.addWidget(self.date_view_text)

        self.main_layout.addWidget(self.left_calendar_widget)
        self.main_layout.addWidget(self.right_calender_widget)





class Tasks_Tab(QWidget):

    def __init__(self):
        super(QWidget, self).__init__()
        self.setObjectName("tasks_tab")
        # The main layout in which all other widgets will be
        self.main_layout = QHBoxLayout()
        # Set the layout of the Tasks_Tab
        self.setLayout(self.main_layout)

         # Layout for the tree area widget or the left side of the GUI
        self.left_layout = QVBoxLayout()
        
        #label for tree
        self.tree_view_label = QLabel("Boards, Lists, and Tasks")
        self.tree_view_label.setAlignment(Qt.AlignCenter)
        # Tree area widget to hold the tree view
        self.tree_area = QWidget()
        self.tree_area.setObjectName("tree_area")
        self.tree_area.setGeometry(0,0,256,607)
        self.tree_area.setLayout(self.left_layout)


        # Tree view object to see boards, lists, and taskcards names
        treeView = QTreeView()
        #treeView.resize(256,607)
        treeView.setHeaderHidden(True)
        treeModel = QStandardItemModel()
        rootNode = treeModel.invisibleRootItem()
        # This would initially populate the list view with items
        self.updateTreeView()
        treeView.setModel(treeModel)
        treeView.expandAll()
        treeView.clicked.connect(self.getValueTree)
        self.left_layout.addWidget(self.tree_view_label)
        
        self.left_layout.addWidget(treeView)


        # middle portion of the task tab
        self.task_card_section = QWidget()
        self.middle_layout = QVBoxLayout()
        self.task_card_section.setLayout(self.middle_layout)

        self.task_card_button_widget = QWidget(self.task_card_section)
        self.task_card_button_set = QHBoxLayout()
        self.task_card_button_widget.setLayout(self.task_card_button_set)

        self.task_card_label = QLabel("Task")
        self.task_card_label.setAlignment(Qt.AlignCenter)
        
        self.task_card = QTableWidget()

        self.task_card.setGeometry(266, 0, 256, 303)
        
        self.delete_task_button = QPushButton("Delete Task")
        self.delete_task_button.clicked.connect(self.delete_task)
        
        self.edit_task_button = QPushButton("Edit Description")
        self.edit_task_button.clicked.connect(self.edit_description)

        self.task_card_button_set.addWidget(self.edit_task_button)
        self.task_card_button_set.addWidget(self.delete_task_button)


        self.create_task_widget = QWidget()
        self.create_task_widget_layout = QVBoxLayout()
        self.create_task_widget.setLayout(self.create_task_widget_layout)

        self.add_board_widget = QWidget()
        self.add_board_widget_layout = QHBoxLayout()
        self.add_board_widget.setLayout(self.add_board_widget_layout)
        
        #self.add_board_label = QLabel("")
        self.add_board_edit = QLineEdit()
        self.add_board_edit.setPlaceholderText("Enter name of Board")
        self.add_board_button = QPushButton("Add Board")
        self.add_board_button.clicked.connect(self.add_board)
        self.delete_board_button = QPushButton("Delete Board")
        self.delete_board_button.clicked.connect(self.delete_board)
        
        #self.add_board_widget_layout.addWidget(self.add_board_label)
        self.add_board_widget_layout.addWidget(self.add_board_edit)
        self.add_board_widget_layout.addWidget(self.add_board_button)
        self.add_board_widget_layout.addWidget(self.delete_board_button)
        
        self.add_list_widget = QWidget()
        self.add_list_widget_layout = QHBoxLayout()
        self.add_list_widget.setLayout(self.add_list_widget_layout)
        
        #self.add_list_label = QLabel("")
        self.add_list_edit = QLineEdit()
        self.add_list_edit.setPlaceholderText("Enter name of List")
        self.add_list_button = QPushButton("Add List")
        self.add_list_button.clicked.connect(self.add_list)
        
        self.delete_list_button = QPushButton("Delete List")
        self.delete_list_button.clicked.connect(self.delete_list)
        
        #self.add_list_widget_layout.addWidget(self.add_list_label)
        self.add_list_widget_layout.addWidget(self.add_list_edit)
        self.add_list_widget_layout.addWidget(self.add_list_button)
        self.add_list_widget_layout.addWidget(self.delete_list_button)
        
        
        self.pick_task_widget = QWidget()#self.create_task_widget
        self.pick_task_layout = QHBoxLayout()
        self.pick_task_widget.setLayout(self.pick_task_layout)

        self.board_combo = QComboBox()
        self.list_combo = QComboBox()

        self.pick_task_layout.addWidget(self.board_combo)
        self.pick_task_layout.addWidget(self.list_combo)

        self.name_task_widget = QWidget()
        self.name_task_widget_layout = QHBoxLayout()
        self.name_task_widget.setLayout(self.name_task_widget_layout)

        self.task_name_label = QLabel("Name of Task: ")
        self.task_entry = QLineEdit()

        self.name_task_widget_layout.addWidget(self.task_name_label)
        self.name_task_widget_layout.addWidget(self.task_entry)

        self.task_description_widget = QWidget()
        self.task_description_layout = QVBoxLayout()
        self.task_description_widget.setLayout(self.task_description_layout)

        #self.task_edit_label = QLabel()
        self.task_description_edit = QTextEdit()
        self.task_description_edit.setPlaceholderText("Enter a description of your task.")
        self.task_add_button = QPushButton("Add Task")
        self.task_add_button.clicked.connect(self.add_task)

        #self.task_description_layout.addWidget(self.task_edit_label)
        self.task_description_layout.addWidget(self.task_description_edit)
        self.task_description_layout.addWidget(self.task_add_button)

        self.create_task_widget_layout.addWidget(self.pick_task_widget)
        self.create_task_widget_layout.addWidget(self.name_task_widget)
        self.create_task_widget_layout.addWidget(self.task_description_edit)
        self.create_task_widget_layout.addWidget(self.task_add_button)


        self.middle_layout.addWidget(self.task_card_label)
        self.middle_layout.addWidget(self.task_card)
        self.middle_layout.addWidget(self.task_card_button_widget)
        self.middle_layout.addWidget(self.add_board_widget)
        self.middle_layout.addWidget(self.add_list_widget)
        self.middle_layout.addWidget(self.create_task_widget)






        # right side of the window layout havent figured out what goes here
        self.right_side_widget = QWidget(self)

        self.layout_right = QVBoxLayout()
        self.right_side_widget.setLayout(self.layout_right)
        self.layout_right.addWidget(self.right_side_widget)
        self.right_side_widget.resize(300, 300)







        self.main_layout.addWidget(self.tree_area)
        self.main_layout.addWidget(self.task_card_section)
        # self.main_layout.addWidget(self.right_side_widget)
        
    @pyqtSlot()
    def edit_description(self):
        
        
        self.descr_edit_window = QMainWindow(self)
        self.descr_edit_window.resize(300,300)
        self.descr_edit_window.setWindowTitle("Edit_Discription")
        # self.descr_edit_window.setWindowIcon("447logoicon.png")
        self.descr_edit_widget = QWidget(self.descr_edit_window)
        self.descr_edit_layout = QVBoxLayout()
        self.descr_edit_widget.setLayout(self.descr_edit_layout)
        
        ############################################################
        self.descr_label = QLabel("Edit Task")
        self.descr_label.setAlignment(Qt.AlignCenter)
        self.descr_edit = QTextEdit()
        self.descr_edit.setPlaceholderText("Enter a new description.")
        self.descr_layout_button_accept = QPushButton("Save Task" )
        self.descr_layout_button_accept.clicked.connect(self.accept_edit_window)
        self.descr_layout_button_cancel = QPushButton("Cancel")
        self.descr_layout_button_cancel.clicked.connect(self.cancel_edit_window)
        ############################################################
        self.descr_edit_buttons_widget = QWidget(self.descr_edit_window)
        self.descr_edit_buttons_layout = QHBoxLayout()
        self.descr_edit_buttons_widget.setLayout(self.descr_edit_buttons_layout)
        
        self.descr_edit_buttons_layout.addWidget(self.descr_layout_button_accept)
        self.descr_edit_buttons_layout.addWidget(self.descr_layout_button_cancel)
        ############################################################
        
        self.descr_edit_layout.addWidget(self.descr_label)
        self.descr_edit_layout.addWidget(self.descr_edit)
        self.descr_edit_layout.addWidget(self.descr_edit_buttons_widget)
        
        self.descr_edit_window.setCentralWidget(self.descr_edit_widget)
        
        self.descr_edit_window.show()
        
    
    @pyqtSlot()    
    def get_task_from_tree(self):
        pass
        
    @pyqtSlot()
    def cancel_edit_window(self):
        self.descr_edit_window.close()
        
    @pyqtSlot()
    def accept_edit_window(self):
        #get task id
        #save the new description for the task
        self.descr_edit_window.close()
    
    @pyqtSlot()
    def add_board(self):
        if self.add_board_edit.text() == '':
            print("empty board")
            pass
    
    @pyqtSlot()
    def delete_board(self):
        if self.add_board_edit.text() == '':
            print("empty board")
            pass
    
    @pyqtSlot()
    def add_list(self):
        pass
    
    @pyqtSlot()
    def delete_list(self):
        pass
    
    @pyqtSlot()
    def add_task(self):
        pass
    
    @pyqtSlot()
    def delete_task(self):
        pass
    
    @pyqtSlot()
    def boards_combo(self):
        pass
    
    @pyqtSlot()
    def lists_combo(self):
        pass
    
    @pyqtSlot()
    def update_trello(self):
        pass
    
# Update the tree view with boards
    def updateTreeView(self):
        pass

# Get value for the item being clicked
    def getValueTree(self, val):
        print(val.data())
        print(val.row())
        print(val.column())

# insert boards into tree view
    def insertBoard(self):
        pass

class Documents_Tab(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        
        self.main_layout = QGridLayout()
        self.setLayout(self.main_layout)
        
        
        self.tree_labels = QWidget()
        self.tree_labels_layout = QHBoxLayout()
        self.tree_labels.setLayout(self.tree_labels_layout)
        
        self.documents_tree_label = QLabel("List of Documents for Group:")
        self.documents_tree_label.setAlignment(Qt.AlignRight)
        self.documents_tree_group = QLabel("My Group")
        self.documents_tree_group.setAlignment(Qt.AlignLeft)
        self.tree_labels_layout.addWidget(self.documents_tree_label)
        self.tree_labels_layout.addWidget(self.documents_tree_group)
        
        self.tree_labels_layout.setAlignment(Qt.AlignCenter)

        
        self.documents_tree = QListView()
        #self.documents_tree.setGeometry(30,10,200,400)
        
        self.create_doc_widget = QWidget()
        
        self.create_doc_widget_layout = QVBoxLayout()
        self.create_doc_widget.setLayout(self.create_doc_widget_layout)
        
        self.create_doc_edits_widget = QWidget()
        self.create_doc_edits_widget_layout = QHBoxLayout()
        self.create_doc_edits_widget.setLayout(self.create_doc_edits_widget_layout)
        
        self.create_doc_label = QLabel("Create a Document")
        self.create_doc_label.setAlignment(Qt.AlignCenter)
        self.create_doc_edit = QLineEdit()
        self.create_doc_button = QPushButton("Create")
        
        self.create_doc_edits_widget_layout.addWidget(self.create_doc_edit)
        self.create_doc_edits_widget_layout.addWidget(self.create_doc_button)
        
        self.create_doc_widget_layout.addWidget(self.create_doc_label)
        self.create_doc_widget_layout.addWidget(self.create_doc_edits_widget)
        ###########################################################################
        
        self.share_doc_widget = QWidget()
        
        self.share_doc_widget_layout = QVBoxLayout()
        self.share_doc_widget.setLayout(self.share_doc_widget_layout)
        
        self.share_doc_edits_widget = QWidget()
        self.share_doc_edits_widget_layout = QHBoxLayout()
        self.share_doc_edits_widget.setLayout(self.share_doc_edits_widget_layout)
        
        self.share_doc_label = QLabel("Share a Document")
        self.share_doc_label.setAlignment(Qt.AlignCenter)
        self.share_doc_edit = QLineEdit()
        self.share_doc_button = QPushButton("Share")
        
        self.share_doc_edits_widget_layout.addWidget(self.share_doc_edit)
        self.share_doc_edits_widget_layout.addWidget(self.share_doc_button)
        
        self.share_doc_widget_layout.addWidget(self.share_doc_label)
        self.share_doc_widget_layout.addWidget(self.share_doc_edits_widget)
        ###########################################################################
        self.delete_doc_widget = QWidget()
        self.delete_doc_widget_layout = QVBoxLayout()
        self.delete_doc_widget.setLayout(self.delete_doc_widget_layout)
        
        self.delete_doc_edits_widget = QWidget()
        self.delete_doc_edits_widget_layout = QHBoxLayout()
        self.delete_doc_edits_widget.setLayout(self.delete_doc_edits_widget_layout)
        
        self.delete_doc_label = QLabel("Delete a Document")
        self.delete_doc_label.setAlignment(Qt.AlignCenter)
        self.delete_doc_edit = QLineEdit()
        self.delete_doc_button = QPushButton("Delete")
        
        self.delete_doc_edits_widget_layout.addWidget(self.delete_doc_edit)
        self.delete_doc_edits_widget_layout.addWidget(self.delete_doc_button)
        
        self.delete_doc_widget_layout.addWidget(self.delete_doc_label)
        self.delete_doc_widget_layout.addWidget(self.delete_doc_edits_widget)
        
        self.main_layout.addWidget(self.tree_labels)
        self.main_layout.addWidget(self.documents_tree)
        self.main_layout.addWidget(self.create_doc_widget)
        self.main_layout.addWidget(self.share_doc_widget)
        self.main_layout.addWidget(self.delete_doc_widget)


        

class StandardItem(QStandardItem):
    def __init__(self, txt='', font_size=12, set_bold=False, color=QColor(0, 0, 0)):
        super().__init__()

        fnt = QFont('Open Sans', font_size)
        fnt.setBold(set_bold)

        self.setEditable(False)
        self.setForeground(color)
        self.setFont(fnt)
        self.setText(txt)

        # need to add the mouse event here for right clicking on item
        # and adding the context menu

# Displays the task cards (Name and Description)
class Task_Card_Widget(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        # self.setGeometry(task_card_frame['x'], task_card_frame['y'])




# This is the driver class responsible for running the application
# Default constructor will build the other UIs needed
# To run the application use member function run
class Pinguin(QMainWindow):
    login_signal = pyqtSignal()
    def __init__(self):
        super(Pinguin,self).__init__()
        self.login_signal.connect(self.login_success)
        self.login_menu = Login_Window(self.login_signal)
        self.main_window = Main_Menu()

    @pyqtSlot()
    def login_success(self):
        self.login_menu.hide()
        self.main_window.show()

    def run(self):
        self.login_menu.show()
###############################################################################

def main():
   app = QApplication(sys.argv)
   ui = Pinguin()
   ui.run()
   sys.exit(app.exec_())

if __name__ == '__main__':
   main()
