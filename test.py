# from PyQt5 import QtWidgets, QtCore
# from PyQt5.Qt import *
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# import os
#
#
# class MainWindow(QtWidgets.QWidget):
#     def __init__(self, t, parent=None):
#         super().__init__(parent)
#         self.t = t
#         self.build()
#
#     def build(self):
#         self.setGeometry(50, 50, 320, 200)
#         self.mainLayout = QtWidgets.QVBoxLayout()
#         self.setWindowOpacity(0.5)
#         self.id = QtWidgets.QLabel(f'имя: текст', self)
#         self.mainLayout.addWidget(self.id)
#         self.setLayout(self.mainLayout)
#
#     def create_db(self):
#         global query
#         db = QSqlDatabase.addDatabase("QSQLITE")
#         db.setDatabaseName("bbb.sqlite")
#         query = QSqlQuery()
#         query.exec \
#                 (
#                 """
#                     CREATE TABLE IF NOT EXISTS testiks (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#                         name VARCHAR(255))
#                 """
#             )
#         db.commit()
#         db.close()
#
#
#
# def connectToDatabase():
#     global query
#     database = QSqlDatabase.database()
#     if not database.isValid():
#         database = QSqlDatabase.addDatabase("QSQLITE")
#         if not database.isValid():
#             logger.error("Cannot add database")
#     filename = "ccc.sqlite3"
#     database.setDatabaseName(filename)
#     if not database.open():
#         logger.error("Cannot open database")
#
#     database.open()
#     query = QSqlQuery()
#     query.exec \
#             (
#             """
#             CREATE TABLE IF NOT EXISTS cTest (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#                         name VARCHAR(255))
#             """
#         )
#     query.exec("INSERT INTO cTest(name) values('rabotaet?')")
# def createTable():
#     database = QSqlDatabase.database()
#     database.open()
#     query = QSqlQuery()
#     query.exec\
#         (
#             """
#             CREATE TABLE IF NOT EXISTS cTest (
#                         id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
#                         name VARCHAR(255))
#             """
#         )
#     query.exec("INSERT INTO cTest(name) values('NeUra')")
#
#
# if __name__ == "__main__":
#     import sys
#     connectToDatabase()
#     #createTable()
#     app = QApplication(sys.argv)
#     w = MainWindow(app)
#     w.show()
#     sys.exit(app.exec_())

import sys

from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class SuperPlayer(QGraphicsView):
    def __init__(self):
        super().__init__(self)

        self.gv = QGraphicsView()
        self.mp = QMediaPlayer()  # Передаёт поток на gvi
        self.gs = QGraphicsScene()  # Передаёт поток на gv

        # Передаёт поток на gs, с надстройкой о игнорировании
        # прозрачности родительских классов дочерними
        self.gvi = QGraphicsVideoItem()

        self.gvi.setMediaObject()
        self.gs.addItem()
        self.gv.setScene()
        self.mp.setVideoOutput()
        self.gvi.setOpacity()
        self.gvi.ItemIgnoresParentOpacity(True)

        # Думал переслать видео поток на него
        # self.vw = QVideoWidget()
        # self.vw.setWindowOpacity()
        # self.vw.showFullScreen()

        self.mp.setMedia(QMediaContent(QUrl.fromLocalFile("background.gif")))
        self.gv.showFullScreen()
        self.mp.play()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    view = SuperPlayer()
    view.show()

    sys.exit(app.exec_())

