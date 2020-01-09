
from livewires import games, color
import random

games.init(screen_width=640, screen_height=480, fps=50)
# wall_image = games.load_image('niebo.jpg', transparent=False)
# games.screen.background = wall_image



class Paletka(games.Sprite):
    paletka_image = games.load_image('paletka.png')

    def __init__(self):
        super(Paletka, self).__init__(image=Paletka.paletka_image,
                                      x=games.mouse.x,
                                      bottom=games.screen.height - 30,)

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
        self.check_collide()

    def check_collide(self):
        for pilka in self.overlapping_sprites:
            self.score.value += 10
            self.score.right = games.screen.width - 10
            pilka.handle_collide()

class Pilka(games.Sprite):
    pilka_image = games.load_image('pizza.bmp')
    speed = 2.5

    def __init__(self):
        super(Pilka, self).__init__(image=Pilka.pilka_image,
                                    x=games.screen.width/2,
                                    y=games.screen.height/2,
                                    dy=1,
                                    dx=1)


    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx
        if self.top < 0:
            self.dy = -self.dy
        if self.bottom > games.screen.height:
            self.end_game()

    def end_game(self):
        end_message = games.Message(
            value="Koniec Gry!",
            size=130,
            color=color.yellow,
            x=games.screen.width/2,
            y=games.screen.height/2,
            lifetime=3 * games.screen.fps,
            after_death=games.screen.quit)
        games.screen.add(end_message)

    def handle_collide(self):

        self.dx = self.dx
        if self.dx == self.dx:
            self.dy = -self.dy
        elif self.dy == self.dy:
            self.dx = -self.dx


def main():
    wall_image = games.load_image('niebo.jpg', transparent=False)
    games.screen.background = wall_image
    the_paletka = Paletka()
    games.screen.add(the_paletka)

    the_pilka = Pilka()
    games.screen.add(the_pilka)

    games.mouse.is_visible = False
    games.screen.event_grab = False
    games.screen.mainloop()

main()
