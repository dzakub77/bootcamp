
from livewires import games, color

games.init(screen_width= 640, screen_height= 480, fps=50)
wall_image = games.load_image('sciana.jpg', transparent=False)
games.screen.background = wall_image

class Pizza(games.Sprite):
    def update(self):
        if self.right > games.screen.width or self.left < 0:
            self.dx = -self.dx

        if self.bottom > games.screen.height or self.top < 0:
            self.dy = -self.dy

def main():
    wall_image = games.load_image('sciana.jpg', transparent=False)
    games.screen.background = wall_image
    pizza_image = games.load_image("pizza.bmp")
    pizza = Pizza(image = pizza_image,
                     x = games.screen.width/2,
                     y= games.screen.height/2,
                     dx = 1,
                     dy = 1)
    games.screen.add(pizza)
    games.screen.mainloop()

main()

"""Wyświetlenie wyniku w grze"""
# score = games.Text(value=1234455,
#                    size=40,
#                    color=color.green,
#                    x=80,
#                    y=30)
# games.screen.add(score)

"""Wyświetlenie napisu w grze"""
# text = games.Message(value="Wygrałeś!",
#                      size=130,
#                      color=color.red,
#                      x=games.screen.width/2,
#                      y=games.screen.height/2,
#                      lifetime=250,
#                      after_death=games.screen.quit)
# games.screen.add(text)

