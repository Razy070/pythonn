import os
import sys
import time

from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLabel, QLineEdit, QPushButton, QSpinBox


class MainWindow(QWidget):
    def __init__(self, width=640, height=480, title="title"):
        QWidget.__init__(self)
        self.setWindowTitle(title)
        self.resize(width, height)

        self.layout = QGridLayout()
        self.setLayout(self.layout)

        self.label_check = QLabel('Введите расширение файла, доступные(.xlsx,.pptx,.docx)')
        self.layout.addWidget(self.label_check, 0, 0)

        self.line_edit_path = QLineEdit('.docx')
        self.layout.addWidget(self.line_edit_path, 1, 0)

        self.widget = QSpinBox()
        self.widget.setRange(1, 11111)
        self.widget.setSingleStep(1)
        self.layout.addWidget(self.widget, 2, 0)

        self.push_button_create = QPushButton('Создать')
        self.layout.addWidget(self.push_button_create, 3, 0)
        self.push_button_create.clicked.connect(self.create)

        self.show()

    def create(self):
        spin_box_item = self.widget.value()
        input_get_expansion_item = self.line_edit_path.text()
        expansion = [".xlsx", ".pptx", ".docx"]

        def create_files():
            if input_get_expansion_item in expansion:
                for i in range(1, int(spin_box_item) + 1):
                    new_file = open(f"temp/file{i}{input_get_expansion_item}", "w+")
                    new_file.write("Привет, напиши что нибудь")
                    new_file.close()
                    self.label_check.setText("Файлы успешно созданы)")
                    time.sleep(1)
            else:
                self.label_check.setText("Расширени файла введен некоректно")

        if os.path.isdir('temp'):
            create_files()
        else:
            os.mkdir("temp")
            create_files()


app = QApplication(sys.argv)
mw = MainWindow(640, 480, 'My App')
app.exec()
