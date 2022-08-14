# from PyQt6.QtCore import QDateTime, Qt, QTimer
# from PyQt6.QtWidgets import (QApplication, QCheckBox, QComboBox, QDateTimeEdit,
#         QDial, QDialog, QGridLayout, QGroupBox, QHBoxLayout, QLabel, QLineEdit,
#         QProgressBar, QPushButton, QRadioButton, QScrollBar, QSizePolicy,
#         QSlider, QSpinBox, QStyleFactory, QTableWidget, QTabWidget, QTextEdit,
#         QVBoxLayout, QWidget)
#
#
# class WidgetGallery(QDialog):
#     def __init__(self, parent=None):
#         super(WidgetGallery, self).__init__(parent)
#
#         self.originalPalette = QApplication.palette()
#
#         styleComboBox = QComboBox()
#         styleComboBox.addItems(QStyleFactory.keys())
#
#         styleLabel = QLabel("&Style:")
#         styleLabel.setBuddy(styleComboBox)
#
#         self.useStylePaletteCheckBox = QCheckBox("&Use style's standard palette")
#         self.useStylePaletteCheckBox.setChecked(True)
#
#         disableWidgetsCheckBox = QCheckBox("&Disable widgets")
#
#         self.createTopLeftGroupBox()
#         self.createTopRightGroupBox()
#         self.createBottomLeftTabWidget()
#         self.createBottomRightGroupBox()
#         self.createProgressBar()
#
#         styleComboBox.textActivated.connect(self.changeStyle)
#         self.useStylePaletteCheckBox.toggled.connect(self.changePalette)
#         disableWidgetsCheckBox.toggled.connect(self.topLeftGroupBox.setDisabled)
#         disableWidgetsCheckBox.toggled.connect(self.topRightGroupBox.setDisabled)
#         disableWidgetsCheckBox.toggled.connect(self.bottomLeftTabWidget.setDisabled)
#         disableWidgetsCheckBox.toggled.connect(self.bottomRightGroupBox.setDisabled)
#
#         topLayout = QHBoxLayout()
#         topLayout.addWidget(styleLabel)
#         topLayout.addWidget(styleComboBox)
#         topLayout.addStretch(1)
#         topLayout.addWidget(self.useStylePaletteCheckBox)
#         topLayout.addWidget(disableWidgetsCheckBox)
#
#         mainLayout = QGridLayout()
#         mainLayout.addLayout(topLayout, 0, 0, 1, 2)
#         mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
#         mainLayout.addWidget(self.topRightGroupBox, 1, 1)
#         mainLayout.addWidget(self.bottomLeftTabWidget, 2, 0)
#         mainLayout.addWidget(self.bottomRightGroupBox, 2, 1)
#         mainLayout.addWidget(self.progressBar, 3, 0, 1, 2)
#         mainLayout.setRowStretch(1, 1)
#         mainLayout.setRowStretch(2, 1)
#         mainLayout.setColumnStretch(0, 1)
#         mainLayout.setColumnStretch(1, 1)
#         self.setLayout(mainLayout)
#
#         self.setWindowTitle("Styles")
#         self.changeStyle('Windows')
#
#     def changeStyle(self, styleName):
#         QApplication.setStyle(QStyleFactory.create(styleName))
#         self.changePalette()
#
#     def changePalette(self):
#         if (self.useStylePaletteCheckBox.isChecked()):
#             QApplication.setPalette(QApplication.style().standardPalette())
#         else:
#             QApplication.setPalette(self.originalPalette)
#
#     def advanceProgressBar(self):
#         curVal = self.progressBar.value()
#         maxVal = self.progressBar.maximum()
#         self.progressBar.setValue(curVal + (maxVal - curVal) // 100)
#
#     def createTopLeftGroupBox(self):
#         self.topLeftGroupBox = QGroupBox("Group 1")
#
#         radioButton1 = QRadioButton("Radio button 1")
#         radioButton2 = QRadioButton("Radio button 2")
#         radioButton3 = QRadioButton("Radio button 3")
#         radioButton1.setChecked(True)
#
#         checkBox = QCheckBox("Tri-state check box")
#         checkBox.setTristate(True)
#         checkBox.setCheckState(Qt.CheckState.PartiallyChecked)
#
#         layout = QVBoxLayout()
#         layout.addWidget(radioButton1)
#         layout.addWidget(radioButton2)
#         layout.addWidget(radioButton3)
#         layout.addWidget(checkBox)
#         layout.addStretch(1)
#         self.topLeftGroupBox.setLayout(layout)
#
#     def createTopRightGroupBox(self):
#         self.topRightGroupBox = QGroupBox("Group 2")
#
#         defaultPushButton = QPushButton("Default Push Button")
#         defaultPushButton.setDefault(True)
#
#         togglePushButton = QPushButton("Toggle Push Button")
#         togglePushButton.setCheckable(True)
#         togglePushButton.setChecked(True)
#
#         flatPushButton = QPushButton("Flat Push Button")
#         flatPushButton.setFlat(True)
#
#         layout = QVBoxLayout()
#         layout.addWidget(defaultPushButton)
#         layout.addWidget(togglePushButton)
#         layout.addWidget(flatPushButton)
#         layout.addStretch(1)
#         self.topRightGroupBox.setLayout(layout)
#
#     def createBottomLeftTabWidget(self):
#         self.bottomLeftTabWidget = QTabWidget()
#         self.bottomLeftTabWidget.setSizePolicy(QSizePolicy.Policy.Preferred,
#                 QSizePolicy.Policy.Ignored)
#
#         tab1 = QWidget()
#         tableWidget = QTableWidget(10, 10)
#
#         tab1hbox = QHBoxLayout()
#         tab1hbox.setContentsMargins(5, 5, 5, 5)
#         tab1hbox.addWidget(tableWidget)
#         tab1.setLayout(tab1hbox)
#
#         tab2 = QWidget()
#         textEdit = QTextEdit()
#
#         textEdit.setPlainText("Twinkle, twinkle, little star,\n"
#                               "How I wonder what you are.\n"
#                               "Up above the world so high,\n"
#                               "Like a diamond in the sky.\n"
#                               "Twinkle, twinkle, little star,\n"
#                               "How I wonder what you are!\n")
#
#         tab2hbox = QHBoxLayout()
#         tab2hbox.setContentsMargins(5, 5, 5, 5)
#         tab2hbox.addWidget(textEdit)
#         tab2.setLayout(tab2hbox)
#
#         self.bottomLeftTabWidget.addTab(tab1, "&Table")
#         self.bottomLeftTabWidget.addTab(tab2, "Text &Edit")
#
#     def createBottomRightGroupBox(self):
#         self.bottomRightGroupBox = QGroupBox("Group 3")
#         self.bottomRightGroupBox.setCheckable(True)
#         self.bottomRightGroupBox.setChecked(True)
#
#         lineEdit = QLineEdit('s3cRe7')
#         lineEdit.setEchoMode(QLineEdit.EchoMode.Password)
#
#         spinBox = QSpinBox(self.bottomRightGroupBox)
#         spinBox.setValue(50)
#
#         dateTimeEdit = QDateTimeEdit(self.bottomRightGroupBox)
#         dateTimeEdit.setDateTime(QDateTime.currentDateTime())
#
#         slider = QSlider(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
#         slider.setValue(40)
#
#         scrollBar = QScrollBar(Qt.Orientation.Horizontal, self.bottomRightGroupBox)
#         scrollBar.setValue(60)
#
#         dial = QDial(self.bottomRightGroupBox)
#         dial.setValue(30)
#         dial.setNotchesVisible(True)
#
#         layout = QGridLayout()
#         layout.addWidget(lineEdit, 0, 0, 1, 2)
#         layout.addWidget(spinBox, 1, 0, 1, 2)
#         layout.addWidget(dateTimeEdit, 2, 0, 1, 2)
#         layout.addWidget(slider, 3, 0)
#         layout.addWidget(scrollBar, 4, 0)
#         layout.addWidget(dial, 3, 1, 2, 1)
#         layout.setRowStretch(5, 1)
#         self.bottomRightGroupBox.setLayout(layout)
#
#     def createProgressBar(self):
#         self.progressBar = QProgressBar()
#         self.progressBar.setRange(0, 10000)
#         self.progressBar.setValue(0)
#
#         timer = QTimer(self)
#         timer.timeout.connect(self.advanceProgressBar)
#         timer.start(1000)
#
#
# if __name__ == '__main__':
#
#     import sys
#
#     app = QApplication(sys.argv)
#     gallery = WidgetGallery()
#     gallery.show()
#     sys.exit(app.exec())
#
# 29 lines (24 sloc)  919 Bytes

# class MyTree:
#     def __init__(self, name):
#         self.age = 1
#         self.name = name
#
#     def drow(self, value_): #рост дерева
#         self.age += value_
#
#     @staticmethod
#     def drow_static(value_: float, name: str):
#         age = 1
#         age += value_
#         # tree = {"name": name, "age": age}
#         # return tree
#         return dict(name=name, age=age)
#
# tree1 = MyTree("Дерево1")
# print('возвраст ', tree1.name, "=", tree1.age)
# tree1.drow(2)
# print('возвраст ', tree1.name, "=", tree1.age)
# tree2 = MyTree("Дерево2")
# print('возвраст ', tree2.name, "=", tree2.age)
#
# print(MyTree.drow_static(0, "derevo3")["age"])
#
# #имя дерева: "дерево 3", возвраст дерева: "3"
# tree_dict = MyTree.drow_static(2, "Дерево3")
# print(tree_dict)
# print(f"имя дерева: '{tree_dict['name']}', возвраст дерева:'{tree_dict['age']}'")

# import sys
# import cv2
# import requests
# from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QLabel, QGridLayout, QCheckBox, \
#     QPushButton, QSlider, QComboBox
#
#
#
#
#
# class MainWindow(QWidget):
#     def __init__(self, width, height, title):
#         QWidget.__init__(self)  #
#         self.setWindowTitle(title)  # название титла
#         self.resize(width, height)  # размер окна
#
#         self.image_data = None
#
#         self.layout = QGridLayout()  # экземпляр класса интерфейса grid (сетка)
#         self.setLayout(self.layout)  # глобальная ячейка, вкладываем QGrid в MainWindow(QWidget)
#
#         self.lable_path = QLabel("путь к файлу: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_path, 1, 1)  # вкладываем QLabel в QGridLayout
#
#         self.line_edit_path = QLineEdit("Ali.jpeg")  # экземпляр строки ввода текста
#         self.layout.addWidget(self.line_edit_path, 2, 1)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout
#
#         self.lable_chec = QLabel("Статус: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_chec, 1, 2)  # вкладываем QLabel в QGridLayout
#
#         self.check_box_status = QCheckBox()  # галочка
#         self.check_box_status.setChecked(False)
#         self.layout.addWidget(self.check_box_status, 2, 2)  # ячейка галочка, вкладываем QCheckBox в QGridLayout
#
#         self.push_button_check = QPushButton('Проверить наличие фаила')  # кнопка
#         self.push_button_check.clicked.connect(
#             self.read_and_check_image_in_path)  # запускаем нажатие кнопки функцию changelabeltext
#         # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
#         self.layout.addWidget(self.push_button_check, 2,
#                               3)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout
#         ######################################################################
#         self.lable_widht = QLabel("ширина: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_widht, 3, 1)  # вкладываем QLabel в QGridLayout
#
#         self.lable_height = QLabel("Высота: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_height, 3, 2)  # вкладываем QLabel в QGridLayout
#
#         self.line_edit_widht = QLineEdit("0")  # экземпляр строки ввода текста
#         self.layout.addWidget(self.line_edit_widht, 4, 1)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout
#
#         self.line_edit_height = QLineEdit("0")  # экземпляр строки ввода текста
#         self.layout.addWidget(self.line_edit_height, 4,
#                               2)  # ячейка для ввода текста, вкладываем QLineEdit в QGridLayout
#
#         self.check_box_wb = QCheckBox()  # галочка ч/б
#         self.check_box_wb.setChecked(False)
#         self.layout.addWidget(self.check_box_wb, 5, 1)  # ячейка галочка, вкладываем QCheckBox в QGridLayout
#
#         self.lable_chec_wb = QLabel("Превратить в ч/б: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_chec_wb, 5, 2)  # вкладываем QLabel в QGridLayout
#
#         self.check_box_protect = QCheckBox()  # галочка ч/б
#         self.check_box_protect.setChecked(False)  # ufkjxrf yt frnbdyf
#         self.check_box_protect.stateChanged.connect(self.protect)
#         self.layout.addWidget(self.check_box_protect, 5, 3)  # ячейка галочка, вкладываем QCheckBox в QGridLayout
#
#         self.lable_check_box_protect = QLabel("Подтвердить изменения: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_check_box_protect, 5, 4)  # вкладываем QLabel в QGridLayout
#
#         self.push_button_start = QPushButton('выполнить')  # кнопка
#         self.push_button_start.clicked.connect(self.start)  # запускаем нажатие кнопки функцию changelabeltext
#         self.push_button_start.setEnabled(False)  # кнопка не активна
#         # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
#         self.layout.addWidget(self.push_button_start, 6,
#                               1)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout
#
#         self.push_button_stop = QPushButton('отменить')  # кнопка
#         self.push_button_stop.clicked.connect(self.stop)  # запускаем нажатие кнопки функцию changelabeltext
#         # self.push_button_check.setGeometry(QtCore.QRect(200, 150, 200, 28))
#         self.layout.addWidget(self.push_button_stop, 6,
#                               3)  # ячейка для ввода текста, вкладываем QPushButton в QGridLayout
#
#         self.slider_quality = QSlider()  # ползунок
#         self.slider_quality.setMinimum(1)  # значения слайдера минимум
#         self.slider_quality.setMaximum(100)  # значения слайдера максимум
#         self.slider_quality.setValue(95)  # значения слайдера
#         self.layout.addWidget(self.slider_quality, 4, 5)
#
#         self.lable_slider_quality = QLabel("Выбрать качество: ")  # ячейка для отображения текста
#         self.layout.addWidget(self.lable_slider_quality, 5, 5)  # вкладываем QLabel в QGridLayout
#         ######################################################################
#         self.combo_box_filter = QComboBox() # Для примера список
#         self.combo_box_filter.addItem("гаус")
#         self.combo_box_filter.addItem("фильтр 2")
#         self.combo_box_filter.addItem("фильтр 3")
#         self.combo_box_filter.addItems(["фильтр 4", "фильтр 5", "фильтр 6"])
#         self.layout.addWidget(self.combo_box_filter, 7, 4)
#         #######################################################################
#         self.show()  # метод для отрисовки интерфейса
#
#     def read_and_check_image_in_path(self):
#         value = self.line_edit_path.text()  # путь к файлу
#         print(value)
#         ################################################## #обработка изображения
#         try:
#             # img = cv2.imread(value, cv2.IMREAD_GRAYSCALE) # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR -
#             # цветной
#             img = cv2.imread(value, cv2.IMREAD_COLOR)  # читаем фаил  в сером 0 - серый, 1, cv2.IMREAD_COLOR - цветной
#             # cv2.imshow("Ali_window", img) # открываем окно с именем  volf_window
#             cv2.imshow("Ali_window1", img)  # открываем окно с именем  volf_window
#             cv2.waitKey(1)  # задержка изображения
#         except Exception as error:
#             print(error)
#             img = []
#         cv2.imwrite("Ali2.jpg", img)
#         ###################################################
#         if len(img) > 0:
#             has_file = True
#             print("Изображение успешно прочитано")
#             self.image_data = img
#             height, width = self.image_data.shape[:2]  # читаем изображения с self.image_data (возврощает tuple)
#             self.line_edit_widht.setText(str(width))  # устанавливае значение для line_edit_widht
#             self.line_edit_height.setText(str(height))  # устанавливае значение для line_edit_height
#         else:
#             has_file = False
#             print("Изображение не прочитано")
#             self.line_edit_widht.setText("0")
#             self.line_edit_height.setText("0")
#         self.check_box_status.setChecked(has_file)  # меняем статус check_box_status на True
#         # if has_file:
#         #     self.check_box_status.setChecked(True)  # меняем статус check_box_status на True
#         # else:
#         #     self.check_box_status.setChecked(False) # меняем статус check_box_status на False
#         ########################################################
#         # self.push_button_check.hide() # после нажатия кнопка исчезает
#
#     def start(self):
#         print("start")
#
#         combo = self.combo_box_filter.currentText()
#         print(combo)
#
#         white_black = bool(self.check_box_wb.isChecked())
#         quality = int(self.slider_quality.value())  # Выводит значения слайдера
#         widht = int(self.line_edit_widht.text())
#         height = int(self.line_edit_height.text())
#         image = self.image_data
#
#         if white_black:
#             image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
#             # cv2.equalizeHist(image)
#
#             image = cv2.threshold(image_gray, 127, 255, cv2.THRESH_BINARY)[1]
#
#         # image = cv2.imread(self.line_edit_path.text(), 0)
#         # cv2.imshow('grey scale image', image)
#         image = cv2.resize(image, (widht, height))
#         cv2.imwrite("Ali_new.jpg", image, [cv2.IMWRITE_JPEG_QUALITY, quality])
#
#         pass
#
#     def stop(self):
#         print("stop")
#         pass
#
#     def protect(self):
#         self.push_button_start.setEnabled(self.check_box_protect.isChecked())
#
#
# app = QApplication(sys.argv)
# mw = MainWindow(640, 480, "Image Analyse") # создаем инстанс (экземпляр) класса
# app.exec()

# import time
# from threading import Thread
# import sys
# import requests
# from PySide6.QtWidgets import QWidget, QApplication, QVBoxLayout, QLineEdit, QLabel
# from bs4 import BeautifulSoup
#
# course_dollar = 0.0
# # url = "https://www.google.kz/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D1%83&source=" \
# #       "hp&ei=s5yoYsPlCNKJxc8P7umL-AM&iflsig=AJiK0e8AAAAAYqiqw6EejbrNRRjtPcu562hwQ_7G8qGN&ved=0ahUKEwiDi7KIla34AhXSRPEDHe" \
# #       "70Aj8Q4dUDCAY&uact=5&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%B0%D1%80%D1%83&gs_lcp=Cgdnd3" \
# #       "Mtd2l6EAMyDAgAELEDEAoQRhCCAjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjIECAAQCjoLCAAQgAQQs" \
# #       "QMQgwE6CAgAEIAEELEDOg4ILhCABBCxAxDHARCjAjoOCC4QgAQQsQMQxwEQ0QM6BQguEIAEOgsILhCABBDHARDRAzoFCAAQgAQ6CwgAEIAEELED" \
# #       "EMkDOg0IABCABBCxAxBGEIICOgkIABANEEYQggI6BAgAEA1QAFjFMWDoNmgBcAB4AIABnAGIAcwOkgEEMC4xNZgBAKABAQ&sclient=gws-wiz"
# url = "https://finance.rambler.ru/calculators/converter/1-KZT-USD/"
# params = {}
# response = requests.get(url=url, params=params)
#
#
# def get_course():
#     global course_dollar
#     while True:
#         if response.status_code == 200:
#             value = 400000.60
#             soup = BeautifulSoup(response.text, "lxml")
#             # print(response)
#             # print(response.status_code)
#             # print(soup)
#             # print(type(soup))
#             # data = soup.find_all("input", class_="text") #ищем по классу span и классу текст
#             data = soup.find_all("div", class_="converter-display__cross-block")[0]  # ищем по классу span и классу текст
#             new_data = str(data).split(sep='__value">')[1:]
#             # print(new_data)
#             # print(len(new_data))
#             tenge = tuple(
#                 [
#                     new_data[0].split('</div>\n<div class="converter-display__currency">')[0],
#                     new_data[0].split('</div>\n<div class="converter-display__currency">')[1].split("</div>")[0]
#                 ]
#             )
#             dollar = tuple(
#                 [
#                     new_data[1].split("</div>")[0],
#                     new_data[1].split("</div>")[-3].split('>')[-1]
#                 ]
#             )
#             # print(dollar)
#
#             course = [tenge, dollar]
#             print(course)
#             index = 0
#             for valute in course:
#                 index += 1
#                 print(f'Obekt №{index}: {valute}')
#
#                 if valute[-1] == "USD":
#                     course_dollar = float(valute[0])
#                     result = round(value * float(valute[0]), 3)
#                     # result = round(result, 3) # округления
#                     print(str(result) + " S")
#                     # print(valute[-1])
#             # for i in data:
#             #     print(i)
#             #     print("\n")
#
#             # content = response.content #возврощают в байтах
#             # with open(file="temp/new.html", mode="wb") as file:
#             #     file.write(content)
#             # print(type(content))
#             # data = content.decode(encoding="ISO-8859-1")  #возврощает строку
#             # print(type(data))
#             # print(data)
#             # new_data = data.split("""value=""")
#             # print(len(new_data))
#             # for i in new_data:
#             #     print(i + "\n")
#         else:
#             print("Oshibka polucheniya")
#         # print(response)
#         # print(response.status_code)
#         # print(response.content)
#         time.sleep(5.0)
#         print("Kurs obnovlen")
#
#
# Thread(target=get_course).start()
#
#
#
# from PySide6.QtCore import *
# from PySide6.QtGui import *
#
#
# class MainWindow(QWidget):
#     def __init__(self):
#         QWidget.__init__(self)
#
#         layout = QVBoxLayout()
#         self.setLayout(layout)
#
#         self.line_edit = QLineEdit()
#         layout.addWidget(self.line_edit)
#
#         self.label = QLabel()
#         layout.addWidget(self.label)
#
#         self.line_edit.textChanged.connect(self.line_edit_text_changed)
#
#         self.show()
#
#     def line_edit_text_changed(self, text):
#         try:
#             text = round(course_dollar * float(text), 3)
#             self.label.setText("Ваша сумма: " + str(text) + " $")
#         except Exception as error:
#             self.label.setText('ошибка ввода данных')
#
#
# app = QApplication(sys.argv)
# mw = MainWindow()
#
# try:
#     from PySide6.QtWidgets import QHBoxLayout, QApplication, QFileDialog, QCheckBox, QLineEdit, QPushButton
#     from PySide6.QtCore import Qt, QPoint, QSize, QDir, QThread, Signal
#     from PySide6.QtGui import QIcon
# except:
#     from PyQt5.QtWidgets import QHBoxLayout, QApplication, QFileDialog, QCheckBox, QLineEdit, QPushButton
#     from PyQt5.QtCore import Qt, QPoint, QSize, QDir, QThread
#     from PyQt5.QtGui import QIcon
#     from PyQt5.QtCore import pyqtSignal as Signal
#     from persepolis.gui.addlink_ui import AddLinkWindow_Ui
#     from persepolis.scripts.check_proxy import getProxy
#     from persepolis.scripts import spider
#     from persepolis.scripts import logger
#     from functools import partial
#     import os
#
#
# # find file name and file size
#
#
# class AddLinkSpiderThread(QThread):
#     ADDLINKSPIDERSIGNAL = Signal(dict)
#
#     def __init__(self, add_link_dictionary):
#         QThread.__init__(self)
#         self.add_link_dictionary = add_link_dictionary
#
#     def run(self):
#         try:
#             # get file name and file size
#             file_name, file_size = spider.addLinkSpider(self.add_link_dictionary)
#
#             spider_dict = {'file_size': file_size, 'file_name': file_name}
#
#             # emit results
#             self.ADDLINKSPIDERSIGNAL.emit(spider_dict)
#
#             # write an ERROR in log, If spider couldn't find file_name or file_size.
#             if not(file_name):
#                 logger.sendToLog(
#                     "Spider couldn't find file name", "ERROR")
#             if not(file_size):
#                 logger.sendToLog(
#                     "Spider couldn't find file size", "ERROR")
#         except Exception as e:
#             logger.sendToLog(
#                 "Spider couldn't find download information", "ERROR")
#             logger.sendToLog(
#                 str(e), "ERROR")
#
#
# class AddLinkWindow(AddLinkWindow_Ui):
#     def __init__(self, parent, callback, persepolis_setting, plugin_add_link_dictionary={}):
#         super().__init__(persepolis_setting)
#         self.callback = callback
#         self.plugin_add_link_dictionary = plugin_add_link_dictionary
#         self.persepolis_setting = persepolis_setting
#         self.parent = parent
#
#         # entry initialization
#         # read values from persepolis_setting
#         # connections
#         connections = int(
#             self.persepolis_setting.value('settings/connections'))
#
#         self.connections_spinBox.setValue(connections)
#
#         # download_path
#         download_path = str(
#             self.persepolis_setting.value('settings/download_path'))
#
#         self.download_folder_lineEdit.setText(download_path)
#         self.download_folder_lineEdit.setEnabled(False)
#
#         # enable ok button only if link_lineEdit is not empty!
#         # see linkLineChanged method.
#         self.ok_pushButton.setEnabled(False)
#         self.download_later_pushButton.setEnabled(False)
#         self.link_lineEdit.textChanged.connect(self.linkLineChanged)
#
#         # if browsers plugin didn't send any links
#         # then check clipboard for link!
#         if ('link' in self.plugin_add_link_dictionary.keys()):
#             # check plugin_add_link_dictionary for link!
#             # "link" key-value must be checked
#             self.link_lineEdit.setText(
#                 str(self.plugin_add_link_dictionary['link']))
#
#         else:
#             # check clipboard
#             clipboard = QApplication.clipboard()
#             text = clipboard.text()
#             if (("tp:/" in text[2:6]) or ("tps:/" in text[2:7])):
#                 self.link_lineEdit.setText(str(text))
#
#         # detect_proxy_pushButton
#         self.detect_proxy_pushButton.clicked.connect(
#             self.detectProxy)
#
#         # ip_lineEdit initialization ->
#         settings_ip = self.persepolis_setting.value(
#             'add_link_initialization/ip', None)
#         if (settings_ip):
#             self.ip_lineEdit.setText(str(settings_ip))
#
#         # proxy user lineEdit initialization ->
#         settings_proxy_user = self.persepolis_setting.value(
#             'add_link_initialization/proxy_user', None)
#         if (settings_proxy_user):
#             self.proxy_user_lineEdit.setText(str(settings_proxy_user))
#
#         # port_spinBox initialization ->
#         settings_port = self.persepolis_setting.value(
#             'add_link_initialization/port', 0)
#
#         self.port_spinBox.setValue(int(int(settings_port)))
#
#         # download UserName initialization ->
#         settings_download_user = self.persepolis_setting.value(
#             'add_link_initialization/download_user', None)
#         if (settings_download_user):
#             self.download_user_lineEdit.setText(str(settings_download_user))
#
# # get categories name and add them to add_queue_comboBox
#         categories_list = self.parent.persepolis_db.categoriesList()
#         for queue in categories_list:
#             if queue != 'All Downloads':
#                 self.add_queue_comboBox.addItem(queue)
#
#         self.add_queue_comboBox.setCurrentIndex(0)
#
#         # add_queue_comboBox event
#         self.add_queue_comboBox.currentIndexChanged.connect(self.queueChanged)
#
#         # connect folder_pushButton
#         self.folder_pushButton.clicked.connect(self.changeFolder)
#
#         # connect OK and cancel download_later button ->
#         self.cancel_pushButton.clicked.connect(self.close)
#         self.ok_pushButton.clicked.connect(partial(
#             self.okButtonPressed, download_later=False))
#         self.download_later_pushButton.clicked.connect(
#             partial(self.okButtonPressed, download_later=True))
#
#         # frames and checkBoxes ->
#         self.proxy_frame.setEnabled(False)
#         self.proxy_checkBox.toggled.connect(self.proxyFrame)
#
#         self.download_frame.setEnabled(False)
#         self.download_checkBox.toggled.connect(self.downloadFrame)
#
#         self.limit_frame.setEnabled(False)
#         self.limit_checkBox.toggled.connect(self.limitFrame)
#
#         self.start_frame.setEnabled(False)
#         self.start_checkBox.toggled.connect(self.startFrame)
#
#         self.end_frame.setEnabled(False)
#         self.end_checkBox.toggled.connect(self.endFrame)
#
#         self.change_name_lineEdit.setEnabled(False)
#         self.change_name_checkBox.toggled.connect(self.changeName)
#
#         # set focus to ok button
#         self.ok_pushButton.setFocus()
#
#         # check plugin_add_link_dictionary for finding file name
#         # perhaps plugin sended file name in plugin_add_link_dictionary
#         # for finding file name "out" key must be checked
#         if ('out' in self.plugin_add_link_dictionary.keys()):
#             if self.plugin_add_link_dictionary['out']:
#                 self.change_name_lineEdit.setText(
#                     str(self.plugin_add_link_dictionary['out']))
#                 self.change_name_checkBox.setChecked(True)
#
#         # get referer and header and user_agent and load_cookies in plugin_add_link_dictionary if exits.
#         if ('referer' in self.plugin_add_link_dictionary):
#             self.referer_lineEdit.setText(str(self.plugin_add_link_dictionary['referer']))
#
#         if ('header' in self.plugin_add_link_dictionary):
#             if str(self.plugin_add_link_dictionary['header']) != 'None':
#                 self.header_lineEdit.setText(str(self.plugin_add_link_dictionary['header']))
#
#         if ('user_agent' in self.plugin_add_link_dictionary):
#             self.user_agent_lineEdit.setText(str(self.plugin_add_link_dictionary['user_agent']))
#
#         if ('load_cookies' in self.plugin_add_link_dictionary):
#             self.load_cookies_lineEdit.setText((self.plugin_add_link_dictionary['load_cookies']))
#
#
# # set window size and position
#         size = self.persepolis_setting.value(
#             'AddLinkWindow/size', QSize(520, 425))
#         position = self.persepolis_setting.value(
#             'AddLinkWindow/position', QPoint(300, 300))
#         self.resize(size)
#         self.move(position)
#
#
# # detect system proxy setting, and set ip_lineEdit and port_spinBox
#
#
#     def detectProxy(self, button):
#         # get system proxy information
#         system_proxy_dict = getProxy()
#
#         enable_proxy_frame = False
#
#         # ip
#         if 'http_proxy_ip' in system_proxy_dict.keys():
#             self.ip_lineEdit.setText(str(system_proxy_dict['http_proxy_ip']))
#             enable_proxy_frame = True
#
#         # port
#         if 'http_proxy_port' in system_proxy_dict.keys():
#             self.port_spinBox.setValue(int(system_proxy_dict['http_proxy_port']))
#             enable_proxy_frame = True
#
#         # enable proxy frame if http_proxy_ip or http_proxy_port is valid.
#         if enable_proxy_frame:
#             self.proxy_checkBox.setChecked(True)
#             self.detect_proxy_label.setText('')
#         else:
#             self.proxy_checkBox.setChecked(False)
#             self.detect_proxy_label.setText('No proxy detected!')
#
#
# # active frames if checkBoxes are checked
#     def proxyFrame(self, checkBox):
#
#         if self.proxy_checkBox.isChecked() == True:
#             self.proxy_frame.setEnabled(True)
#         else:
#             self.proxy_frame.setEnabled(False)
#
#     def downloadFrame(self, checkBox):
#
#         if self.download_checkBox.isChecked() == True:
#             self.download_frame.setEnabled(True)
#         else:
#             self.download_frame.setEnabled(False)
#
#     def limitFrame(self, checkBox):
#
#         if self.limit_checkBox.isChecked() == True:
#             self.limit_frame.setEnabled(True)
#         else:
#             self.limit_frame.setEnabled(False)
#
#     def startFrame(self, checkBox):
#
#         if self.start_checkBox.isChecked() == True:
#             self.start_frame.setEnabled(True)
#         else:
#             self.start_frame.setEnabled(False)
#
#     def endFrame(self, checkBox):
#
#         if self.end_checkBox.isChecked() == True:
#             self.end_frame.setEnabled(True)
#         else:
#             self.end_frame.setEnabled(False)
#
#     def changeFolder(self, button):
#         # get download_path from lineEdit
#         download_path = self.download_folder_lineEdit.text()
#
#         # open select folder dialog
#         fname = QFileDialog.getExistingDirectory(
#             self, 'Select a directory', download_path)
#
#         if fname:
#             # Returns pathName with the '/' separators converted to separators that are appropriate for the underlying operating system.
#             # On Windows, toNativeSeparators("c:/winnt/system32") returns
#             # "c:\winnt\system32".
#             fname = QDir.toNativeSeparators(fname)
#
#         if os.path.isdir(fname):
#             self.download_folder_lineEdit.setText(fname)
#
# # enable when link_lineEdit is not empty and find size of file.
#     def linkLineChanged(self, lineEdit):
#         if str(self.link_lineEdit.text()) == '':
#             self.ok_pushButton.setEnabled(False)
#             self.download_later_pushButton.setEnabled(False)
#         else:  # find file size
#
#             dict = {'link': str(self.link_lineEdit.text())}
#
#             # spider is finding file size
#             new_spider = AddLinkSpiderThread(dict)
#             self.parent.threadPool.append(new_spider)
#             self.parent.threadPool[len(self.parent.threadPool) - 1].start()
#             self.parent.threadPool[len(self.parent.threadPool) - 1].ADDLINKSPIDERSIGNAL.connect(
#                 partial(self.parent.addLinkSpiderCallBack, child=self))
#
#             self.ok_pushButton.setEnabled(True)
#             self.download_later_pushButton.setEnabled(True)
#
# # enable change_name_lineEdit if change_name_checkBox is checked.
#     def changeName(self, checkBoxes):
#         if self.change_name_checkBox.isChecked() == True:
#             self.change_name_lineEdit.setEnabled(True)
#         else:
#             self.change_name_lineEdit.setEnabled(False)
#
#     def queueChanged(self, combo):
#         # if one of the queues selected by user , start time and end time must
#         # be deactivated
#         if self.add_queue_comboBox.currentIndex() != 0:
#             self.start_checkBox.setCheckState(Qt.Unchecked)
#             self.start_checkBox.setEnabled(False)
#
#             self.end_checkBox.setCheckState(Qt.Unchecked)
#             self.end_checkBox.setEnabled(False)
#
#         else:
#             self.start_checkBox.setEnabled(True)
#             self.end_checkBox.setEnabled(True)
#
#     def okButtonPressed(self, download_later, button=None):
#         # user submitted information by pressing ok_pushButton, so get information
#         # from AddLinkWindow and return them to the mainwindow with callback!
#
#         # write user's new inputs in persepolis_setting for next time :)
#         self.persepolis_setting.setValue(
#             'add_link_initialization/ip', self.ip_lineEdit.text())
#         self.persepolis_setting.setValue(
#             'add_link_initialization/port', self.port_spinBox.value())
#         self.persepolis_setting.setValue(
#             'add_link_initialization/proxy_user', self.proxy_user_lineEdit.text())
#         self.persepolis_setting.setValue(
#             'add_link_initialization/download_user', self.download_user_lineEdit.text())
#
#         # Check 'Remember path' and change default path if needed
#         if self.folder_checkBox.isChecked() == True:
#             self.persepolis_setting.setValue(
#                 'settings/download_path', self.download_folder_lineEdit.text())
#
#         # get proxy information
#         if not(self.proxy_checkBox.isChecked()):
#             ip = None
#             port = None
#             proxy_user = None
#             proxy_passwd = None
#         else:
#             ip = self.ip_lineEdit.text()
#             if not(ip):
#                 ip = None
#             port = self.port_spinBox.value()
#             if not(port):
#                 port = None
#             proxy_user = self.proxy_user_lineEdit.text()
#             if not(proxy_user):
#                 proxy_user = None
#             proxy_passwd = self.proxy_pass_lineEdit.text()
#             if not(proxy_passwd):
#                 proxy_passwd = None
#
#         # get download username and password information
#         if not(self.download_checkBox.isChecked()):
#             download_user = None
#             download_passwd = None
#         else:
#             download_user = self.download_user_lineEdit.text()
#             if not(download_user):
#                 download_user = None
#             download_passwd = self.download_pass_lineEdit.text()
#             if not(download_passwd):
#                 download_passwd = None
#
#         # check that if user limits download speed.
#         if not(self.limit_checkBox.isChecked()):
#             limit = 0
#         else:
#             if self.limit_comboBox.currentText() == "KiB/s":
#                 limit = str(self.limit_spinBox.value()) + str("K")
#             else:
#                 limit = str(self.limit_spinBox.value()) + str("M")
#
#         # get start time for download if user set that.
#         if not(self.start_checkBox.isChecked()):
#             start_time = None
#         else:
#             start_time = self.start_time_qDataTimeEdit.text()
#
#         # get end time for download if user set that.
#         if not(self.end_checkBox.isChecked()):
#             end_time = None
#         else:
#             end_time = self.end_time_qDateTimeEdit.text()
#
#         # check that if user set new name for download file.
#         if self.change_name_checkBox.isChecked():
#             out = str(self.change_name_lineEdit.text())
#             self.plugin_add_link_dictionary['out'] = out
#         else:
#             out = None
#
#         # get download link
#         link = self.link_lineEdit.text()
#
#         # get number of connections
#         connections = self.connections_spinBox.value()
#
#         # get download_path
#         download_path = self.download_folder_lineEdit.text()
#
#         # referer
#         if self.referer_lineEdit.text() != '':
#             referer = self.referer_lineEdit.text()
#         else:
#             referer = None
#
#         # header
#         if self.header_lineEdit.text() != '':
#             header = self.header_lineEdit.text()
#         else:
#             header = None
#
#         # user_agent
#         if self.user_agent_lineEdit.text() != '':
#             user_agent = self.user_agent_lineEdit.text()
#         else:
#             user_agent = None
#
#         # load_cookies
#         if self.load_cookies_lineEdit.text() != '':
#             load_cookies = self.load_cookies_lineEdit.text()
#         else:
#             load_cookies = None
#         # save information in a dictionary(add_link_dictionary).
#         self.add_link_dictionary = {'referer': referer, 'header': header, 'user_agent': user_agent, 'load_cookies': load_cookies,
#                                     'out': out, 'start_time': start_time, 'end_time': end_time, 'link': link, 'ip': ip,
#                                     'port': port, 'proxy_user': proxy_user, 'proxy_passwd': proxy_passwd,
#                                     'download_user': download_user, 'download_passwd': download_passwd,
#                                     'connections': connections, 'limit_value': limit, 'download_path': download_path}
#
#         # get category of download
#         category = str(self.add_queue_comboBox.currentText())
#
#         del self.plugin_add_link_dictionary
#
#         # return information to mainwindow
#         self.callback(self.add_link_dictionary, download_later, category)
#
#         # close window
#         self.close()
#
#     # close window with ESC key
#     def keyPressEvent(self, event):
#         if event.key() == Qt.Key_Escape:
#             self.close()
#
#
#     # save size and position of window, when user closes the window.
#     def closeEvent(self, event):
#         self.persepolis_setting.setValue('AddLinkWindow/size', self.size())
#         self.persepolis_setting.setValue('AddLinkWindow/position', self.pos())
#         self.persepolis_setting.sync()
#         event.accept()
#
#     def changeIcon(self, icons):
#         icons = ':/' + str(icons) + '/'
#
#         self.folder_pushButton.setIcon(QIcon(icons + 'folder'))
#         self.download_later_pushButton.setIcon(QIcon(icons + 'stop'))
#         self.cancel_pushButton.setIcon(QIcon(icons + 'remove'))
#         self.ok_pushButton.setIcon(QIcon(icons + 'ok'))


