# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'todoUI.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(438, 631)
        MainWindow.setStyleSheet(u"")
        MainWindow.setTabShape(QTabWidget.Rounded)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"QWidget {\n"
"  background-color: #fff;\n"
"}\n"
"QListWidget{\n"
"	\n"
"	font: 75 14pt \"Verdana\";\n"
"\n"
"}\n"
"QListWidget::item:selected{\n"
"	\n"
"	background-color: rgba(62, 123, 185, 180);\n"
"	border-radius: 8px;\n"
"}\n"
"\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit {\n"
"  border-radius: 8px;\n"
"  border: 1px solid #e0e4e7;\n"
"  padding: 5px 15px;\n"
"}\n"
"QLineEdit::placeholder {\n"
"  color: #767e89;\n"
"}\n"
"\n"
"\n"
"\n"
"QPushButton {\n"
"	font: 87 8pt \"Arial Black\";\n"
"  background-color: #0d6efd;\n"
"  color: #fff;\n"
"  font-weight: 600;\n"
"  border-radius: 8px;\n"
"  border: 1px solid #0d6efd;\n"
"  padding: 15px 15px;\n"
"  margin-top: 2px;\n"
"  outline: 0px;\n"
"}\n"
"\n"
"")
        self.gridLayout = QGridLayout(self.centralwidget)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(15, 15, 15, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(12)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.listWidget = QListWidget(self.centralwidget)
        QListWidgetItem(self.listWidget)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setFrameShape(QFrame.NoFrame)
        self.listWidget.setFrameShadow(QFrame.Raised)

        self.verticalLayout.addWidget(self.listWidget)

        self.newtaskedit = QLineEdit(self.centralwidget)
        self.newtaskedit.setObjectName(u"newtaskedit")

        self.verticalLayout.addWidget(self.newtaskedit)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.add_btn = QPushButton(self.centralwidget)
        self.add_btn.setObjectName(u"add_btn")

        self.horizontalLayout.addWidget(self.add_btn)

        self.del_btn = QPushButton(self.centralwidget)
        self.del_btn.setObjectName(u"del_btn")

        self.horizontalLayout.addWidget(self.del_btn)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))

        __sortingEnabled = self.listWidget.isSortingEnabled()
        self.listWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.listWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("MainWindow", u"fsdf", None));
        self.listWidget.setSortingEnabled(__sortingEnabled)

        self.newtaskedit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"New Task", None))
        self.add_btn.setText(QCoreApplication.translate("MainWindow", u"Add Task", None))
        self.del_btn.setText(QCoreApplication.translate("MainWindow", u"Delete", None))
    # retranslateUi

