
class Critter():
    total = 0

    def __init__(self, name):
        print("Urodził się nowy zwierzak")
        self.name = name
        Critter.total += 1

    def talk(self):
        print(f"Cześć, jestem {self.name}")

    @staticmethod
    def status():
        print("Tyle zwierzaków powstało", Critter.total)

    def __str__(self):
        napis = "Obiekt klasy Critter:\n"
        napis += "Name:" + self.name
        return napis

    # @property
    # def name(self):
    #     return self.__name
    #                                   przyklad dostepu do prywatnej metody poprzez wlasciwosci
    # @name.setter
    # def name(self, new_name):
    #     if new_name == "":
    #         print("Pusty napis nie moze byc nowym imieniem")
    #     else:
    #         self.name = new_name
    #         print("Zmiana imienia powiodla sie")

crit1 = Critter("Burek")
crit1.talk()
crit2 = Critter("Pucek")
crit2.talk()
Critter.status()