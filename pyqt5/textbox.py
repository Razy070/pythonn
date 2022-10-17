import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot
import psycopg2

conn = psycopg2.connect(dbname='new_db', user='postgres', password='R29062011Z', host='localhost')
cursor = conn.cursor()
cursor.execute("""
SELECT * FROM public.books
ORDER BY id ASC, title ASC, author ASC, price ASC, "pageCounts" ASC 
""")
records = cursor.fetchall()
print(records)
print(type(records))

...
cursor.close()
conn.close()


class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt6'
        self.left = 10
        self.top = 10
        self.width = 400
        self.height = 140
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create textbox
        self.textbox = QLineEdit(self)
        self.textbox.move(20, 20)
        self.textbox.resize(280, 40)

        # Create a button in the window
        self.button = QPushButton('Show text', self)
        self.button.move(20, 80)

        # connect button to function on_click
        self.button.clicked.connect(self.on_click)
        self.show()

    @pyqtSlot()
    def on_click(self):
        textboxValue = self.textbox.text()
        # print(textboxValue)
        self.textbox.setText("")
        # for i in range(1, textboxValue):
        #     print(i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
