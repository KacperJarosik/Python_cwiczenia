from tkinter import *


def do_nothing():
    filewin = Toplevel(root)
    button = Button(filewin, text="Do nothing button")
    button.pack()


root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="New", command=do_nothing)
filemenu.add_command(label="Open", command=do_nothing)
filemenu.add_command(label="Save", command=do_nothing)
filemenu.add_command(label="Save as...", command=do_nothing)
filemenu.add_command(label="Close", command=do_nothing)

filemenu.add_separator()

filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)
editmenu = Menu(menubar, tearoff=0)
editmenu.add_command(label="Undo", command=do_nothing)

editmenu.add_separator()

editmenu.add_command(label="Cut", command=do_nothing)
editmenu.add_command(label="Copy", command=do_nothing)
editmenu.add_command(label="Paste", command=do_nothing)
editmenu.add_command(label="Delete", command=do_nothing)
editmenu.add_command(label="Select All", command=do_nothing)

menubar.add_cascade(label="Edit", menu=editmenu)
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="Help Index", command=do_nothing)
helpmenu.add_command(label="About...", command=do_nothing)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
