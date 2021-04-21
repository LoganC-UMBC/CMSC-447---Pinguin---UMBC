# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Groups_Tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.
from collections import deque
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from Database.PinguinDB import PinguinDB


class Ui_Groups_Tab(object):
    def __init__(self,DB,create_group_signal, accept_invite_signal, delete_invite_signal):
        self.DB = DB
        self.create_group_signal = create_group_signal
        self.accept_invite_signal = accept_invite_signal
        self.delete_invite_signal = delete_invite_signal

    def setupUi(self, Groups_Tab):
        Groups_Tab.setObjectName("Groups_Tab")
        Groups_Tab.resize(700, 506)
        Groups_Tab.setMinimumSize(QtCore.QSize(700, 506))
        Groups_Tab.setMaximumSize(QtCore.QSize(700, 506))
        Groups_Tab.setStyleSheet("QWidget#Groups_Tab{\n"
"background-color:rgb(35,35,35);\n"
"}\n"
"\n"
"")
        self.group_view = QtWidgets.QTreeView(Groups_Tab)
        self.group_view.setGeometry(QtCore.QRect(0, 20, 151, 491))
        self.group_view.setStyleSheet("QTreeView{\n"
"border:0;\n"
"background-color:rgb(200,200,200);\n"
"color:rgb(0,0,0);\n"
" border-radius: 5px;\n"
"}")
        self.group_view.setObjectName("group_view")
        """
        self.model = QtCore.QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Groups'])
        self.group_view.header().setDefaultSectionSize(180)
        self.group_view.setModel(self.model)
        self.import_data(self.get_user_groups(self.user_id))
        """

        self.horizontalLayoutWidget = QtWidgets.QWidget(Groups_Tab)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(160, 240, 261, 31))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.create_group_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.create_group_button.setMinimumSize(QtCore.QSize(75, 24))
        self.create_group_button.setMaximumSize(QtCore.QSize(75, 24))
        self.create_group_button.setStyleSheet("QPushButton {\n"
" border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"color:rgb(200,200,200);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(35, 35, 35);\n"
"color: rgb(200, 200, 200);\n"
"}")
        self.create_group_button.setObjectName("create_group_button")
        self.horizontalLayout.addWidget(self.create_group_button)
        self.group_add_description = QtWidgets.QTextEdit(Groups_Tab)
        self.group_add_description.setGeometry(QtCore.QRect(160, 70, 261, 161))
        self.group_add_description.setMinimumSize(QtCore.QSize(261, 161))
        self.group_add_description.setMaximumSize(QtCore.QSize(261, 161))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_add_description.setFont(font)
        self.group_add_description.setStyleSheet("QTextEdit{\n"
"border-radius: 5px;\n"
"background-color:rgb(50,50,50);\n"
"color:rgb(255, 255, 255);\n"
"border:2;\n"
"}")
        self.group_add_description.setObjectName("group_add_description")
        self.horizontalLayoutWidget_3 = QtWidgets.QWidget(Groups_Tab)
        self.horizontalLayoutWidget_3.setGeometry(QtCore.QRect(160, 20, 261, 41))
        self.horizontalLayoutWidget_3.setObjectName("horizontalLayoutWidget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_3)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.group_add_name = QtWidgets.QLineEdit(self.horizontalLayoutWidget_3)
        font = QtGui.QFont()
        font.setPointSize(12)
        self.group_add_name.setFont(font)
        self.group_add_name.setStyleSheet("QLineEdit{\n"
"border-radius: 5px;\n"
"background-color:rgb(50,50,50);\n"
"color:rgb(255, 255, 255);\n"
"border:2;\n"
"}")
        self.group_add_name.setObjectName("group_add_name")
        self.horizontalLayout_3.addWidget(self.group_add_name)
        self.group_description = QtWidgets.QPlainTextEdit(Groups_Tab)
        self.group_description.setGeometry(QtCore.QRect(160, 300, 261, 121))
        self.group_description.setObjectName("group_description")
        self.invite_list = QtWidgets.QListWidget(Groups_Tab)
        self.invite_list.setGeometry(QtCore.QRect(440, 20, 241, 401))
        self.invite_list.setObjectName("invite_list")
        self.widget = QtWidgets.QWidget(Groups_Tab)
        self.widget.setGeometry(QtCore.QRect(443, 430, 221, 42))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.accept_invite_button = QtWidgets.QPushButton(self.widget)
        self.accept_invite_button.setObjectName("accept_invite_button")
        self.horizontalLayout_2.addWidget(self.accept_invite_button)
        self.delete_invite_button = QtWidgets.QPushButton(self.widget)
        self.delete_invite_button.setObjectName("delete_invite_button")
        self.horizontalLayout_2.addWidget(self.delete_invite_button)

        self.create_group_button.clicked.connect(self.create_group)
        self.accept_invite_button.clicked.connect(self.accept_invite)
        self.delete_invite_button.clicked.connect(self.delete_invite)

        self.retranslateUi(Groups_Tab)
        QtCore.QMetaObject.connectSlotsByName(Groups_Tab)

    """
    #https://stackoverflow.com/questions/47102920/pyqt5-how-to-generate-a-qtreeview-from-a-list-of-dictionary-items
    def import_data(self, data, root=None):
        self.model.setRowCount(0)
        if root is None:
            root = self.model.invisibleRootItem()
        seen = {}   # List of  QStandardItem
        values = deque(data)
        while values:
            value = values.popleft()
            if value['unique_id'] == 1:
                parent = root
            else:
                pid = value['parent_id']
                if pid not in seen:
                    values.append(value)
                    continue
                parent = seen[pid]
            unique_id = value['unique_id']
            parent.appendRow([
                QtCore.QStandardItem(value['short_name']),
                QtCore.QStandardItem(value['height']),
                QtCore.QStandardItem(value['weight'])
            ])
            seen[unique_id] = parent.child(parent.rowCount() - 1)

    def get_user_groups(self,user_id):
        groups = self.DB.get_groups()
        user_groups = []

        for group in groups:
            if user_id in group['members']:
                user_groups.append(group)

        return user_groups
    """

    def retranslateUi(self, Groups_Tab):
        _translate = QtCore.QCoreApplication.translate
        Groups_Tab.setWindowTitle(_translate("Groups_Tab", "Groups_Tab"))
        self.create_group_button.setText(_translate("Groups_Tab", "Create Group"))
        self.group_add_description.setHtml(_translate("Groups_Tab", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'Titillium Web\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.group_add_description.setPlaceholderText(_translate("Groups_Tab", "Enter a description for your new group. "))
        self.group_add_name.setPlaceholderText(_translate("Groups_Tab", "Enter your group\'s name..."))
        self.group_description.setPlaceholderText(_translate("Groups_Tab", "Description of selected group."))
        self.accept_invite_button.setText(_translate("Groups_Tab", "Accept Invite"))
        self.delete_invite_button.setText(_translate("Groups_Tab", "Delete Invite"))

    def create_group(self):
        self.create_group_signal.emit()

    def accept_invite(self):
        self.accept_invite_signal.emit()

    def delete_invite(self):
        self.delete_invite_signal.emit()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Groups_Tab = QtWidgets.QWidget()
    ui = Ui_Groups_Tab()
    ui.setupUi(Groups_Tab)
    Groups_Tab.show()
    sys.exit(app.exec_())