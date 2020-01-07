
class Player:
    """ Uczestnik gry. """
    def __init__(self, name, score = 0):
        self.name = name
        self.score = score

    def __str__(self):
        rep = self.name + ':\t' + str(self.score)
        return rep

def ask_yes_no(question):
    """Zadaj pytanie na które można odpowiedzieć tak lub nie"""
    response = None
    while response not in("t", "n"):
        response = input(question).lower()
    return response

def ask_number(question, low, high):
    """Poproś o poadanie liczby z okreslonego zakresu."""
    resposne = None
    while resposne not in range(low, high):
        resposne = int(input(question))
    return resposne

if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezposrednio, zamiast go zaimportować")
