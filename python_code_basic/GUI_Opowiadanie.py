
from tkinter import *

class Apka(Frame):
    def __init__(self, master):
        super(Apka, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(
            self,
            text = "Wprowadź informacje do nowego opowiadania"
        ).grid(row=0, column = 0, columnspan=2, sticky=W)

        self.lbl_os = Label(self, text="Osoba: ").grid(row=1, column=0, columnspan = 2, sticky=W)
        self.en_os = Entry(self)
        self.en_os.grid(row=1, column=1, sticky=W)

        self.lbl_rz = Label(self, text="Rzeczownik w liczbie mnogiej: ").grid(row=2, column=0, sticky=W)
        self.en_rz = Entry(self)
        self.en_rz.grid(row=2, column=1, sticky=W)

        self.lbl_cz = Label(self, text="Czasownik: ").grid(row=3, column=0, columnspan = 2, sticky=W)
        self.en_cz = Entry(self)
        self.en_cz.grid(row=3, column=1, sticky=W)

        self.lbl_prz = Label(self, text="Przymiotnik(i): ").grid(row=4, column=0, columnspan=2, sticky=W)
        self.prz_1 = BooleanVar()
        Checkbutton(
            self,
            text="naglące",
            variable=self.prz_1,
        ).grid(row=4, column=2)
        self.prz_2 = BooleanVar()
        Checkbutton(
            self,
            text="radosne",
            variable=self.prz_2,
        ).grid(row=4, column=3)
        self.prz_3 = BooleanVar()
        Checkbutton(
            self,
            text="ekscytujące",
            variable=self.prz_3,
        ).grid(row=4, column=4)
        self.lbl_cz_c = Label(self, text="Część ciała: ").grid(row=5, column=0, columnspan=2, sticky=W)
        self.cz_c = StringVar()
        self.cz_c.set(None)
        Radiobutton(
            self,
            text="kolano",
            variable=self.cz_c,
            value="kolano.",
        ).grid(row=5, column=2)
        Radiobutton(
            self,
            text="kostkę",
            variable=self.cz_c,
            value="kostę.",
        ).grid(row=5, column=3)
        Radiobutton(
            self,
            text="głowę",
            variable=self.cz_c,
            value="głowę.",
        ).grid(row=5, column=4)
        self.b1 = Button(self, text="Kliknij, aby wyświetlić opowiadanie", command = self.update_text).grid(row=6, column=0, sticky=W)
        self.txt = Text(self, width=50, height=10, wrap=WORD)
        self.txt.grid(row=7)

    def update_text(self):
        person = self.en_os.get()
        verb = self.en_cz.get()
        noun = self.en_rz.get()
        adj = ""
        if self.prz_1.get():
            adj += "naglące, "
        if self.prz_2.get():
            adj += "radosne, "
        if self.prz_3.get():
            adj += "ekscytujące, "
        body_part = self.cz_c.get()

        text = "Sławny badacz i odkrywca "
        text += person
        text += ", o mało co nie zrezygnował z życiowej misji poszukiwania zaginionego miasta, które zamieszkiwały "
        text += noun
        text += ", gdy pewnego dnia "
        text += noun
        text += " znalazły "
        text += person
        text += f". Silne, {adj}osobliwe uczucie owładnęło badaczem. Po tak dlugim czasie poszukiwanie "
        text += f"wreszcie się zakończyło. W oku {person}a pojawiła się łza, która spadła na jego "
        text += f"{body_part}. "
        text += f"A wtedy {noun} szybko pożarły {person}a. Jaku morał płynie z tego opowiadania?"
        text += f"Pomyśl, zanim zaczniesz coś {verb}."


        self.txt.delete(0.0, END)
        self.txt.insert(0.0, text)


root = Tk()
root.title("Opowiadanie")
root.geometry("600x400")
app = Apka(root)
root.mainloop()