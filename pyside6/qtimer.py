import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class StopWatchWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("timer")
        self.setGeometry(100, 100, 300, 200)
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.startWatch = False
        self.label = QLabel(self)
        self.label.setGeometry(100, 40, 150, 70)
        self.start = QPushButton("Start", self)
        self.start.setGeometry(50, 120, 100, 40)
        self.start.pressed.connect(self.Start)


        resetWatch = QPushButton("Reset", self)

        resetWatch.setGeometry(160, 120, 100, 40)

        resetWatch.pressed.connect(self.Reset)

        timer = QTimer(self)

        timer.timeout.connect(self.showCounter)

        timer.start(100)

        self.move(900, 400)

        self.show()

    def showCounter(self):

        if self.startWatch:
            self.counter += 1
            cnt = int((self.counter/10 - int(self.counter/10))*10)
            self.count = '0' + str(cnt)

            if int(self.counter/10) < 10 :
                self.second = '0' + str(int(self.counter / 10))
            else:
                self.second = str(int(self.counter / 10))
                # Set the minute value
                if self.counter / 10 == 60.0 :
                    self.second == '00'
                    self.counter = 0
                    min = int(self.minute) + 1
                    if min < 10 :
                        self.minute = '0' + str(min)
                    else:
                        self.minute = str(min)

        text = self.minute + ':' + self.second + ':' + self.count
        self.label.setText('<h1 style="color:black">' + text + '</h1>')

    def Start(self):

        if self.start.text() == 'Stop':
            self.start.setText('Resume')
            self.startWatch = False
        else:
            self.startWatch = True
            self.start.setText('Stop')


    def Reset(self):
        self.startWatch = False
        self.counter = 0
        self.minute = '00'
        self.second = '00'
        self.count = '00'
        self.label.setText(str(self.counter))


app = QApplication(sys.argv)
stopWt = StopWatchWindow()
app.exec()




