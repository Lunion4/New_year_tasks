from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from ui import Ui_Dialog
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))

        self.load_tasks()
        self.ui.add_button.clicked.connect(self.add_tasks)
        self.ui.remove_button.clicked.connect(self.remove_tasks)
        self.ui.move_button.clicked.connect(self.click_push_button)

    def load_tasks(self):
        self.ui.listWidget.addItems(['Украсить ёлку', 'Развесить игрушки по дому', 'Приготовить подарки родным'])
        self.ui.listWidget.setCurrentRow(0)

    def add_tasks(self):
        current_index = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, 'Новая Задача', 'Задача:')
        if ok and text is not None:
            self.ui.listWidget.insertItem(current_index, text)

    def remove_tasks(self):
        current_index = self.ui.listWidget.currentRow()
        item = self.ui.listWidget.item(current_index)
        if item is None:
            return

        question = QMessageBox.question(self, "Убрать задачу", 'Вы точно хотите убрать задачу ' + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.listWidget.takeItem(current_index)
            del item

    def click_push_button(self):
        rows = sorted([index.row() for index in self.ui.listWidget.selectedIndexes()], reverse=True)
        for row in rows:
            self.ui.listWidget_2.addItem(self.ui.listWidget.takeItem(row))


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
