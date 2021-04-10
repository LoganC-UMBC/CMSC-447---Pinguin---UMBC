import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QGridLayout, QMenuBar, QMenu, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QFrame, QLabel, QCheckBox, QTreeView, QTableWidget, QFormLayout, QSpacerItem, QListView, QComboBox, QTextEdit, QCalendarWidget, QDateEdit


from PyQt5.QtGui import QIcon, QDesktopServices, QColor, QFont
from PyQt5.QtCore import pyqtSlot, QSize, Qt, QRect, QMetaObject
from PyQt5.Qt import QStandardItemModel, QStandardItem, QSizePolicy

from Login_Menu import Ui_Login_Window
MAX_W = 1024
MAX_H = 768

# This is the login window that will appear first when the application is started.
# We need two line edit objects and two push buttons .
# The push buttons will be to login with the input(user and pass) from the two line edits
# and to let the user create an account.
# We need to add some graphics and maybe a help menu button.
# Send a pop up to the user if the login is wrong 
# When the login is successful the main menu should appear and the login window should hide
class Login_Window(QMainWindow):
    def __init__(self):
        super(QMainWindow, self).__init__()
        self.ui = Ui_Login_Window()
        self.ui.set_up_ui(self)
        
        



# This is the main menu window that appears after login is successful
# The default constructor will setup and instance of a Main Window set with the appropiate tabs
class Main_Menu(QMainWindow):
    def __init__(self):
        super(QMainWindow,self).__init__()
        
        self.setMaximumSize(MAX_W, MAX_H)
        self.setMinimumSize(MAX_W, MAX_H)
        
        self.setWindowIcon(QIcon("447logoicon"))
        
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
        
        self.groups_tab = Groups_Tab()
        self.calendar_tab = Calendar_Tab()
        self.forums_tab = Forums_Tab()
        self.tasks_tab = Tasks_Tab()
        
        self.addTab(self.groups_tab, "Groups")
        self.addTab(self.forums_tab, "Forums")
        self.addTab(self.calendar_tab, "Calendar")
        self.addTab(self.tasks_tab, "Tasks")
        
        
        

# Each tab needed to be deisgned to hold the appropiate widgets
class Groups_Tab(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        
        # Main layout
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)
        
        ################################################
        # left section holds tree view of groups
        ################################################
        self.left_groups_widget = QWidget()
        self.left_groups_widget_layout = QVBoxLayout()
        self.left_groups_widget.setLayout(self.left_groups_widget_layout)
        
        # Tree view object to see Groups and users in the group
        self.groups_tree = QTreeView()
        
        self.groups_tree.setHeaderHidden(True)
        self.tree_model = QStandardItemModel()
        self.rootNode = self.tree_model.invisibleRootItem()
        # This would initially populate the list view with items 
        #self.updateTreeView()
        self.groups_tree.setModel(self.tree_model)
        self.groups_tree.expandAll()
        self.groups_tree.clicked.connect(self.getValueTree)
        
        self.left_groups_widget_layout.addWidget(self.groups_tree)
        
        
        
        ################################################
        # mid section still debating on how to set up 
        ################################################
        self.middle_groups_widget = QWidget()
        self.middle_groups_widget_layout = QVBoxLayout()
        self.middle_groups_widget.setLayout(self.middle_groups_widget_layout)
        
        self.group_view_widget = QWidget()
        self.group_view_widget_layout = QVBoxLayout()
        self.group_view_widget.setLayout(self.group_view_widget_layout)
        
        self.group_description = QListView()
        # self.group_description.setMaximumSize(200,200)
        
        self.group_view_widget_layout.addWidget(self.group_description)
        
        
        self.middle_groups_widget_layout.addWidget(self.group_view_widget)
        
        
        ################################################
        # right section still don't know what to put here
        ################################################
        self.right_groups_widget = QWidget()
        self.right_groups_layout = QVBoxLayout()
        self.right_groups_widget.setLayout(self.right_groups_layout)
        
        self.groups_buttons = QWidget()
        self.groups_buttons_layout = QVBoxLayout()
        self.groups_buttons.setLayout(self.groups_buttons_layout)
        
        self.create_groups_button = QPushButton("Create Group")
        self.add_to_groups_button = QPushButton("Add to Group")
        self.delete_groups_button = QPushButton("Delete Group")
        
        self.groups_buttons_layout.addWidget(self.create_groups_button)
        self.groups_buttons_layout.addWidget(self.add_to_groups_button)
        self.groups_buttons_layout.addWidget(self.delete_groups_button)
        
        self.right_groups_layout.addWidget(self.groups_buttons)

        
        
        
        ################################################
        # Add everything to the main layout
        ################################################
        self.main_layout.addWidget(self.left_groups_widget)
        self.main_layout.addWidget(self.middle_groups_widget)
        self.main_layout.addWidget(self.right_groups_widget)
        
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
        #self.group_pick_view.setGeometry(0,0,256,607)
        
        self.left_forums_widget_layout.addWidget(self.group_pick_view)
        
        
        self.right_forums_widget = QWidget()
        self.right_forums_layout = QVBoxLayout()
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
        self.left_layout.addWidget(treeView)
        
        
        # middle portion of the task tab
        self.task_card_section = QWidget()
        self.middle_layout = QVBoxLayout()
        self.task_card_section.setLayout(self.middle_layout)
        
        self.task_card_button_widget = QWidget(self.task_card_section)
        self.task_card_button_set = QHBoxLayout()
        self.task_card_button_widget.setLayout(self.task_card_button_set)
        
        self.task_card = QTableWidget()
        self.task_card.setGeometry(266, 0, 256, 303.5)
        self.delete_task_button = QPushButton("Delete Card")
        self.edit_task_button = QPushButton("Edit Description")
        
        self.task_card_button_set.addWidget(self.edit_task_button)
        self.task_card_button_set.addWidget(self.delete_task_button)
        
        
        self.create_task_widget = QWidget()
        self.create_task_widget_layout = QVBoxLayout()
        self.create_task_widget.setLayout(self.create_task_widget_layout)
        
        
        self.pick_task_widget = QWidget()#self.create_task_widget
        self.pick_task_layout = QHBoxLayout()
        self.pick_task_widget.setLayout(self.pick_task_layout)
        
        self.board_combo = QComboBox()
        self.list_combo = QComboBox()
        
        self.pick_task_layout.addWidget(self.board_combo)
        self.pick_task_layout.addWidget(self.board_combo)
        
        self.name_task_widget = QWidget()
        self.name_task_widget_layout = QHBoxLayout()
        self.name_task_widget.setLayout(self.name_task_widget_layout)
        
        self.task_name_label = QLabel()
        self.task_entry = QLineEdit()
        
        self.name_task_widget_layout.addWidget(self.task_name_label)
        self.name_task_widget_layout.addWidget(self.task_entry)
        
        self.task_description_widget = QWidget()
        self.task_description_layout = QVBoxLayout()
        self.task_description_widget.setLayout(self.task_description_layout)
        
        self.task_edit_label = QLabel()
        self.task_description_edit = QTextEdit()
        self.task_add_button = QPushButton("Add Task")
        
        self.task_description_layout.addWidget(self.task_edit_label)
        self.task_description_layout.addWidget(self.task_description_edit)
        self.task_description_layout.addWidget(self.task_add_button)
        
        self.create_task_widget_layout.addWidget(self.pick_task_widget)
        self.create_task_widget_layout.addWidget(self.name_task_widget)
        self.create_task_widget_layout.addWidget(self.task_description_edit)
        
        
        
        self.middle_layout.addWidget(self.task_card)
        self.middle_layout.addWidget(self.task_card_button_widget)
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
class Pinguin():
    
    def __init__(self):
        self.login_menu = Login_Window()
        self.main_window = Main_Menu()
        
        

    def run(self):
        #self.login_menu.show()
        self.main_window.show()
###############################################################################  

def main():
   app = QApplication(sys.argv)
   ui = Pinguin()
   ui.run()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()