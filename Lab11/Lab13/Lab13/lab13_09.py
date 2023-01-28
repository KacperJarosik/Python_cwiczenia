# zmodyfikuj program tak, aby na dole pojawiała się informacja,
# które z pól są zaznaczone lub nie (korzystając z poprzedniego zadania)
# Wygląd aplikacji podany w pliku lab13.pdf

from tkinter import *

import tkinter

def sel():
    if CheckVar1.get()==1 and CheckVar2.get()==0:
        selection = "You selected the option Music"
        label.config(text=selection)
    if CheckVar1.get()==1 and CheckVar2.get()==1:
        selection = "You selected the option Music and Video"
        label.config(text=selection)
    if CheckVar1.get()==0 and CheckVar2.get()==1:
        selection = "You selected the option Video"
        label.config(text=selection)
    if CheckVar1.get()==0 and CheckVar2.get()==0:
        selection = "You selected the option -"
        label.config(text=selection)


top = Tk()
CheckVar1 = IntVar()
CheckVar2 = IntVar()
C1 = Checkbutton(top, text="Music", variable=CheckVar1, onvalue=1, offvalue=0, height=5, width=20,command=sel)
C2 = Checkbutton(top, text="Video", variable=CheckVar2, onvalue=1, offvalue=0, height=5, width=20,command=sel)
C1.pack()
C2.pack()
label = Label(top)
label.pack()

top.mainloop()
