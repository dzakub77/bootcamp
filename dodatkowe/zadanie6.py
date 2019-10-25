
lista = []

y = 0
while y < 5:
    x = int(input("Wprowadz cyfre: "))
    y += 1
    lista.append(x)
tupla = tuple(lista)
print(lista)
print(tupla)