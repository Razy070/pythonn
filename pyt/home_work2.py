from tkinter import *
from tkinter import ttk

def nazmy():
    print("се работает хорошо")

root = Tk()

frm = ttk.Frame(root, padding=100)
root.title("Таймер с интерфейсом на Python")
root.geometry("640x480")
frm.grid()

Button(text="это кнопка",  # текст кнопки
       background="#555",  # фоновый цвет кнопки
       foreground="#ccc",  # цвет текста
       padx="20",  # отступ от границ до содержимого по горизонтали
       pady="8",  # отступ от границ до содержимого по вертикали
       font="16",  # высота шрифта

       ).grid(column=2, row=1)




