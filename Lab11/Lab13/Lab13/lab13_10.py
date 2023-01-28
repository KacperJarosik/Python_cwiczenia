# Zadanie: opracować z wykorzystaniem biblioteki tkinter aplikację,
# która wykona konwersję podawanych wartości w stopach na metry.
# współczynnik przeliczania sprawdzić w sieci:
# https://pl.wikipedia.org/wiki/Jednostki_imperialne lub
# https://www.metric-conversions.org/pl/dlugosc/stopy-do-metry.htm

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((0.3048 * value * 10000.0 + 0.5) / 10000.0)
    except ValueError:
        pass


root = Tk()
root.title("Zamiana stóp na metry")
root.iconbitmap('ikona.ico')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

feet = StringVar()
meters = StringVar()

feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=(W, E))

ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=3, sticky=W)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="is equivalent to (jest równa)").grid(column=1, row=2, sticky=E)
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

feet_entry.focus()

root.mainloop()