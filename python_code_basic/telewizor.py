

class Telewizor:
    def __init__(self, kanal = 0, volume = 0):
        self.kanal = kanal
        self.volume = volume

    @property
    def numer_kanalu(self):
        return f"Aktulany numer kanału: {self.kanal}"

    @property
    def vol(self):
        return f"Głośność: {self.volume}"

    def zmiana_kanalu(self):
        zmiana = int(input("Wprowadz numer kanału: "))
        self.kanal = zmiana
        print(self.numer_kanalu)

    def volup(self, up = 1):
        print("Podgłaszam")
        self.volume += up
        print(self.vol)

    def voldown(self, down = 1):
        print("Ściszam")
        self.volume -= down
        if self.volume < 0:
            self.volume = 0+565
        print(self.vol)


def main():
    tel = Telewizor()

    choice = None
    while choice != '0':
        print('''
            Menu telewizora
            0 - zakończ
            1 - zmień kanał
            2 - podgłaszanie 
            3 - ściszanie
            ''')

        choice = input("Co wybierasz? ")
        print()

        if choice == '0':
            print('Do widzenia!')
        elif choice == '1':
            tel.zmiana_kanalu()
        elif choice == '2':
            tel.volup()
        elif choice == '3':
            tel.voldown()
        else:
            print(f'Wybor {choice} jest nieprawidłowym wyborem')

main()
input("Naciśnij enter aby zakonczyc program!")