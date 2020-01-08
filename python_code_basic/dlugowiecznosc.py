
from tkinter import *

class Apka3(Frame):
    def __init__(self, master):
        super(Apka3, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        self.lbl1 = Label(self, text= "Podaj hasło do sekretu długowieczności")
        self.lbl1.grid(row = 0, column = 0, columnspan = 2, sticky = W)
        self.lbl2 = Label(self, text= "Hasło: ")
        self.lbl2.grid(row = 1, column = 0, sticky = W)
        self.ent1 = Entry(self)
        self.ent1.grid(row = 1, column = 1, columnspan = 2)
        self.bt1 = Button(self, text = "Wprowadź", command = self.reveal) # ustawiam uaktywnienie przycisku wprowadz
        self.bt1.grid(row = 2, column = 0, sticky = W)
        self.txt1 = Text(self, width = 35, height = 5, wrap = WORD)
        self.txt1.grid(row=3, column=0, columnspan = 2, rowspan = 2, sticky=W)

    def reveal(self):
        """Wyświetl komunikat który zależy od poprawności hasła"""
        contents = self.ent1.get()
        if contents == "sekret":
            message = """Udało Ci się, zdobywasz tajemny przepis na długowieczność: XXX"""
        else:
            message = """Niestety to hasło jest nie poprawne i nie mogę zdradzić Ci sekretu na 
            długowieczność."""
        self.txt1.delete(0.0, END)
        self.txt1.insert(0.0, message)

root = Tk()
root.title("asdasda")
root.geometry("300x210")
app = Apka3(root)
root.mainloop()