word = input("Podaj słowo: ")
x = word[::-1]
y = x[::-1]
print(y)
for i in word:
    if  word == y:
        print("To słowo jest palindromem")
        break
    else:
        print("To nie jest palindrom")
        break