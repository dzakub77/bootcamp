

class Player:
    def blast(self, enemy):
        print("Atak!")
        enemy.die()

class Alien:
    def die(self):
        print("Ja umierać")

hero = Player()
invader = Alien()
hero.blast(invader)