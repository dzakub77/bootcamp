
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

class Ship(games.Sprite):

    def update(self):
        """Ustawienie klawiszy sterujących"""
        if games.keyboard.is_pressed(games.K_w):
            self.y -= 1
        if games.keyboard.is_pressed(games.K_s):
            self.y += 1
        if games.keyboard.is_pressed(games.K_a):
            self.x -= 1
        if games.keyboard.is_pressed(games.K_d):
            self.x += 1
        """Ustawienie klawiszy które obracają statek"""
        if games.keyboard.is_pressed(games.K_RIGHT):
            self.angle += 1 #odpowiada za stopnie
        if games.keyboard.is_pressed(games.K_LEFT):
            self.angle -= 1

        if games.keyboard.is_pressed(games.K_1):
            self.angle = 0
        if games.keyboard.is_pressed(games.K_2):
            self.angle = 90
        if games.keyboard.is_pressed(games.K_3):
            self.angle = 180
        if games.keyboard.is_pressed(games.K_4):
            self.angle = 270

def main():
    wall_image = games.load_image('mglawica.jpg', transparent=False)
    games.screen.background = wall_image

    statek_image = games.load_image("statek.bmp")
    statek = Ship(image=statek_image,
                  x=games.screen.width/2,
                  y=games.screen.height/2)
    games.screen.add(statek)
    games.screen.mainloop()

main()