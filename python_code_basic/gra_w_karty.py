
class Card(object):
    """Karta do gry"""
    RANKS = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
    SUITS = ['c', 'd', 'h', 's'] # c -trefle(ang.clubs), d -kara(ang.diamonds), h - kiery(ang.hearts), s- piki(ang.spades)

    def __init__(self, rank, suit, face_up = True):
        self.rank = rank
        self.suit = suit
        self.is_face_up = face_up

    def __str__(self):
        if self.is_face_up:
            rep = self.rank + self.suit
        else:
            rep = "XX"
        return rep

    def flip(self):
        self.is_face_up = not self.is_face_up

class Hand(object):
    """Ręka - karty do gry w ręku gracza"""
    def __init__(self):
        self.cards = []

    def __str__(self):
        if self.cards:
            rep = ''
            for card in self.cards:
                rep += str(card) + "\t"
        else:
            rep = "<pusta>"
        return rep

    def clear(self):
        self.cards = []

    def add(self, card):
        self.cards.append(card)

    def give(self, card, other_hand):
        self.cards.remove(card)
        other_hand.add(card)

class Deck(Hand):
    def populate(self):
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                self.add(Card(rank, suit))

    def shuffle(self):
        import random
        random.shuffle(self.cards)

    def deal(self, hands, per_hand = 1):
        for rounds in range(per_hand):
            for hand in hands:
                if self.cards:
                    top_card = self.cards[0]
                    self.give(top_card, hand)
                else:
                    "Nie moge dalej rozdawac!"



if __name__ == "__main__":
    print("Uruchomiłeś ten moduł bezposrednio, zamiast go zaimportować")

# class Unprinttable_Card(Card):
#     def __str__(self):
#         rep = "<Utajniona"
#         return rep
#
# class Positionable_Card(Card):
#     """Klasa pozwala na odrycie lub zakrycie kart"""
#     def __init__(self, rank, suit, face_up = True):
#         super(Positionable_Card, self).__init__(rank, suit)
#         self.is_face_up = face_up
#
#     def __str__(self):
#         if self.is_face_up:
#             rep = super(Positionable_Card, self).__str__()
#         else:
#             rep = "XX"
#         return rep
#
#     def flip(self):
#         self.is_face_up = not self.is_face_up
#
# deck1 = Deck()
# print("Nowa talia:")
# print(deck1)
# print("Dodaje karty do talii")
# deck1.populate()
# print(deck1)
# print('Tasuje talię')
# deck1.shuffle()
# print(deck1)
# my_hand = Hand()
# your_hand = Hand()
# hands = [my_hand, your_hand]
# deck1.deal(hands, per_hand=5)
# print(my_hand)
# print(your_hand)
# print("Usuwam zawartość talii.")
# deck1.clear()
# print(deck1)


# card1 = Card(rank = '2', suit = 's')
# card2 = Card(rank = '4', suit = 'd')
# card3 = Card(rank = 'J', suit = 'd')
# card4 = Card(rank = '6', suit = 'h')
# card5 = Card(rank = 'Q', suit = 'd')
# card6 = Card(rank = 'A', suit = 'c')
#
# my_hand = Hand()
# my_hand.add(card2)
# my_hand.add(card1)
# my_hand.add(card5)
# my_hand.add(card4)
# print(my_hand)
# your_hand = Hand()
# my_hand.give(card2, your_hand)
# my_hand.give(card4, your_hand)
# print(my_hand)
# print(your_hand)
# my_hand.clear()
# print(my_hand)