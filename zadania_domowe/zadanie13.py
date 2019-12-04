

def fib():
    num = int(input("Ile numerów wygenerowac? "))
    i = 1
    if num == 0:
        c_fib = []
    elif num == 1:
        c_fib = [1]
    elif num == 2:
        c_fib = [1, 1]
    elif num > 2:
        c_fib = [1, 1]
        while i < (num - 1):
            c_fib.append(c_fib[i] + c_fib[i -1])
            i += 1
    return c_fib

print(fib())