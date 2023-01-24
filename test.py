from PyQt5 import QtWidgets, QtCore
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import os


class MainWindow(QtWidgets.QWidget):
    def __init__(self, t, parent=None):
        super().__init__(parent)
        self.t = t
        self.build()

    def build(self):
        self.setGeometry(50, 50, 320, 200)
        self.mainLayout = QtWidgets.QVBoxLayout()
        self.setWindowOpacity(0.5)
        self.id = QtWidgets.QLabel(f'имя: текст', self)
        self.mainLayout.addWidget(self.id)
        self.setLayout(self.mainLayout)


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    w = MainWindow(app)
    w.show()
    sys.exit(app.exec_())