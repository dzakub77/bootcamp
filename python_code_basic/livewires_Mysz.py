
from livewires import games
import random

games.init(screen_height=480, screen_width=640, fps=50)

class Mysz(games.Sprite):
    """Ustawienie myszy jako patelnia i ustawianie współrzędnych"""
    def update(self):
        self.x = games.mouse.x
        self.y = games.mouse.y
        self.check_collide()

    def check_collide(self):
        for pizza in self.overlapping_sprites:
            pizza.handle_collide()

class Pizza(games.Sprite):
    def handle_collide(self):
        self.x = random.randrange(games.screen.width)
        self.y = random.randrange(games.screen.height)


def main():
    wall_image = games.load_image('sciana.jpg', transparent=False)
    games.screen.background = wall_image
    patelnia_image = games.load_image("patelnia.bmp")
    patelnia = Mysz(image = patelnia_image,
                    x = games.mouse.x,
                    y = games.mouse.y)
    pizza_image = games.load_image("pizza.bmp")
    pizza_x = random.randrange(games.screen.width)
    pizza_y = random.randrange(games.screen.height)
    pizza = Pizza(image=pizza_image,
                  x=pizza_x,
                  y=pizza_y)
    games.screen.add(pizza)
    games.screen.add(patelnia)
    games.mouse.is_visible = False # wskaźnik myszy będzie nie widoczny
    games.screen.event_grab = True # obsługa wszystkich sygnałów wejściowych zostanie skoncentrowana w ekrania graficznym
    games.screen.mainloop()

main()