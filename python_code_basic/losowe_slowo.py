import random

words = ('komputer', 'myszka', 'ekran', 'ladowarka', 'klawiatura', 'bateria', 'internet')
word = random.choice(words)
j = 0
for i in word:
    j += 1

print(f"Wylosowane słowo ma {j} liter. Masz pięć prób!")
tries = 0
while tries != 6:
    guess = input("Zgadnij co to za słowo: ")
    if guess == word:
        print("Brawo, to jest to słowo")
        break
    else:
        print("Próbuj dalej!")
    tries += 1
    if tries == 5:
        print("Niestety nie udało Ci się. To słowo to: ", word)

input("Jeśli chcesz zakończyć gre, naciśnij enter.")

