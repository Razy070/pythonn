from flask import Flask
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<p>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the " \
           "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and " \
           "scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap " \
           "into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the " \
           "release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing " \
           "software like Aldus PageMaker including versions of Lorem Ipsum.</p> "


if __name__ == "__main__":
    app.run(threaded=True, port=5000)


# text1 = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the
# industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it
# to make a type specimen book. It has survived not only five centuries, but also the leap into electronic
# typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets
# containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including
# versions of Lorem Ipsum."
#
#
# print(text1)
class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'PyQt5 textbox - pythonspot.com'
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
        QMessageBox.question(self, 'Message - pythonspot.com', "You typed: " + textboxValue, QMessageBox.Ok,
                             QMessageBox.Ok)
        self.textbox.setText("")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

