import random


guess = None
correct = random.randrange(1000, 10000)
while guess != correct:
    guess = int(input("Zgadnij jaka to liczba: "))
    if guess > correct:
        print("Za duża!")
    elif guess < correct
        print("Za mała!")
