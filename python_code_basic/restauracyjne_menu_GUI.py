
from tkinter import *

class Apka(Frame):
    def __init__(self, master):
        super(Apka, self).__init__(master)
        self.grid()
        self.menu()

    def menu(self):
        Label(
            self,
            text="Witamy w restauracji 'BonaVita'!"
        ).grid(row=0, column=3)
        Label(
            self,
            text="Oto nasze Menu: "
        ).grid(row=1, column=2)
        self.danie1 = BooleanVar()
        Checkbutton(
            self,
            text="Pierogi Ruskie - 20zł",
            variable=self.danie1,
            command=self.text
        ).grid(row=2, column=0)
        self.danie2 = BooleanVar()
        Checkbutton(
            self,
            text="Rosół - 10zł",
            variable=self.danie2,
            command=self.text
        ).grid(row=2, column=1)
        self.danie3 = BooleanVar()
        Checkbutton(
            self,
            text="Barszcz Czerwony - 8zł",
            variable=self.danie3,
            command=self.text
        ).grid(row=2, column=2)
        self.danie4 = BooleanVar()
        Checkbutton(
            self,
            text="Zapiekana pierś z kurczaka - 30zł",
            variable=self.danie4,
            command=self.text
        ).grid(row=2, column=3)
        self.danie5 = BooleanVar()
        Checkbutton(
            self,
            text="Żeberka w sosie własnym - 26zł",
            variable=self.danie5,
            command=self.text
        ).grid(row=3, column=0)
        self.danie6 = BooleanVar()
        Checkbutton(
            self,
            text="Piwo - 10zł",
            variable=self.danie6,
            command=self.text
        ).grid(row=3, column=1)
        self.danie7 = BooleanVar()
        Checkbutton(
            self,
            text="Wódka z pieprzem - 5zł",
            variable=self.danie7,
            command = self.text
        ).grid(row=3, column=2)
        self.txt = Text(self, width=15, height=10)
        self.txt.grid(row=5)

    def text(self):
        bill = 0
        napis = ""
        if self.danie1.get():
            napis += "- Pierogi Ruskie\n"
            bill += 20
        if self.danie2.get():
            napis += "- Rosół\n"
            bill += 10
        if self.danie3.get():
            napis += "- Barszcz Czerwony\n"
            bill += 8
        if self.danie4.get():
            napis += "- Zapiekana pierś z kurczaka\n"
            bill += 30
        if self.danie5.get():
            napis += "- Żeberka w sosie własnym\n"
            bill += 26
        if self.danie6.get():
            napis += "- Piwo\n"
            bill += 10
        if self.danie7.get():
            napis += "- Wódka z pieprzem\n"
            bill += 5
        napis += f"Rachunek razem: {bill}"

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, napis)

root = Tk()
root.title("Opowiadanie")
root.geometry("600x400")
app = Apka(root)
root.mainloop()