import random

osoby = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]

random.shuffle(osoby)
random.shuffle(osoby2)
licznik = 0
while licznik != 4:
    for os1, os2 in zip(osoby, osoby2):
        if os1 == os2:
            print()
            licznik -= 1
        else:
            print(f"{os1} kupuje prezent {os2}")
            licznik += 1

