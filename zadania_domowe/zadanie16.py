import random
def gen_pass(word):
    weak_pass = ('babajaga', 'kogielmogiel', 'jabol')
    strong_pass = ('Pierwszytydzien123', 'Bardzosilnehaslo567*', 'mniejsilne--', 'sredniosilne1234567')
    if word == "silne":
        return random.choice(strong_pass)
    elif word == "słabe":
        return random.choice(weak_pass)
    else:
        return "Nie poprawna komenda. Wpisz 'słabe'/'silne'"

print(gen_pass("silne"))