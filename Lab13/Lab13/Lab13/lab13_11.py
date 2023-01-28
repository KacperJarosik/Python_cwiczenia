# Zadanie: opracować z wykorzystaniem biblioteki tkinter aplikację,
# która wykona obliczenia współczynnika BMI (body mass index)
# współczynnik przeliczania BMI zprawdzić w sieci:
# https://pl.wikipedia.org/wiki/Wska%C5%BAnik_masy_cia%C5%82a
# Aplikacja ma podawać zarówno wartość tego współczynnika jak również informację o nadwadze,
# wadze prawidłowej, niedowadze itd.
# Wygląd aplikacji podany w pliku lab13.pdf

from tkinter import *
from tkinter import ttk

def calculate(*args):
    try:
        value1 = float(wzrost_cm.get())
        value2 = float(waga_kg.get())
        BMI.set((value2/(value1*value1*0.01*0.01)))
        x =value2/(value1*value1*0.01*0.01)
        ttk.Label(mainframe, text="Klasyfikacja:").grid(column=1, row=4, sticky=W)
        if x <16.0:
            ttk.Label(mainframe, text="wygłodzenie").grid(column=2, row=4, sticky=W)
        elif x < 17.0:
            ttk.Label(mainframe, text="wychudzenie").grid(column=2, row=4, sticky=W)
        elif x < 18.5:
            ttk.Label(mainframe, text="niedowaga").grid(column=2, row=4, sticky=W)
        elif x < 25.0:
            ttk.Label(mainframe, text="waga w normie").grid(column=2, row=4, sticky=W)
        elif x < 30.0:
            ttk.Label(mainframe, text="nadwaga").grid(column=2, row=4, sticky=W)
        elif x < 35.0:
            ttk.Label(mainframe, text="otyłość 1. st.").grid(column=2, row=4, sticky=W)
        elif x < 40.0:
            ttk.Label(mainframe, text="otyłość 2. st.").grid(column=2, row=4, sticky=W)
        else:
            ttk.Label(mainframe, text="otyłość 3. st.").grid(column=2, row=4, sticky=W)
    except ValueError:
        pass


root = Tk()
root.title("Obliczanie BMI")
root.iconbitmap('ikona.ico')
mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(N, W, E, S))
mainframe.columnconfigure(0, weight=1)
mainframe.rowconfigure(0, weight=1)

wzrost_cm = StringVar()
waga_kg = StringVar()
BMI = StringVar()

wzrost_cm_entry = ttk.Entry(mainframe, width=7, textvariable=wzrost_cm)
wzrost_cm_entry.grid(column=2, row=1, sticky=(W, E))

waga_kg_entry = ttk.Entry(mainframe, width=7, textvariable=waga_kg)
waga_kg_entry.grid(column=2, row=2, sticky=(W, E))

ttk.Label(mainframe, textvariable=BMI).grid(column=2, row=3, sticky=(W, E))
ttk.Button(mainframe, text="Calculate", command=calculate).grid(column=3, row=4, sticky=W)

ttk.Label(mainframe, text="wzrost cm").grid(column=3, row=1, sticky=W)
ttk.Label(mainframe, text="waga kg").grid(column=3, row=2, sticky=W)
ttk.Label(mainframe, text="Twój wynik").grid(column=1, row=3, sticky=E)
ttk.Label(mainframe, text="BMI").grid(column=3, row=3, sticky=W)

wzrost_cm_entry.focus()

root.mainloop()