# Przykład demonstruje użycie klasy w programie wykorzystującym Tkinter
# Zdefiniuj, aby przycisk 3 realizował zamknięcie programu.
# Zamienić widżety dostępne w module tkinter.ttk (nowszym) (Frame i Button)

from tkinter import *
from tkinter import ttk

class Application(Frame):
    """ Aplikacja oparta na GUI z trzema przyciskami. """

    #zdefiniowanie konstrukrora:
    def __init__(self, master):
        """ Inicjalizuj ramkę. """
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        """ Tworzenie trzech przycisków, które nie mają obsługi zdarzeń. """
        # utwórz pierwszy przycisk
        self.bttn1 = Button(self, text = "Brak zdarzenia 1!")
        self.bttn1.grid()

        # utwórz drugi przycisk
        self.bttn2 = Button(self)
        self.bttn2.grid()
        self.bttn2.configure(text = "Brak zdarzenia 2!")

        # utwórz trzeci przycisk
        self.bttn3 = Button(self,command=self.master.destroy)
        self.bttn3.grid()
        self.bttn3["text"] = "Zamknij aplikację!"

# część główna
root = Tk()
root.title("Przyciski")
root.geometry("300x100")
app = Application(root)
root.mainloop()
