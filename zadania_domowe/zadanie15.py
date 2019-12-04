
def odwrotnie(word):
    new_word = word.split()
    x = new_word[::-1]
    y = " ".join(x)
    return y

print(odwrotnie("My name is Jakub"))