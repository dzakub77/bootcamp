from faker import Faker

fake = Faker("pl_Pl")



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
        return f"\nname: {self.name}\ngłód: {self.hunger}\nhumor: {self.boredom}"

def main():
    crit1_name = fake.name()
    crit2_name = fake.name()
    crit3_name = fake.name()
    crit4_name = fake.name()

    crit1 = Critter(crit1_name)
    crit2 = Critter(crit2_name)
    crit3 = Critter(crit3_name)
    crit4 = Critter(crit4_name)
    crit_lista = []
    crit_lista.append(crit1)
    crit_lista.append(crit2)
    crit_lista.append(crit3)
    crit_lista.append(crit4)

    choice = None
    while choice != '0':
        print(f'''
            Opiekun zwierzaka
            0 - zakończ
            1 - sprawdź co u twojego zwierzaka:
            2 - nakarm zwierzaka
            3 - pobaw się''')

        choice = input("Co wybierasz? ")
        if choice == '0':
            print('Do widzenia!')
        elif choice == '1':
            print(f'''
                - {crit1_name}
                - {crit2_name}
                - {crit3_name}
                - {crit4_name}''')
            x = input("Wprowadź imię zwierzaka którego chcesz sprawdzić: ")
            if x == crit4_name:
                crit4.talk()
            elif x == crit3_name:
                crit3.talk()
            elif x == crit2_name:
                crit2.talk()
            elif x == crit1_name:
                crit1.talk()
        elif choice == '2':
            print(f'''
                - {crit1_name}
                - {crit2_name}
                - {crit3_name}
                - {crit4_name}''')
            x = input("Wprowadź imię zwierzaka którego chcesz nakarmić: ")
            if x == crit4_name:
                crit4.eat()
            elif x == crit3_name:
                crit3.eat()
            elif x == crit2_name:
                crit2.eat()
            elif x == crit1_name:
                crit1.eat()
        elif choice == '3':
            print(f'''
                - {crit1_name}
                - {crit2_name}
                - {crit3_name}
                - {crit4_name}''')
            x = input("Wprowadź imię zwierzaka z którym chcesz się pobawić: ")
            if x == crit4_name:
                crit4.play()
            elif x == crit3_name:
                crit3.play()
            elif x == crit2_name:
                crit2.play()
            elif x == crit1_name:
                crit1.play()
        elif choice == '9':
            print(f"[{crit1}, {crit2}, {crit3}, {crit4}]")
        else:
            print(f'Wybor {choice} jest nieprawidłowym wyborem')

main()
input("Naciśnij enter aby zakonczyc program!")