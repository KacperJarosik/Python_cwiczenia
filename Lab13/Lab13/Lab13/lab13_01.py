# Elementy GUI tworzy się poprzez konkretyzację obiektów klas z modułu tkinter.
# Jest to programowanie sterowane zdarzeniami
# ----------------------------------------------------
# W programach sterowanych zdarzeniami, wiąże się (kojarzy) zdarzenia,
# które mogą się wydarzyć z procedurami obsługi zdarzeń
# tzn. kodem który jest wykonywany, gdy wystąpi określone zdarzenie.
# Definiując obiekty, zdarzenia i procedury obsługi zdarzeń, ustala się sposób działania programu.
# Następnie uruchamia się program poprzez wejście w pętlę obsługi zdarzeń,
# w której program oczekuje na wystąpienie opisanych zdarzeń.

from tkinter import *
from tkinter import ttk
# ttk to nowsza rodzina widżetów Tk, które zapewniają znacznie lepsze dopasowanie na innych platformach

# W programie wykorzystującym Tkinter występuje tylko jedno okno główne.

# część główna aplikacji - okno główne
root = Tk()
# ustawienie tytułu okna głównego:
root.title("Interfejs GUI 1!")
# rozmiar wyrażony w pikselach:
root.geometry("500x200")
#dodaje ikone pliku
root.iconbitmap('ikona.ico')
# uruchamia pętlę zdarzeń obiektu root:
root.mainloop()
