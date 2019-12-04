a = [1, 1, 2, 2, 4, 4, 4, 3, 10, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 4, 13, 13, 1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13]

c = []
for i in a:
    for j in b:
        if i == j and i not in c:
            c.append(i)

print(sorted(c))