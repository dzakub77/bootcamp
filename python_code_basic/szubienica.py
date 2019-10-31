import random

words = ['morze', 'kaloryfer', 'komoda', 'laptop', 'lusterko', 'obraz', 'pudełka', 'skarbonka', 'łóżko', 'podłoga',
         'ala ma kota a kot ma ale', 'jak kuba bogu, tak bog kubie', 'ale jaja']
word = random.choice(words)
word = word.upper()
wisielec = (
   '''
    
    
    
    
    
    
    
   ----------
   ''',
   '''
    |
    |
    |
    |
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |
    |
    |
    |
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |
    |
    |
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |
    |
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |   -+-
    |
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |  /-+-\\
    | /     \\
    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |  /-+-\\
    | /  |  \\
    |    |
    |
    |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |  /-+-\\
    | /  |  \\
    |    |
    |  |
    |  |
    |
   ----------
   ''',
   '''
    ------
    |    |
    |    O
    |  /-+-\\
    | /  |  \\
    |    |
    |  |   |
    |  |   |
    |
   ----------
   ''')

wrong_answers = 0
wrong_letters = []
answer = '-' * len(word)
max_tries = len(wisielec)
while wrong_answers < max_tries and answer != word:
    print("Oto twoja zagadka: ", answer.upper())
    print("Wykorzystałeś już następujące litery: ", wrong_letters)
    x = input("Wybierz litere: ")
    x = x.upper()
    if x not in word:
        print("Niestety, ta litera tu nie pasuje.")
        if x in wrong_letters:
            print("Już używałeś tej litery!")
        else:
            wrong_letters.append(x)
        print(wisielec[wrong_answers])
        wrong_answers += 1
    elif x in answer:
        print("Już wykorzystałeś tą literę")
        print(wisielec[wrong_answers])
        wrong_answers += 1
    else:
        print("Tak, ta litera tu pasuje!")
        new = ""
        for i in range(len(word)):
            if x == word[i]:
                new += x
            else:
                new += answer[i]
        answer = new
    if wrong_answers == max_tries:
        print("Zostałeś powieszony! Koniec gry!")
    elif answer == word:
        print("Brawo, udało Ci się odgadnąć. Zagadka to ",word)