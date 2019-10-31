
import random
words = ['takie', 'przypadkowe', 'slowa', 'w', 'roznej', 'kolejnosci', 'itd']
y = []
x = 0
while x < 7:
    word = random.choice(words)
    if word in words:
        words.remove(word)
    print(word)
    x += 1