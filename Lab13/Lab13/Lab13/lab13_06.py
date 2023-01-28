# https://www.tutorialspoint.com/python3/tk_button.htm
# zmodyfikuj program, aby na dole okna pojawiała się informacja, która pobierana jest z pola typu Entry
import tkinter
from tkinter import *
from tkinter import ttk

top = Tk()
L1 = Label(top, text="User Name")
L1.pack(side=LEFT)
E1 = Entry(top, bd=5)
E1.pack(side=RIGHT)
# zmienna_aplikacji=str(E1.get())
# label = Label(top)
# label.pack()
# label.config(text=zmienna_aplikacji)
# Dodać guzk wyświetlający
top.mainloop()