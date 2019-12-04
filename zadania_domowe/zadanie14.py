
def listy():
    print("Jak skończysz wprowadzać liste, nacisnij e")
    a = []
    b = []
    licznik = 0
    while licznik != 5:
        x = int(input("Wprowadź liste: "))
        a.append(x)
        licznik += 1
    for i in a:
        if i not in b:
            b.append(i)
    return b, a

print(listy())