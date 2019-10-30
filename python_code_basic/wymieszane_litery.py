

# tworze tuple z losowych słów do wylosowania
# wybieram losowe słowo z tupli
# tworze petle która ma na celu wylosowanie litery z wylosowanego slowa i stworzenia z niej randomowego slowa
# tworze petli dzieki ktorej gracz bedzie mogl probować wprowadzic prawidlowo slowo z podanych liter
import random

gry = ('wiedźmin', 'naruto', 'diablo', 'fifa', 'needforspeed', 'UFC', 'heroes', 'plantsandzombie')
word = random.choice(gry)
correct = word
new_word = ""

while word:
    possition = random.randrange(len(word))
    possition = possition
    new_word += word[possition]
    word = word[:possition] + word[possition +1:]
print("Rozpoczynamy grę! W tej chwili masz 100 pkt. Za każdą nie udaną odpowiedź otrzymujesz -10 pkt, a za podpowiedź - 20 pkt.")
print(new_word)
tries = 1
p = input("Jeżeli potrzebujesz podpowiedźi wpisz y(yes)/n(no): ")
if p == 'y' and correct == 'wiedźmin':
    print("Ciri, Yennefer i Jaskier")
if p == 'y' and correct == 'naruto':
    print("Anime")
if p == 'y' and correct == 'diablo':
    print("Lord of Destruction")
if p == 'y' and correct == 'fifa':
    print("Zawsze piłka jest jedna, a bramki są dwie")
if p == 'y' and correct == 'needforspeed':
    print("Most Wanted")
if p == 'y' and correct == 'UFC':
    print("Joanna Jędrzejczyk")
if p == 'y' and correct == 'heroes':
    print("Might and Magic")
if p == 'y' and correct == 'plantsandzombie':
    print("Doniczki")
guess = input("Twoja odpowiedź: ")

while guess != correct and guess != "":
    print("Niestety to nie to słowo!")
    tries += 1
    p = input("Jeżeli potrzebujesz podpowiedźi wpisz y(yes)/n(no): ")
    if p == 'y' and correct == 'wiedźmin':
        print("Ciri, Yennefer i Jaskier")
    if p == 'y' and correct == 'naruto':
        print("Anime")
    if p == 'y' and correct == 'diablo':
        print("Lord of Destruction")
    if p == 'y' and correct == 'fifa':
        print("Zawsze piłka jest jedna, a bramki są dwie")
    if p == 'y' and correct == 'needforspeed':
        print("Most Wanted")
    if p == 'y' and correct == 'UFC':
        print("Joanna Jędrzejczyk")
    if p == 'y' and correct == 'heroes':
        print("Might and Magic")
    if p == 'y' and correct == 'plantsandzombie':
        print("Doniczki")
    guess = input("Twoja odpowiedź: ")


score = 100
if guess == correct and p == 'y':
    print("Brawo, udało Ci się zganąć, niestety za użycie podpowiedźi otrzymujesz -20 pkt.")
    print(f"Udało ci się za {tries} próbą")
    score = 100 - (tries * 10) - 20
    print(f"Zdobyłeś {score} pkt.")
elif guess == correct:
    print(f"Brawo, udało ci się za {tries} próbą")
    score = 100 - (tries * 10)