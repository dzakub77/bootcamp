

x = int(input("Wprowadz liczbe: "))

for i in range(2, 100):
    if x % i == 0 and x != i:
        print(f"{x} nie jest liczba pierwsza")
        break
    else:
        print("Liczba pierwsza")
        break