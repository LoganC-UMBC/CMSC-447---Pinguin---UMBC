# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calendar_Tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import pyqtSignal, pyqtSlot
from Database.PinguinDB import PinguinDB

class Ui_Calendar_Tab(object):
    def __init__(self,DB):
        self.DB = DB

    def setupUi(self, Calendar_Tab):
        Calendar_Tab.setObjectName("Calendar_Tab")
        Calendar_Tab.resize(700, 506)
        Calendar_Tab.setMinimumSize(QtCore.QSize(700, 506))
        Calendar_Tab.setMaximumSize(QtCore.QSize(700, 506))
        Calendar_Tab.setStyleSheet("QWidget#Calendar_Tab{background-color: rgb(100,100,100);}")
        self.gridLayout = QtWidgets.QGridLayout(Calendar_Tab)
        self.gridLayout.setObjectName("gridLayout")
        self.widget_2 = QtWidgets.QWidget(Calendar_Tab)
        self.widget_2.setObjectName("widget_2")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_2)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.todays_label = QtWidgets.QLabel(self.widget_2)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.todays_label.setFont(font)
        self.todays_label.setStyleSheet("QLabel#todays_label{color :rgb(244, 244, 244)}")
        self.todays_label.setObjectName("todays_label")
        self.verticalLayout_2.addWidget(self.todays_label, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setMinimumSize(QtCore.QSize(30, 24))
        self.pushButton.setMaximumSize(QtCore.QSize(30, 24))
        self.pushButton.setText("")
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout_2.addWidget(self.pushButton)
        self.todays_events_list = QtWidgets.QListView(self.widget_2)
        self.todays_events_list.setStyleSheet("QListView#todays_events_list{border:0;}\n"
"QListView#todays_events_list{\n"
"border-radius: 5px;  \n"
"background-position: center;  \n"
"background-color: rgb(100,100,100);\n"
"}\n"
"QListView#todays_events_list{\n"
"background-color: rgb(50, 50, 50); \n"
" color: rgb(200, 200, 200);\n"
"}")
        self.todays_events_list.setObjectName("todays_events_list")
        self.verticalLayout_2.addWidget(self.todays_events_list)
        self.gridLayout.addWidget(self.widget_2, 1, 1, 1, 1)
        self.widget = QtWidgets.QWidget(Calendar_Tab)
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.month_label = QtWidgets.QLabel(self.widget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.month_label.setFont(font)
        self.month_label.setStyleSheet("QLabel#month_label{color :rgb(244, 244, 244)}")
        self.month_label.setObjectName("month_label")
        self.verticalLayout.addWidget(self.month_label, 0, QtCore.Qt.AlignHCenter)
        self.month_events_list = QtWidgets.QListView(self.widget)
        self.month_events_list.setStyleSheet("QListView#month_events_list{border:0;}\n"
"QListView#month_events_list{\n"
" border-radius: 5px;  \n"
"background-position: center;  \n"
"background-color: rgb(100,100,100);\n"
"}\n"
"QListView#month_events_list{\n"
"background-color: rgb(100,100,100);\n"
" color: rgb(200, 200, 200);\n"
"}\n"
"QListView#month_events_list{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(200, 200, 200);\n"
"}")
        self.month_events_list.setObjectName("month_events_list")
        self.verticalLayout.addWidget(self.month_events_list)
        self.gridLayout.addWidget(self.widget, 3, 1, 1, 1)
        self.widget_5 = QtWidgets.QWidget(Calendar_Tab)
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.widget_5)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.create_event_label = QtWidgets.QLabel(self.widget_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.create_event_label.setFont(font)
        self.create_event_label.setStyleSheet("QLabel#create_event_label{color :rgb(244, 244, 244)}")
        self.create_event_label.setObjectName("create_event_label")
        self.verticalLayout_3.addWidget(self.create_event_label, 0, QtCore.Qt.AlignHCenter)
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.calendar_edit = QtWidgets.QDateEdit(self.widget_3)
        self.calendar_edit.setStyleSheet("\n"
"QDateEdit#calendar_edit{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(200, 200, 200);\n"
"border:0;\n"
"}")
        self.calendar_edit.setObjectName("calendar_edit")
        self.horizontalLayout.addWidget(self.calendar_edit)
        self.event_name_edit = QtWidgets.QLineEdit(self.widget_3)
        self.event_name_edit.setStyleSheet("QLineEdit#event_name_edit{\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(200, 200, 200);\n"
"border:0;\n"
"}")
        self.event_name_edit.setObjectName("event_name_edit")
        self.horizontalLayout.addWidget(self.event_name_edit)
        self.verticalLayout_3.addWidget(self.widget_3)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.event_edit = QtWidgets.QTextEdit(self.widget_5)
        self.event_edit.setMinimumSize(QtCore.QSize(320, 136))
        self.event_edit.setMaximumSize(QtCore.QSize(320, 136))
        self.event_edit.setStyleSheet("QTextEdit#event_edit{border:0;}\n"
"QTextEdit {\n"
" border-radius: 5px;  \n"
"background-position: center;  \n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QTextEdit {\n"
"background-color: rgb(50, 50, 50); \n"
" color: rgb(200, 200, 200);\n"
"}\n"
"QTextEdit {\n"
"background-color: rgb(50, 50, 50);\n"
"color: rgb(200, 200, 200);\n"
"}")
        self.event_edit.setObjectName("event_edit")
        self.verticalLayout_4.addWidget(self.event_edit)
        self.add_event_button = QtWidgets.QPushButton(self.widget_5)
        self.add_event_button.setStyleSheet("QPushButton {\n"
" border-radius: 5px;  \n"
"background-position: center;  \n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(50, 50, 50); \n"
" color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(35, 35, 35);  \n"
"color: rgb(200, 200, 200);\n"
"}")
        self.add_event_button.setObjectName("add_event_button")
        self.verticalLayout_4.addWidget(self.add_event_button)
        self.gridLayout.addWidget(self.widget_5, 2, 0, 2, 1)
        self.widget_6 = QtWidgets.QWidget(Calendar_Tab)
        self.widget_6.setObjectName("widget_6")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.calendar = QtWidgets.QCalendarWidget(self.widget_6)
        self.calendar.setMinimumSize(QtCore.QSize(0, 0))
        self.calendar.setStyleSheet("QCalendarWidget QWidget#qt_calendar_navigationbar { background-color :rgb(244, 244, 244);selection- }\n"
"QCalendarWidget QAbstractItemView\n"
"{\n"
"background-color :rgb(244, 244, 244)\n"
"}\n"
"QCalendarWidget QToolButton {\n"
"    color: black\n"
"}")
        self.calendar.setObjectName("calendar")
        self.verticalLayout_5.addWidget(self.calendar)
        self.gridLayout.addWidget(self.widget_6, 1, 0, 1, 1)

        self.retranslateUi(Calendar_Tab)
        QtCore.QMetaObject.connectSlotsByName(Calendar_Tab)

    def retranslateUi(self, Calendar_Tab):
        _translate = QtCore.QCoreApplication.translate
        Calendar_Tab.setWindowTitle(_translate("Calendar_Tab", "Calender"))
        self.todays_label.setText(_translate("Calendar_Tab", "Todays  Events"))
        self.month_label.setText(_translate("Calendar_Tab", "This Months Events"))
        self.create_event_label.setText(_translate("Calendar_Tab", "Create A New Event"))
        self.event_name_edit.setPlaceholderText(_translate("Calendar_Tab", "Enter a title for Event"))
        self.event_edit.setPlaceholderText(_translate("Calendar_Tab", "Enter a description of the event"))
        self.add_event_button.setText(_translate("Calendar_Tab", "Add Event"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Calendar_Tab = QtWidgets.QWidget()
    ui = Ui_Calendar_Tab()
    ui.setupUi(Calendar_Tab)
    Calendar_Tab.show()
    sys.exit(app.exec_())
