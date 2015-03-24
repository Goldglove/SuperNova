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
        #weapon1 = Weapons.Weapons("wep1.png", screen, pg)
        player1 = Player.Player()

    def Draw():
        screen.fill(white)
        Player.Player.Draw(screen)
        Enemy.Enemy.Draw(screen)
        pg.time.delay(60)
        pg.display.flip()
### NOTE:
###         No matter what we call to draw, it will draw the last called object
###         Here I call to draw player1, but because weapon1 was last called it is
###         drawn instead.
### SOLUTION:
###         We are currently only blitting one gameobject
###         per main loop (look in GameObject.py\\line:16), we need to blit multiple
###         objects per loop. Changes to GameObject.py are needed.

    def InputEvents():
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_a:
                    Player.Player.SetXPosition(Player.Player.GetXPosition() - 10)
                if event.key == pg.K_d:
                    Player.Player.SetXPosition(Player.Player.GetXPosition() + 10)
            #elif event.type == KEYUP:
        
if __name__ == "__main__":
    main()
    while game_running:
        main.InputEvents()     
        main.Draw()
         


