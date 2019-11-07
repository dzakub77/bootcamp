a = [34, 84, 85, 2, 4, 9, 1, 0, 2, 4, 55, 71, 12, 6, 3]
x = []
for i in a:
    if i < 5:
        x.append(i)
print(x)
new_list = []
y = int(input("Podaj liczbe: "))
for i in a:
    if i < y:
        new_list.append(i)
print(new_list)
