import pygame as pg
import sys, os

game_running = True
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
darkBlue = (0,0,128)
white = (255,255,255)
black = (0,0,0)
pink = (255,200,200)

pg.init()
"""Create the Screen"""
screen = pg.display.set_mode((600, 480))

class main:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    def __init__(self):
        pg.init()
        pg.display.set_caption("SuperNova")

    def Draw():
        screen.fill(white)
        pg.draw.line(screen, black, (100, 100), (300, 300), 5)
        

if __name__ == "__main__":
    main()
    while game_running:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
        main.Draw()
        pg.display.flip() 
        pg.time.delay(60)
        
