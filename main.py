from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QInputDialog, QMessageBox
from PyQt5.QtSql import QSqlQuery, QSqlDatabase, QSqlQueryModel
from ui import Ui_Dialog
import sys


class Window(QtWidgets.QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.setWindowIcon(QtGui.QIcon('icon.png'))
        self.connectToDatabase()
        self.load_tasks()
        self.ui.add_button.clicked.connect(self.add_tasks)
        self.ui.remove_button.clicked.connect(self.remove_tasks)
        self.ui.move_button.clicked.connect(self.click_push_button)
        self.ui.listWidget.itemDoubleClicked.connect(self.remove_tasks)
        self.ui.listWidget_2.itemDoubleClicked.connect(self.remove_tasks_2)

    def connectToDatabase(self):
        database = QSqlDatabase.database()
        if not database.isValid():
            database = QSqlDatabase.addDatabase("QSQLITE")
            if not database.isValid():
                logger.error("Cannot add database")
        filename = "tasklist.sqlite3"
        database.setDatabaseName(filename)
        if not database.open():
            logger.error("Cannot open database")

        database.open()
        query = QSqlQuery()
        ok = query.exec \
                (
                """
                CREATE TABLE IF NOT EXISTS task (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name VARCHAR(255) UNIQUE)
                """
            )
        # print("Таблица task создана:", ok)
        ok = query.exec \
                (
                """
                CREATE TABLE IF NOT EXISTS completed_tasks (
                            id INTEGER PRIMARY KEY AUTOINCREMENT UNIQUE,
                            name VARCHAR(255) UNIQUE)
                """
            )
        # print("Таблица completed_tasks создана:", ok)

    def load_tasks(self):
        database = QSqlDatabase.database()
        database.open()
        query = QSqlQuery()
        query.exec("SELECT * FROM task")
        while query.next():
            id = query.value(0)
            text = query.value(1)
            self.ui.listWidget.insertItem(id, text)
        query.exec("SELECT * FROM completed_tasks")
        while query.next():
            id = query.value(0)
            text = query.value(1)
            self.ui.listWidget_2.insertItem(id, text)

    def add_tasks(self):
        query = QSqlQuery()
        current_index = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, 'Новая Задача', 'Задача:')
        if ok and text != '':
            query.prepare("INSERT INTO task (name) values (?)")
            query.addBindValue(text)
            query.exec()
            self.ui.listWidget.insertItem(current_index, text)

    def remove_tasks(self):
        curr_id = self.ui.listWidget.currentRow()
        curr_item = self.ui.listWidget.item(curr_id)
        if curr_item is None:
            return
        question = QMessageBox.question(self, "Убрать задачу", 'Вы точно хотите убрать задачу ' + curr_item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("SELECT id FROM task WHERE name = (?)")
            query.addBindValue(curr_item.text())
            query.exec()
            query.next()
            id = query.value(0)
            query.prepare("DELETE FROM task WHERE id = (?)")
            query.addBindValue(id)
            query.exec()
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.load_tasks()

    def remove_tasks_2(self):
        curr_id = self.ui.listWidget_2.currentRow()
        curr_item = self.ui.listWidget_2.item(curr_id)
        if curr_item is None:
            return
        question = QMessageBox.question(self, "Убрать задачу", 'Вы точно хотите убрать задачу ' + curr_item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            query = QSqlQuery()
            query.prepare("SELECT id FROM completed_tasks WHERE name = (?)")
            query.addBindValue(curr_item.text())
            query.exec()
            query.next()
            id = query.value(0)
            query.prepare("DELETE FROM completed_tasks WHERE id = (?)")
            query.addBindValue(id)
            query.exec()
            self.ui.listWidget.clear()
            self.ui.listWidget_2.clear()
            self.load_tasks()

    def click_push_button(self):
        curr_id = self.ui.listWidget.currentRow()
        curr_item = self.ui.listWidget.item(curr_id)
        if curr_item is None:
            return
        query = QSqlQuery()
        query.prepare("SELECT * FROM task WHERE name = (?)")
        query.addBindValue(curr_item.text())
        query.exec()
        query.next()
        id = query.value(0)
        text = query.value(1)

        query.prepare("INSERT INTO completed_tasks (name) values (?)")
        query.addBindValue(text)
        query.exec()

        query.prepare("DELETE FROM task WHERE id = (?)")
        query.addBindValue(id)
        query.exec()

        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        self.load_tasks()


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
