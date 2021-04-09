import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget,QVBoxLayout, QGridLayout, QMenuBar, QMenu, QHBoxLayout, QLineEdit, QFrame
from PyQt5.QtGui import QIcon, QDesktopServices, QColor
from PyQt5.QtCore import pyqtSlot, QSize, Qt

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
        super(QMainWindow,self).__init__()
        
        self.setMinimumSize(QSize(500, 700))
        self.setMaximumSize(QSize(500, 700))
        
        self.setWindowIcon(QIcon("447logoicon"))
        
        self.login_widget = QWidget(self)
        
        
        self.entry_area = QVBoxLayout(self)
        
        
        self.passEdit = QLineEdit()
        self.userEdit = QLineEdit()
        
        self.entry_area.addWidget(self.userEdit)
        self.entry_area.addWidget(self.passEdit)
        
        self.login_button = QPushButton("Login")
        self.new_user_button = QPushButton("New User")
        
        
        
        #self.layout.addWidget(self.entry_area)
        self.setLayout(self.contents)



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
        
class Forums_Tab(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        
class Calendar_Tab(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        
class Tasks_Tab(QWidget):
    
    def __init__(self):
        super(QWidget, self).__init__()
        self.layout = QHBoxLayout()
        self.setLayout(self.layout)
        
        
# This is the driver class responsible for running the application
# Default constructor will build the other UIs needed
# The run application will run the first instance of the login menu after 
# a successful login the main menu should appear
class Pinguin():
    
    def __init__(self):
        self.login_menu = Login_Window()
        self.main_window = Main_Menu()
        
        

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