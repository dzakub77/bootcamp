
from livewires import games, color
import random

games.init(screen_height=480, screen_width=640, fps=50)

class Mysz(games.Sprite):
    patelnia_image = games.load_image("patelnia.bmp")

    def __init__(self):
        super(Mysz, self).__init__(image=Mysz.patelnia_image,
                                   x=games.mouse.x,
                                   bottom=games.screen.height)
        self.score = games.Text(value=0,
                           size=50,
                           color=color.black,
                           top=5,
                           right=games.screen.width - 10)
        games.screen.add(self.score)

    def update(self):
        self.x = games.mouse.x
        if self.left < 0:
            self.left = 0
        if self.right > games.screen.width:
            self.right = games.screen.width
        self.check_catch()

    def check_catch(self):
        for pizza in self.overlapping_sprites: #sprawdza czy obiekt pizza zachodzi na patelnie
            self.score.value += 10 #dodaje punkty do wyniku
            self.score.right = games.screen.width - 10 #upewniam się że wynik jest cały w tej samej pozycji niezależnie od wielkości wyniku
            pizza.handle_caught()
            if self.score.value == 50:
                Pizza.speed += 0.3
            elif self.score.value == 100:
                Pizza.speed += 0.4
            elif self.score.value == 150:
                Pizza.speed += 0.5
            elif self.score.value == 200:
                Pizza.speed += 0.6
            elif self.score.value == 250:
                Pizza.speed += 1
            elif self.score.value == 300:
                Pizza.speed += 2

class Pizza(games.Sprite):
    pizza_image = games.load_image("pizza.bmp")
    speed = 1

    def __init__(self, x, y = 90):
        super(Pizza, self).__init__(image=Pizza.pizza_image,
                                    x=x,
                                    y=y,
                                    dy=Pizza.speed)
    def update(self):
        if self.bottom > games.screen.height:
            self.end_game()
            self.destroy()

    def handle_caught(self):
        self.destroy()

    def end_game(self):
        end_message = games.Message(
                value="Koniec Gry!",
                size=130,
                color=color.red,
                x=games.screen.width/2,
                y=games.screen.height/2,
                lifetime=5 * games.screen.fps,
                after_death=games.screen.quit)
        games.screen.add(end_message)

class Chef(games.Sprite):
    chef_image = games.load_image("kucharz.bmp")


    def __init__(self, y = 55, speed = 2, odds_change = 100):
        super(Chef, self).__init__(image=Chef.chef_image,
                                   x = games.screen.width/2,
                                   y = y,
                                   dx = speed)
        self.odds_change = odds_change
        self.time_till_drop = 0

    def update(self):
        if self.left < 0 or self.right > games.screen.width:
            self.dx = -self.dx
        elif random.randrange(self.odds_change) == 0:
            self.dx = -self.dx

        self.check_drop()

    def check_drop(self):
        if self.time_till_drop > 0:
            self.time_till_drop -= 1
        else:
            new_pizza = Pizza(x = self.x)
            games.screen.add(new_pizza)
            self.time_till_drop = int(new_pizza.height * 5 / Pizza.speed) + 1

def main():
    wall_image = games.load_image('sciana.jpg', transparent=False)
    games.screen.background = wall_image

    the_chef = Chef()
    games.screen.add(the_chef)

    the_mouse = Mysz()
    games.screen.add(the_mouse)

    games.mouse.is_visible = False
    games.screen.event_grab = True

    games.screen.mainloop()

main()
