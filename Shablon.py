#Шаблон из 11 урока (18 декабря)

import sys
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLCDNumber, QVBoxLayout
class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Планировшик задач на Новый Год")
        self.resize(200, 200)
        self.lcd = QLCDNumber(self)
        self.vbox = QVBoxLayout()
        self.button1 = QPushButton('Нажми меня', self)
        self.button2 = QPushButton('Сбросить', self)
        self.counter = 0
        self.initUI()

    def initUI(self):
        self.SetStructure()
        self.button1.clicked.connect(self.WasClicked)
        self.button2.clicked.connect(self.WasClicked)
        self.show()

    def SetStructure(self):
        self.vbox.addWidget(self.lcd)
        self.vbox.addWidget(self.button1)
        self.vbox.addWidget(self.button2)
        self.setLayout(self.vbox)

    def WasClicked(self):
        sender = self.sender()

        if sender.text() == 'Нажми меня':
            self.counter += 1
            self.button2.setText('Сбросить')
        elif sender.text() == 'Сбросить':
            self.counter = 0
            self.button2.setText('Нажми меня')

        self.lcd.display(self.counter)

    def keyPressEvent(self, event):

        if event.key() == Qt.Key_Escape:
            self.close()
        elif event.key() == Qt.Key_1:
            self.counter += 1

        self.lcd.display(self.counter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())