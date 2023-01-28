# Program demonstruje tworzenie przycisków i wykonywania komend zamykających różne obiekty
# Utwórz w ramce czwarty przycisk, który wyświetli przycisk podobny do przycisku 3
# - do zamykania programu (Tk)
# zamienić widżety dostępne w module tkinter.ttk (nowszym) (Frame i Button)

from tkinter import *
from tkinter import ttk

# utwórz okno główne
root = Tk()
root.title("Przyciski")
root.geometry("200x130")

# utwórz w oknie ramkę do pomieszczenia innych widżetów
app = Frame(root)
app.grid()

# utwórz w ramce przycisk do zamykania okna (Frame)
bttn1 = Button(app, text="1. Zamknij okno !", command=app.destroy)
bttn1.grid()

# utwórz w ramce drugi przycisk do zamykania przycisku (Button)
bttn2 = Button(app)
bttn2.grid()
bttn2.configure(text="2. Zamknij dany przycisk !", command=bttn2.destroy)

# utwórz w ramce trzeci przycisk do zamykania programu (Tk)
bttn3 = Button(app, command=root.destroy)
bttn3.grid()
bttn3["text"] = "3. Zamknij program !"

# utwórz w ramce czwarty przycisk, który wyświetli przycisk podobny do przycisku 3 - do zamykania programu (Tk)
pass
bttn5 = Button(app, text="5. Zamknij program !", command=app.destroy)
bttn4 = Button(app, text="4. Utwórz przycisk !", command=bttn5.grid)
bttn4.grid()

# uruchom pętlę zdarzeń okna głównego
root.mainloop()
