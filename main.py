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
                            name VARCHAR(255))
                """
            )
        print("Таблица создана:", ok)

    def load_tasks(self):
        database = QSqlDatabase.database()
        database.open()
        query = QSqlQuery()
        query.exec("SELECT * FROM task")
        while query.next():
            id = query.value(0)
            text = query.value(1)
            self.ui.listWidget.insertItem(id, text)

        # self.ui.listWidget.setCurrentRow(0)

    def add_tasks(self):
        database = QSqlDatabase.database()
        database.open()
        query = QSqlQuery()
        current_index = self.ui.listWidget.currentRow()
        text, ok = QInputDialog.getText(self, 'Новая Задача', 'Задача:')
        if ok and text != '':
            ok = query.prepare("INSERT INTO task (name) values (?)")
            query.addBindValue(text)
            ok = query.exec()
            print(f"Задача '{text}' добавлена в БД: {ok}")
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

    def remove_tasks_2(self):
        current_index = self.ui.listWidget_2.currentRow()
        item = self.ui.listWidget_2.item(current_index)
        if item is None:
            return

        question = QMessageBox.question(self, "Убрать задачу", 'Вы точно хотите убрать задачу ' + item.text(),
                                        QMessageBox.Yes | QMessageBox.No)

        if question == QMessageBox.Yes:
            item = self.ui.listWidget_2.takeItem(current_index)
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
