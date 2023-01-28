# Dołożyć przycisk do zamknięcia aplikacji
# zamienić widżety dostępne w module tkinter.ttk (nowszym) (Frame i Button)

from tkinter import *
from tkinter import ttk
from tkinter import messagebox

top = Tk()
top.geometry("150x100")


def helloCallBack():
    msg = ttk.messagebox.showinfo("Hello Python", "Hello World")


bttn1 = ttk.Button(top, text="Hello", command=helloCallBack)
bttn1.place(x=50, y=50)

bttn2 = ttk.Button(top, text="Close", command=top.destroy)
bttn2.place(x=0, y=0)
top.mainloop()
