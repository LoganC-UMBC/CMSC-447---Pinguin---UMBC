import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
	QGridLayout, QMenuBar, QMenu, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QFrame, QLabel, QCheckBox, QTreeView, QTableWidget, QFormLayout, QSpacerItem, QListView, \
	QComboBox, QTextEdit, QCalendarWidget, QDateEdit

from PyQt5.QtGui import QIcon, QDesktopServices, QColor, QFont
from PyQt5.QtCore import pyqtSlot, QSize, Qt, QRect, QMetaObject, pyqtSignal
from PyQt5.Qt import QStandardItemModel, QStandardItem, QSizePolicy

from Application.GUI.main_window import Main_Window
from Application.GUI.login_window import Ui_Login_Window
from Application.Database.PinguinDB import PinguinDB
from Application.Functions.trello_api.task_card import Trello
from Application.Functions.google_client import *
from pydrive.auth import GoogleAuth


MAX_W = 700
MAX_H = 515

DB = PinguinDB()


# This is the login window that will appear first when the application is started.
# We need two line edit objects and two push buttons .
# The push buttons will be to login with the input(user and pass) from the two line edits
# and to let the user create an account.
# We need to add some graphics and maybe a help menu button.
# Send a pop up to the user if the login is wrong
# When the login is successful the main menu should appear and the login window should hide
class Login_Window(QMainWindow):
	def __init__(self, login_signal, db, trello):
		super(QMainWindow, self).__init__()
		self.ui = Ui_Login_Window(login_signal, db, trello)
		self.ui.set_up_ui(self)


# This is the main menu window that appears after login is successful
# The default constructor will setup and instance of a Main Window set with the appropiate tabs
class Main_Menu(QMainWindow):
	def __init__(self, db, trello, google):
		super(QMainWindow, self).__init__()
		self.ui = Main_Window(db, trello, google)
		self.ui.setupUi(self)




# This is the driver class responsible for running the application
# Default constructor will build the other UIs needed
# To run the application use member function run
class Pinguin(QMainWindow):
	login_signal = pyqtSignal()

	def __init__(self):
		super().__init__()
		self.db = DB
		self.trello = Trello()
		self.auth = None
		self.google_client = None
		self.login_signal.connect(self.login_success)
		self.login_menu = Login_Window(self.login_signal, self.db, self.trello)
		self.main_window = Main_Menu(self.db, self.trello, self.google_client)

	@pyqtSlot()
	def login_success(self):
		self.login_menu.hide()
		if self.trello.client == None:
			print(self.db.user.user_id)
			self.trello.action_setup2(self.db.user.user_id)

		self.auth = GoogleAuth()
		# Try to load saved client credentials
		self.auth.LoadCredentialsFile("Credentials.json")

		if self.auth.credentials is None:
			print("no creds")
			# Authenticate if they're not there
			self.auth.LocalWebserverAuth()

		elif self.auth.access_token_expired:
			print("creds expired")
			# Refresh them if expired
			self.auth.Refresh()

			print("creds renewed")

		else:
			print("new creds")
			# Initialize the saved creds
			self.auth.Authorize()
		# Save the current credentials to a file
		self.auth.SaveCredentialsFile("Credentials.json")

		self.main_window.ui.google_client = GoogleClient(self.auth)
		print("heresdasd")
		self.main_window.ui.widgets_refresh()
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
