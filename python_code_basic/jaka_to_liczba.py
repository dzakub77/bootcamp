# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random
from tkinter import *

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nPodaj mi zakres liczb w którym chcesz odgadnąć cyfre.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")


class Apka(Frame):
    def __init__(self, master):
        super(Apka, self).__init__(master)
        self.grid()
        self.ask_number()

    def ask_number(self):
        Label(self, text="Wybierz przedział liczbowy z którego ma być wylosowana liczba").grid(row=0, column=0,
                                                                                               columnspan=2)
        Label(self, text="Dolny przedział: ").grid(row=1, column=0)
        self.min_num = Entry(self)
        self.min_num.grid(row=1, column=1)
        Label(self, text="Górny przedział: ").grid(row=2, column=0)
        self.max_num = Entry(self)
        self.max_num.grid(row=2, column=1)
        Label(self, text="Zgadnij jaka to liczba!").grid(row=3, column=0)
        self.choice = Entry(self)
        self.choice.grid(row=4, column=0)
        self.bt = Button(self, text="Strzelaj!", command=self.asking_number)
        self.bt.grid(row=4, column=1)
        self.txt = Text(self, width=15, height=10)
        self.txt.grid(row=5)

    def asking_number(self):
        max = self.max_num.get()
        min = self.min_num.get()
        the_number = random.randint(int(min), int(max))
        tries = 0
        guess = int(self.choice.get())
        if guess == the_number:
            text = "Brawo! Udało Ci się!"
            text += f" To była {tries} próba"
        else:
            if guess > the_number:
                tries += 1
                text = "Ta liczba jest za duża"
            else:
                text = "Próbuj dalej"
                text += "Ta liczba jest za mała"
                tries += 1
        self.txt.delete(0.0, END)
        self.txt.insert(0.0, text)

root = Tk()
root.title("Jaka to liczba")
root.geometry("600x400")
app = Apka(root)
root.mainloop()

        # while guess != the_number:
        #     guess = int(input("Ta liczba to: "))
        #     tries += 1
        #     if tries > 10:
        #         break
        #     elif guess > the_number:
        #         print("Za duża...")
        #     elif guess < the_number:
        #     p   rint("Za mała...")
        #
        # if tries < 10 and guess == the_number:
        #     print("Odgadłeś! Ta liczba to", the_number)
        #     print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
        # else:
        #     print("Niestety nie udało Ci się odgadnać tej liczby w 10 próbach")

# print(ask_number(20, 25))

# input("\n\nAby zakończyć program, naciśnij klawisz Enter.")
