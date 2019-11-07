import random

number = random.randint(1, 50)
tries = 1
guess = int(input("Zgadnij co to za liczba: "))
while guess != number:
    if guess > number:
        print("Za duża!")
    else:
        print("Za mała!")
    guess = int(input("Zgadnij co to za liczba: "))
    tries += 1

print(f"Brawo! Udało ci się odganąć co to za liczba. Zrobiłeś to za {tries} razem")

input("Jeśli chcesz zakończyć gre, naciśnij enter.")