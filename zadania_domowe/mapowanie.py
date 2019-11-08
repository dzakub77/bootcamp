import random

osoby = ['marek', 'przemek', "michał", "kamila"]
osoby2 = ['marek', 'przemek', "michał", "kamila"]

random.shuffle(osoby)
random.shuffle(osoby2)
licznik = 0
while licznik != 8:
    for os1, os2 in zip(osoby, osoby2):

        print(f"{os1} kupuje prezent {os2}")
        licznik += 1

