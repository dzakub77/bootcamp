#Napisz funkcję, która pozwoli na dodawanie do siebie macierzy.
#Funkcja przyjmuje jako argumenty macierze i zwraca ich sumę

 #   [[3, -3], [-3, 3]]
#add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]])
   # [[8, 8], [7, 7]]

m1 = [[1, -2, 3], [-3, 4, 2], [1, 2, 4]]
m2 = [[2, -1, 4], [0, -1, 1], [2, 3, 5]]
m3 = [[2, -1, 4], [0, -1, 1], [2, 3, 5]]
def add(*args):
    wynik = []
    for row1, row2 in zip(*args):
        wiersz = []
        for col1, col2 in zip(row1, row2):
            wiersz.append(col1 + col2)
        wynik.append(wiersz)
    return wynik

print(add(m1, m2))