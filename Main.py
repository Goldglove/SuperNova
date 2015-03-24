import pygame as pg
import GameObject, Weapons, Player, Enemy
import sys, os

game_running = True

#Colour Dictionary
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

pg.init()
#Create the Screen
screen = pg.display.set_mode((600, 480))
global pause
pause = 1

#The Main Class - This class handles the main initialization and creating of the Game.
class main:
    global player1
    global weapon1
    global enemy1
    def __init__(self):
        pg.init()
        pg.display.set_caption("SuperNova")
        window_icon_path = os.getcwd() + '\\Images\\window_icon.jpg'
        window_icon = pg.image.load(window_icon_path)
        pg.display.set_icon(window_icon)
        global player1
        global weapon1
        global enemy1
        enemy1 = Enemy.Enemy()
        #(pic name, slide width, slide height, num slides)
        weapon1 = Weapons.Weapons("autocannon3.png", 20, 79, 6)
        player1 = Player.Player()

    def Draw():
        screen.fill(white)
        Player.Player.Draw(screen)
        Enemy.Enemy.Draw(screen)
        Weapons.Weapons.Draw(screen)
        pg.time.delay(60)
        pg.display.flip()

    def Update():
        Weapons.Weapons.Animate()
        
    def Quit():
        pg.quit()
        sys.exit()
    def pause():
        global pause
        pause+=1

    def InputEvents():
        global pause
        for event in pg.event.get():
            if event.type == pg.QUIT:
                main.Quit()
            elif event.type == pg.KEYDOWN:
                try:
                    key_list = {
                        pg.K_a : lambda : Player.Player.SetXPosition(Player.Player.GetXPosition() - 10),
                        pg.K_d : lambda : Player.Player.SetXPosition(Player.Player.GetXPosition() + 10),
                        pg.K_SPACE : lambda : main.pause(),
                        pg.K_ESCAPE : lambda : main.Quit()
                    }[event.key]()
                except KeyError:
                    break
        
if __name__ == "__main__":
    main()
    while game_running:
        main.InputEvents()
        if pause % 2 == 1:
            main.Update()
            main.Draw()
         

