
class Critter:

    def __init__(self, name, hunger = 0, boredom = 0):
        self.name = name
        self.hunger = hunger
        self.boredom = boredom

    def __pass_time(self):
        self.hunger += 1
        self.boredom += 1

    @property
    def mood(self):
        unhappiness = self.hunger + self.boredom
        if unhappiness < 5:
            m = "Jestem szczęśliwy!"
        elif 5 <= unhappiness <= 10:
            m = "Jestem zadowolony!"
        elif 11 <= unhappiness <= 15:
            m = "Jestem zły!"
        else:
            m = "Jestem wściekły!"
        return m

    def talk(self):
        print(f"Nazywam się {self.name}, i jestem teraz {self.mood}")
        self.__pass_time()

    def eat(self):
        food = int(input("Jaka ilość jedzenia? "))
        print("To było pyszne!")
        self.hunger -= food
        if self.hunger < 0:
            self.hunger = 0
        self.__pass_time()

    def play(self):
        fun = int(input("Ile bedziemy sie bawic? "))
        print("Świetna zabawa!")
        self.boredom -= fun
        if self.boredom < 0:
            self.boredom = 0
        self.__pass_time()

    def __str__(self):
        return f"name: {self.name}\ngłód: {self.hunger}\nhumor: {self.boredom}"

def main():
    crit_name = input("Jak mam nazwac zwierzaka? ")
    crit = Critter(crit_name)

    choice = None
    while choice != '0':
        print('''
            Opiekun zwierzaka
            0 - zakończ
            1 - sprawdź co u twojego zwierzaka
            2 - nakarm go 
            3 - pobaw się''')

        choice = input("Co wybierasz? ")
        print()

        if choice == '0':
            print('Do widzenia!')
        elif choice == '1':
            crit.talk()
        elif choice == '2':
            crit.eat()
        elif choice == '3':
            crit.play()
        elif choice == '9':
            print(crit)
        else:
            print(f'Wybor {choice} jest nieprawidłowym wyborem')

main()
input("Naciśnij enter aby zakonczyc program!")