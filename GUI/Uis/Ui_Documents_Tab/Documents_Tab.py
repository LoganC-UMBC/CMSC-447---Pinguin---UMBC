# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Documents_Tab.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Tasks_Tab(object):
    def setupUi(self, Tasks_Tab):
        Tasks_Tab.setObjectName("Tasks_Tab")
        Tasks_Tab.resize(700, 506)
        Tasks_Tab.setMinimumSize(QtCore.QSize(700, 506))
        Tasks_Tab.setMaximumSize(QtCore.QSize(700, 506))
        Tasks_Tab.setStyleSheet("QWidget#Tasks_Tab{background-color: rgb(100,100,100);}")
        self.widget_4 = QtWidgets.QWidget(Tasks_Tab)
        self.widget_4.setGeometry(QtCore.QRect(0, 300, 701, 156))
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.widget_3 = QtWidgets.QWidget(self.widget_4)
        self.widget_3.setObjectName("widget_3")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget_3)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.create_edit = QtWidgets.QLineEdit(self.widget_3)
        self.create_edit.setMinimumSize(QtCore.QSize(0, 24))
        self.create_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.create_edit.setStyleSheet("QLineEdit{border:0;}\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}")
        self.create_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.create_edit.setObjectName("create_edit")
        self.horizontalLayout_3.addWidget(self.create_edit)
        self.create_button = QtWidgets.QPushButton(self.widget_3)
        self.create_button.setMinimumSize(QtCore.QSize(75, 24))
        self.create_button.setMaximumSize(QtCore.QSize(75, 24))
        self.create_button.setStyleSheet("QPushButton {\n"
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
        self.create_button.setObjectName("create_button")
        self.horizontalLayout_3.addWidget(self.create_button)
        self.create_info_button = QtWidgets.QPushButton(self.widget_3)
        self.create_info_button.setMinimumSize(QtCore.QSize(30, 24))
        self.create_info_button.setMaximumSize(QtCore.QSize(30, 24))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setItalic(False)
        self.create_info_button.setFont(font)
        self.create_info_button.setStyleSheet("QPushButton {\n"
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
        self.create_info_button.setObjectName("create_info_button")
        self.horizontalLayout_3.addWidget(self.create_info_button)
        self.verticalLayout.addWidget(self.widget_3)
        self.widget = QtWidgets.QWidget(self.widget_4)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.share_name_edit = QtWidgets.QLineEdit(self.widget)
        self.share_name_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.share_name_edit.setStyleSheet("QLineEdit{border:0;}\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}")
        self.share_name_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.share_name_edit.setObjectName("share_name_edit")
        self.horizontalLayout.addWidget(self.share_name_edit)
        self.share_link_edit = QtWidgets.QLineEdit(self.widget)
        self.share_link_edit.setMinimumSize(QtCore.QSize(0, 24))
        self.share_link_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.share_link_edit.setStyleSheet("QLineEdit{border:0;}\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}")
        self.share_link_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.share_link_edit.setObjectName("share_link_edit")
        self.horizontalLayout.addWidget(self.share_link_edit)
        self.pushButton_4 = QtWidgets.QPushButton(self.widget)
        self.pushButton_4.setMinimumSize(QtCore.QSize(75, 24))
        self.pushButton_4.setMaximumSize(QtCore.QSize(75, 24))
        self.pushButton_4.setStyleSheet("QPushButton {\n"
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
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.share_help_button = QtWidgets.QPushButton(self.widget)
        self.share_help_button.setMinimumSize(QtCore.QSize(30, 24))
        self.share_help_button.setMaximumSize(QtCore.QSize(30, 24))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setItalic(False)
        self.share_help_button.setFont(font)
        self.share_help_button.setStyleSheet("QPushButton {\n"
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
        self.share_help_button.setObjectName("share_help_button")
        self.horizontalLayout.addWidget(self.share_help_button)
        self.verticalLayout.addWidget(self.widget)
        self.widget_2 = QtWidgets.QWidget(self.widget_4)
        self.widget_2.setObjectName("widget_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.delete_edit = QtWidgets.QLineEdit(self.widget_2)
        self.delete_edit.setMinimumSize(QtCore.QSize(0, 24))
        self.delete_edit.setMaximumSize(QtCore.QSize(16777215, 24))
        self.delete_edit.setStyleSheet("QLineEdit{border:0;}\n"
"QLineEdit{\n"
"border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QLineEdit{\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}")
        self.delete_edit.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.delete_edit.setObjectName("delete_edit")
        self.horizontalLayout_2.addWidget(self.delete_edit)
        self.delete_button = QtWidgets.QPushButton(self.widget_2)
        self.delete_button.setMinimumSize(QtCore.QSize(75, 24))
        self.delete_button.setMaximumSize(QtCore.QSize(75, 24))
        self.delete_button.setStyleSheet("QPushButton {\n"
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
        self.delete_button.setObjectName("delete_button")
        self.horizontalLayout_2.addWidget(self.delete_button)
        self.delete_help_button = QtWidgets.QPushButton(self.widget_2)
        self.delete_help_button.setMinimumSize(QtCore.QSize(30, 24))
        self.delete_help_button.setMaximumSize(QtCore.QSize(30, 24))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setItalic(False)
        self.delete_help_button.setFont(font)
        self.delete_help_button.setStyleSheet("QPushButton {\n"
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
        self.delete_help_button.setObjectName("delete_help_button")
        self.horizontalLayout_2.addWidget(self.delete_help_button)
        self.verticalLayout.addWidget(self.widget_2)
        self.widget_5 = QtWidgets.QWidget(Tasks_Tab)
        self.widget_5.setGeometry(QtCore.QRect(10, 20, 681, 281))
        self.widget_5.setObjectName("widget_5")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.widget_5)
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget_6 = QtWidgets.QWidget(self.widget_5)
        self.widget_6.setObjectName("widget_6")
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.widget_6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.doc_label = QtWidgets.QLabel(self.widget_6)
        font = QtGui.QFont()
        font.setPointSize(13)
        self.doc_label.setFont(font)
        self.doc_label.setStyleSheet("QLabel{color: orange;}")
        self.doc_label.setObjectName("doc_label")
        self.horizontalLayout_4.addWidget(self.doc_label, 0, QtCore.Qt.AlignRight|QtCore.Qt.AlignVCenter)
        self.group_label = QtWidgets.QLabel(self.widget_6)
        self.group_label.setMinimumSize(QtCore.QSize(285, 16))
        self.group_label.setMaximumSize(QtCore.QSize(250, 16777215))
        font = QtGui.QFont()
        font.setPointSize(13)
        self.group_label.setFont(font)
        self.group_label.setStyleSheet("QLabel{color:orange;}")
        self.group_label.setText("")
        self.group_label.setObjectName("group_label")
        self.horizontalLayout_4.addWidget(self.group_label)
        self.verticalLayout_2.addWidget(self.widget_6)
        self.doc_list = QtWidgets.QListWidget(self.widget_5)
        self.doc_list.setStyleSheet("QListWidget{border:0;}\n"
"QListWidget{\n"
"border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"}\n"
"QListWidget{\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}")
        self.doc_list.setObjectName("doc_list")
        self.verticalLayout_2.addWidget(self.doc_list)
        self.doc_help_button = QtWidgets.QPushButton(self.widget_5)
        self.doc_help_button.setMinimumSize(QtCore.QSize(30, 24))
        self.doc_help_button.setMaximumSize(QtCore.QSize(30, 24))
        font = QtGui.QFont()
        font.setFamily("Lucida Bright")
        font.setPointSize(16)
        font.setItalic(False)
        self.doc_help_button.setFont(font)
        self.doc_help_button.setStyleSheet("QPushButton {\n"
" border-radius: 5px;\n"
"background-position: center;\n"
"background-color: rgb(60, 60, 60);\n"
"color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgb(50, 50, 50);\n"
" color: rgb(200, 200, 200);\n"
"}\n"
"QPushButton:pressed {\n"
"background-color: rgb(35, 35, 35);\n"
"color: rgb(200,200,200);\n"
"}")
        self.doc_help_button.setObjectName("doc_help_button")
        self.verticalLayout_2.addWidget(self.doc_help_button, 0, QtCore.Qt.AlignHCenter)

        self.retranslateUi(Tasks_Tab)
        QtCore.QMetaObject.connectSlotsByName(Tasks_Tab)

    def retranslateUi(self, Tasks_Tab):
        _translate = QtCore.QCoreApplication.translate
        Tasks_Tab.setWindowTitle(_translate("Tasks_Tab", "Ui_Tasks_Tab"))
        self.create_edit.setPlaceholderText(_translate("Tasks_Tab", "Title of New Document"))
        self.create_button.setText(_translate("Tasks_Tab", "Create A Doc"))
        self.create_info_button.setText(_translate("Tasks_Tab", "i"))
        self.share_name_edit.setPlaceholderText(_translate("Tasks_Tab", "Name to Save Link By"))
        self.share_link_edit.setPlaceholderText(_translate("Tasks_Tab", "Link you want to save"))
        self.pushButton_4.setText(_translate("Tasks_Tab", "Share Link"))
        self.share_help_button.setText(_translate("Tasks_Tab", "i"))
        self.delete_edit.setPlaceholderText(_translate("Tasks_Tab", "Name of the document"))
        self.delete_button.setText(_translate("Tasks_Tab", "Delete A Doc"))
        self.delete_help_button.setText(_translate("Tasks_Tab", "i"))
        self.doc_label.setText(_translate("Tasks_Tab", "Viewing Documents for Group:"))
        self.doc_help_button.setText(_translate("Tasks_Tab", "i"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Tasks_Tab = QtWidgets.QWidget()
    ui = Ui_Tasks_Tab()
    ui.setupUi(Tasks_Tab)
    Tasks_Tab.show()
    sys.exit(app.exec_())
