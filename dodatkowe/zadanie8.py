import random
player1 = input("Gracz nr 1: ")
player2 = input("Gracz nr 2: ")
player1g = random.randrange(1, 4)
player2g = random.randrange(1, 4)
print(player2g)
print(player1g)
# 1 kamien              kamien > nozyce     kamien < papier
# 2 nozyce              nozyce > papier     nozyce < kamien
# 3 papier              papier > kamien     papier < nozyce
licznik1 = 0
licznik2 = 0
while True:
    player1g = random.randrange(1, 4)
    player2g = random.randrange(1, 4)
    if player1g == 1 and player2g == 2:
        print(f"Wygrywa {player1}")
        licznik1 += 1
    elif player1g == 1 and player2g == 3:
        print(f"Wygrywa {player2}")
        licznik2 += 1
    elif player1g == 1 and player2g == 1:
        print(f"Remis!")
    elif player1g == 2 and player2g == 1:
        print(f"Wygrywa {player2}")
        licznik2 += 1
    elif player1g == 2 and player2g == 2:
        print(f"Remis!")
    elif player1g == 2 and player2g == 3:
        print(f"Wygrywa {player1}")
        licznik1 += 1
    elif player1g == 3 and player2g == 2:
        print(f"Wygrywa {player2}")
        licznik2 += 1
    elif player1g == 3 and player2g == 3:
        print(f"Remis!")
    elif player1g == 3 and player2g == 1:
        print(f"Wygrywa {player1}")
        licznik1 += 1
    elif player1g == 1 and player2g == 3:
        print(f"Wygrywa {player2}")
        licznik2 += 1
    if licznik1 == 10:
        print(f"I 10 raz wygrywa {player1} ")
        break
    elif licznik2 == 10:
        print(f"I wygrywa {player2}")
        break

print("Koniec gry")