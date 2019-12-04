# Jaka to liczba?
#
# Komputer wybiera losowo liczbę z zakresu od 1 do 100.
# Gracz próbuje ją odgadnąć, a komputer go informuje,
# czy podana przez niego liczba jest: za duża, za mała,
# prawidłowa.

import random

print("\tWitaj w grze 'Jaka to liczba'!")
print("\nPodaj mi zakres liczb w którym chcesz odgadnąć cyfre.")
print("Spróbuj ją odgadnąć w jak najmniejszej liczbie prób.\n")


def ask_number(low, high):
    the_number = random.randint(low, high)
    guess = None
    tries = 0
    while guess != the_number:
        guess = int(input("Ta liczba to: "))
        tries += 1
        if tries > 10:
            break
        elif guess > the_number:
            print("Za duża...")
        elif guess < the_number:
            print("Za mała...")

    if tries < 10 and guess == the_number:
        print("Odgadłeś! Ta liczba to", the_number)
        print("Do osiągnięcia sukcesu potrzebowałeś tylko", tries, "prób!\n")
    else:
        print("Niestety nie udało Ci się odgadnać tej liczby w 10 próbach")

print(ask_number(20, 25))

input("\n\nAby zakończyć program, naciśnij klawisz Enter.")

