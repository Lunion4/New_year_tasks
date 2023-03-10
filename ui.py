# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QMovie, QFont
from PyQt5.QtWidgets import QGraphicsOpacityEffect, QSystemTrayIcon, QStyle, QMenu, QAction, qApp, QApplication
import sys


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Horror Tasks")
        Dialog.setFixedSize(702, 584)
        self.centralwidget = QtWidgets.QWidget(Dialog)
        self.centralwidget.setObjectName("main-widget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 1920, 1080))
        self.label.setMinimumSize(QtCore.QSize(800, 600))
        self.label.setMaximumSize(QtCore.QSize(800, 600))
        self.label.setObjectName("lb1")
        self.label.setFont(QFont('Times', 15))
        Dialog.setCentralWidget(self.centralwidget)
        self.movie = QMovie("background.gif")
        self.label.setMovie(self.movie)
        self.startAnimation()
        self.listWidget = QtWidgets.QListWidget(Dialog)
        self.listWidget.setFont(QFont('Times', 11))
        self.listWidget.setStyleSheet("QListWidget"
                            "{"
                            "border : 1px solid grey;"
                            "background : transparent;"
                            "color: LightSeaGreen;"
                            "padding: 0 3px;"
                            "}")
        self.listWidget.setGeometry(QtCore.QRect(30, 130, 271, 341))
        self.listWidget.setObjectName("listWidget")
        self.listWidget_2 = QtWidgets.QListWidget(Dialog)
        self.listWidget_2.setFont(QFont('Times', 11))
        # self.opacity_effect_2 = QGraphicsOpacityEffect()
        # self.opacity_effect_2.setOpacity(0.1)
        # self.listWidget_2.setGraphicsEffect(self.opacity_effect_2) #?? ??????????: ???????????? 6 ?????????? 1 ??????????(background : transparent;)
        self.listWidget_2.setStyleSheet("QListWidget"
                                      "{"
                                      "border : 1px solid grey;"
                                      "background : transparent;"
                                      "color: LightSeaGreen;"
                                      "}")
        self.listWidget_2.setGeometry(QtCore.QRect(390, 130, 271, 341))
        self.listWidget_2.setObjectName("listWidget_2")
        self.good = QtWidgets.QLabel(Dialog)
        self.good.setGeometry(QtCore.QRect(480, 60, 211, 101))
        self.good.setObjectName("good")
        self.bad = QtWidgets.QLabel(Dialog)
        self.bad.setGeometry(QtCore.QRect(100, 60, 161, 91))
        self.bad.setObjectName("bad")
        self.widget = QtWidgets.QWidget(Dialog)
        self.widget.setGeometry(QtCore.QRect(300, 0, 91, 121))
        self.widget.setObjectName("widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.add_button = QtWidgets.QPushButton(self.widget)
        self.add_button.setFont(QFont('Times', 11))
        self.add_button.setStyleSheet("QPushButton {"
                                      "background: transparent;"
                                      "border-style: inset;"
                                      "border : 1px solid LightSeaGreen;"
                                      "color: LightSeaGreen"
                                      "}"
                                      "QPushButton:pressed {"
                                      "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #97b7f7, stop: 1 #b0deff);"
                                      "border-style: inset;"
                                      "}"
                                      )
        self.add_button.setObjectName("add_button")
        self.verticalLayout.addWidget(self.add_button)
        self.move_button = QtWidgets.QPushButton(self.widget)
        self.move_button.setFont(QFont('Times', 11))
        self.move_button.setObjectName("move_button")
        self.verticalLayout.addWidget(self.move_button)
        self.move_button.setStyleSheet("QPushButton {"
                                       "background: transparent;"
                                       "border-style: inset;"
                                       "border : 1px solid LightSeaGreen;"
                                       "color: LightSeaGreen"
                                       "}"
                                       "QPushButton:pressed {"
                                       "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #97b7f7, stop: 1 #b0deff);"
                                       "border-style: inset;"
                                       "}"
                                       )
        self.remove_button = QtWidgets.QPushButton(self.widget)
        self.remove_button.setFont(QFont('Times', 11))
        self.remove_button.setObjectName("remove_button")
        self.verticalLayout.addWidget(self.remove_button)
        self.remove_button.setStyleSheet("QPushButton {"
                                       "background: transparent;"
                                       "border-style: inset;"
                                       "border : 1px solid LightSeaGreen;"
                                       "color: LightSeaGreen"
                                       "}"
                                       "QPushButton:pressed {"
                                       "background-color: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1,stop: 0 #97b7f7, stop: 1 #b0deff);"
                                       "border-style: inset;"
                                       "}"
                                       )

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


        self.tray_icon = QSystemTrayIcon(Dialog)
        self.tray_icon.setIcon(Dialog.style().standardIcon(QStyle.SP_ComputerIcon))
        show_action = QAction("Show", Dialog)
        quit_action = QAction("Exit", Dialog)
        hide_action = QAction("Hide", Dialog)
        show_action.triggered.connect(Dialog.show)
        hide_action.triggered.connect(Dialog.hide)
        quit_action.triggered.connect(qApp.quit)
        tray_menu = QMenu()
        tray_menu.addAction(show_action)
        tray_menu.addAction(hide_action)
        tray_menu.addAction(quit_action)
        self.tray_icon.setContextMenu(tray_menu)
        self.tray_icon.show()


    def close(self):
        self.tray_icon.showMessage("Tray Program", "Application was minimized to Tray", QSystemTrayIcon.Information,
                                   2000)




    def startAnimation(self):
        self.movie.start()
    #def stopAnimation(self):
        #self.movie.stop()
    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Horror | Tasks"))
        self.good.setText(_translate("Dialog", "?????????????????????? ????????????"))
        self.bad.setText(_translate("Dialog", "???????????????? ????????????"))
        self.add_button.setText(_translate("Dialog", "????????????????"))
        self.remove_button.setText(_translate("Dialog", "??????????????"))
        self.move_button.setText(_translate("Dialog", "C??????????????"))