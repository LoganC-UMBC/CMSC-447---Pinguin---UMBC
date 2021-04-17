import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QPushButton, QWidget, QAction, QTabWidget, QVBoxLayout, \
	QGridLayout, QMenuBar, QMenu, QHBoxLayout, QLineEdit
from PyQt5.QtWidgets import QFrame, QLabel, QCheckBox, QTreeView, QTableWidget, QFormLayout, QSpacerItem, QListView, \
	QComboBox, QTextEdit, QCalendarWidget, QDateEdit

from PyQt5.QtGui import QIcon, QDesktopServices, QColor, QFont
from PyQt5.QtCore import pyqtSlot, QSize, Qt, QRect, QMetaObject, pyqtSignal
from PyQt5.Qt import QStandardItemModel, QStandardItem, QSizePolicy

from Database.PinguinDB import PinguinDB

from GUI.Uis.Login_Menu import Ui_Login_Window
from GUI.Uis.Ui_Calendar_Tab.Calendar_Tab import Ui_Calendar_Tab
from GUI.Uis.Ui_Documents_Tab.Documents_Tab import Ui_Documents_Tab
from GUI.Uis.Ui_Forums_Tab.Forums_Tab import Ui_Forums_Tab
from GUI.Uis.Ui_Groups_Tab.Groups_Tab import Ui_Groups_Tab
from GUI.Uis.Ui_Tasks_Tab.Tasks_Tab import Ui_Tasks_Tab

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
	def __init__(self, login_signal):
		super(QMainWindow, self).__init__()
		self.ui = Ui_Login_Window(DB,login_signal)
		self.ui.set_up_ui(self)


# This is the main menu window that appears after login is successful
# The default constructor will setup and instance of a Main Window set with the appropiate tabs
class Main_Menu(QMainWindow):
	def __init__(self):
		super(QMainWindow, self).__init__()

		self.setMaximumSize(MAX_W, MAX_H)
		self.setMinimumSize(MAX_W, MAX_H)

		self.setWindowIcon(QIcon("447logoicon"))
		self.setWindowTitle("Pinguin")
		self.layout = QGridLayout()
		self.tab_widget = Main_TabWidget()
		# self.tab_widget.setTabShape(self.tab_widget.Rounded)

		self.setCentralWidget(self.tab_widget)
		self.setLayout(self.layout)

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

	create_group_signal = pyqtSignal()
	accept_invite_signal = pyqtSignal()
	delete_invite_signal = pyqtSignal()

	def __init__(self):
		super(QWidget, self).__init__()

		self.create_group_signal.connect(self.create_group)
		self.accept_invite_signal.connect(self.accept_invite)
		self.delete_invite_signal.connect(self.delete_invite)

		self.ui = Ui_Groups_Tab(DB,self.create_group_signal,self.accept_invite_signal,self.delete_invite_signal)
		self.ui.setupUi(self)

	@pyqtSlot()
	def create_group(self):
		print("create")

	@pyqtSlot()
	def accept_invite(self):
		print("accept")

	@pyqtSlot()
	def delete_invite(self):
		print("delete")

class Forums_Tab(QWidget):

	send_message_singal = pyqtSignal()

	def __init__(self):
		super(QWidget, self).__init__()

		self.send_message_singal.connect(self.send_message)

		self.ui = Ui_Forums_Tab(DB,self.send_message_singal)
		self.ui.setupUi(self)

	@pyqtSlot()
	def send_message(self):
		print("send message")

class Calendar_Tab(QWidget):

	def __init__(self):
		super(QWidget, self).__init__()
		self.ui = Ui_Calendar_Tab(DB)
		self.ui.setupUi(self)

class Tasks_Tab(QWidget):

	def __init__(self):
		super(QWidget, self).__init__()
		self.ui = Ui_Tasks_Tab(DB)
		self.ui.setupUi(self)

	@pyqtSlot()
	def edit_description(self):

		self.descr_edit_window = QMainWindow(self)
		self.descr_edit_window.resize(300, 300)
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
		self.descr_layout_button_accept = QPushButton("Save Task")
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
		# get task id
		# save the new description for the task
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

	create_doc_signal = pyqtSignal()
	delete_doc_signal = pyqtSignal()
	share_doc_signal = pyqtSignal()

	def __init__(self):
		super(QWidget, self).__init__()

		self.create_doc_signal.connect(self.create_doc)
		self.delete_doc_signal.connect(self.delete_doc)
		self.share_doc_signal.connect(self.share_doc)

		self.ui = Ui_Documents_Tab(DB,self.create_doc_signal, self.delete_doc_signal, self.share_doc_signal)
		self.ui.setupUi(self)

	@pyqtSlot()
	def create_doc(self):
		print("create")

	@pyqtSlot()
	def delete_doc(self):
		print("delete doc")

	@pyqtSlot()
	def share_doc(self):
		print("share doc")

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


# This is the driver class responsible for running the application
# Default constructor will build the other UIs needed
# To run the application use member function run
class Pinguin(QMainWindow):
	login_signal = pyqtSignal()

	def __init__(self):
		super(Pinguin, self).__init__()
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
