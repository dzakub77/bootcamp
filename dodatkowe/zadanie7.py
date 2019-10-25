

filename = input("Wprowadz nazwe pliku: ")
y = filename[::-1]
new_f = ""
for i in y:
    if i == '.':
        break
    new_f += i
z = new_f[::-1]
print(z)