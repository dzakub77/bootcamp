
from livewires import games

games.init(screen_width=640, screen_height=480, fps=50)

wall_image = games.load_image('mglawica.jpg', transparent=False)
games.screen.background = wall_image

explosions_images = ['eksplozja1.bmp',
                     'eksplozja2.bmp',
                     'eksplozja3.bmp',
                     'eksplozja4.bmp',
                     'eksplozja5.bmp',
                     'eksplozja6.bmp',
                     'eksplozja7.bmp',
                     'eksplozja8.bmp',
                     'eksplozja9.bmp']

explosions = games.Animation(images=explosions_images,
                             x=games.screen.width / 2,
                             y=games.screen.height / 2,
                             n_repeats=0,  # ustawiam ile razy ma być powatarza animacja. Ustawienie na 0 spowoduje że bez się powtarzać bez przerwy
                             repeat_interval= 15) # ustawienie jak szybko animacja ma przebiegać

games.screen.add(explosions)
games.screen.mainloop()