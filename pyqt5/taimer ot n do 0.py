import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget, \
    QLCDNumber, QGridLayout, QSpinBox, QAbstractSpinBox
from PyQt5.QtCore import QTimer, Qt


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.lcd = QLCDNumber()
        self.button = QPushButton("Start")
        self.button.clicked.connect(self.timerStart)
        self.buttonReset = QPushButton("Reset")
        self.buttonReset.clicked.connect(self.timerReset)
        self.spinBox = QSpinBox()
        self.spinBox.setButtonSymbols(QAbstractSpinBox.PlusMinus)
        self.spinBox.setMaximum(222)
        self.spinBox.setSingleStep(1)
        self.spinBox.setProperty("value", 7)
        self.spinBox.setWrapping(True)
        self.spinBox.setAlignment(Qt.AlignRight)

        layout = QGridLayout()
        layout.addWidget(self.lcd, 0, 0, 1, 2)
        layout.addWidget(self.spinBox, 1, 0, 1, 2)
        layout.addWidget(self.button, 2, 0)
        layout.addWidget(self.buttonReset, 2, 1)
        self.setLayout(layout)

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.showTime)
        self.timer.setInterval(1000)  # 1 sec
        self.time = 0

    def showTime(self):
        self.lcd.display(self.time)
        self.time -= 1  # !!!
        if self.time < 0:
            self.timer.stop()
            self.button.setText("Start")
            self.time = 0

    def timerStart(self):
        if self.button.text() == "Start":
            if not self.time: self.time = self.spinBox.value()
            self.timer.start()
            self.button.setText("Stop")
        else:
            self.timer.stop()
            self.button.setText("Start")

    def timerReset(self):
        self.timer.stop()
        self.button.setText("Start")
        self.time = 0
        self.lcd.display(self.time)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = Window()
    window.resize(300, 150)
    window.show()
    sys.exit(app.exec_())










