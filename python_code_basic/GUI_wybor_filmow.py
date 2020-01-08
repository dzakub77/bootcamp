
from tkinter import *

class Apka4(Frame):
    def __init__(self, master):
        super(Apka4, self).__init__(master)
        self.grid()
        self.create_widget()

    def create_widget(self):
        Label(self, text="Wybierz swoje ulubione gatunki filmów.").grid(row=0, column=0, columnspan=2, sticky=W)
        Label(self, text="Zaznacz wszystkie, które chciałbyś wybrać:").grid(row=1, column=0, columnspan=2, sticky=W)
        self.likes_comedy = BooleanVar()
        Checkbutton(self, text="Komedia", variable=self.likes_comedy, command=self.update_text).grid(row=2, column=0, sticky=W)
        self.likes_drama = BooleanVar()
        Checkbutton(
            self,
            text="Dramat",
            variable=self.likes_drama,
            command=self.update_text
        ).grid(row=3, column=0, sticky=W)
        self.likes_fantasy = BooleanVar()
        Checkbutton(
            self,
            text="Fantasy",
            variable=self.likes_fantasy,
            command=self.update_text
        ).grid(row=4, column=0, sticky=W)
        self.txt = Text(self, width=50, height=10, wrap=WORD)
        self.txt.grid(row=5, column=0, columnspan=3)

    def update_text(self):
        """Wstawianie do pola tekstowego, gatunki filmów które został wybrane"""
        likes = ""
        if self.likes_fantasy.get():
            likes += "Lubisz filmy Fantasy\n"
        if self.likes_drama.get():
            likes += "Lubisz filmy Dramatyczne\n"
        if self.likes_comedy.get():
            likes += "Lubisz filmy Komediowe"

        self.txt.delete(0.0, END)
        self.txt.insert(0.0, likes)

root = Tk()
root.title("Uluboine filmy")
root.geometry("400x500")
app = Apka4(root)
root.mainloop()