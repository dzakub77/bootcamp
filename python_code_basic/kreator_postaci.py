"""
Witaj w Kreatorze Postaci.
Na początek otrzymujesz pule 30 pkt. które, możesz spożytkać na cztery atrybuty.
Siła, Zdrowie, Mądrość, Zręczność.
"""

strenght = 0
health = 0
intelligence = 0
dexterity = 0
points = 30
x = None
"""
Masz możliwość przyznania pkt. do dowolnego atrybuty, a także możliwość odebrania pkt. i przekazania
ich spowrotem do puli.
"""
while x != 0:

    print(f"Menu opcji: \
    \n1 - Siła {strenght} \
    \n2 - Zdrowie {health} \
    \n3 - Mądrość {intelligence}\
    \n4 - Zręczność {dexterity}\
    \n0 - Zakończ grę"
    )
    x = int(input("Wybierz opcję od 1 do 4 i naciśnij enter: "))

    if x == 1:
        print("Atrybut Siły: ")
        print("1 - dodaj pkt.")
        print("2 - odejmij pkt.")
        print("3 - powrót do głównego menu opcji")
        y = int(input("Co chcesz z nim zrobić? "))
        if y == 1:
            dodanie = int(input(f"Pozostało {points} pkt, ile chcesz dodać do siły? "))
            strenght += dodanie
            points -= dodanie
            print("Twoja siła: ",strenght)
            print("Pozosta pula pkt: ",points)
        if y == 2:
            odejmij = int(input(f"W tej chwili posiadasz {strenght} pkt siły. Ile chcesz odjąć? "))
            strenght -= odejmij
            points += odejmij
            print("Twoja siła: ",strenght)
            print("Pozosta pula pkt: ", points)
        if y == 3:
            print()
    if x == 2:
        print("Atrybut Zdrowia: ")
        print("1 - dodaj pkt.")
        print("2 - odejmij pkt.")
        print("3 - powrót do głównego menu opcji")
        y = int(input("Co chcesz z nim zrobić? "))
        if y == 1:
            dodanie = int(input(f"Pozostało {points} pkt, ile chcesz dodać do zdrowia? "))
            health += dodanie
            points -= dodanie
            print("Twoje zdrowie: ",health)
            print("Pozosta pula pkt: ",points)
        if y == 2:
            odejmij = int(input(f"W tej chwili posiadasz {health} pkt zdrowia. Ile chcesz odjąć? "))
            health -= odejmij
            points += odejmij
            print("Twoja zdrowia: ",health)
            print("Pozosta pula pkt: ", points)
        if y == 3:
            print()
    if x == 3:
        print("Atrybut Mądrość: ")
        print("1 - dodaj pkt.")
        print("2 - odejmij pkt.")
        print("3 - powrót do głównego menu opcji")
        y = int(input("Co chcesz z nim zrobić? "))
        if y == 1:
            dodanie = int(input(f"Pozostało {points} pkt, ile chcesz dodać do mądrości? "))
            intelligence += dodanie
            points -= dodanie
            print("Twoja mądrość: ",intelligence)
            print("Pozosta pula pkt: ",points)
        if y == 2:
            odejmij = int(input(f"W tej chwili posiadasz {intelligence} pkt mądrości. Ile chcesz odjąć? "))
            intelligence -= odejmij
            points += odejmij
            print("Twoja mądrość: ",intelligence)
            print("Pozosta pula pkt: ", points)
        if y == 3:
            print()
    if x == 4:
        print("Atrybut Zręczność: ")
        print("1 - dodaj pkt.")
        print("2 - odejmij pkt.")
        print("3 - powrót do głównego menu opcji")
        y = int(input("Co chcesz z nim zrobić? "))
        if y == 1:
            dodanie = int(input(f"Pozostało {points} pkt, ile chcesz dodać do zręczności? "))
            dexterity += dodanie
            points -= dodanie
            print("Twoja zręczność: ",dexterity)
            print("Pozosta pula pkt: ",points)
        if y == 2:
            odejmij = int(input(f"W tej chwili posiadasz {dexterity} pkt zręczności. Ile chcesz odjąć? "))
            dexterity -= odejmij
            points += odejmij
            print("Twoja zręczność: ",dexterity)
            print("Pozosta pula pkt: ", points)
        if y == 3:
            print()
    if x == 0:
        break
    else:
        print("Nie posiadam takiej opcji, spróbuj ponownie!")
"""
Koniec Gry!
"""