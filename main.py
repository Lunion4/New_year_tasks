from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from untitled import Ui_Dialog
import sys


class window(QtWidgets.QMainWindow):
    def __init__(self):
        super(window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.loadTasks()
        self.ui.add_button.clicked.connect(self.addTasks)
        self.ui.remove_button.clicked.connect(self.removeTasks)
        self.ui.move_button.clicked.connect(self.click_pushButton)

    def loadTasks(self):
        self.ui.listWidget.addItems(['Украсить ёлку', 'Развесить игрушки по дому', 'Приготовить подарки родным'])
        self.ui.listWidget.setCurrentRow(0)

    def addTasks(self):
        currentIndex = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, 'Новая Задача', 'Задача:')
        if ok and text is not None:
            self.ui.listWidget.insertItem(currentIndex, text)

    def removeTasks(self):
        currentIndex = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(currentIndex)
        if item is None:
            return

        question = QMessageBox.question(self, 'Убрать задачу', 'Вы точно хотите убрать задачу' + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.listWidget.takeItem(currentIndex)
            del item

    def click_pushButton(self):
        rows = sorted([index.row() for index in self.ui.listWidget.selectedIndexes()], reverse=True)
        for row in rows:
            self.ui.listWidget_2.addItem(self.ui.listWidget.takeItem(row))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = window()
    win.show()
    sys.exit(app.exec_())
