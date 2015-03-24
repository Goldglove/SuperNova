import Main, os, GameObject
import pygame as pg

class Weapons():
    global x
    global y
    global screen
    global game_object
    global num_slides
    global cImage
    global num_slides
    global slide_width
    global height
    def __init__(self, pic_name, width, Height, slides):
        global game_object
        global x
        global y
        global cImage
        global num_slides
        global slide_width
        global height
        ship_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        game_object = pg.image.load(ship_path)
        x = 20
        y = 0
        height = Height
        num_slides = slides - 1
        cImage = 1
        slide_width = width

    def Animate():
        global cImage
        cImage += 1
        if cImage > num_slides:
            cImage = 1
        
    def Draw(screen):
        screen.blit(game_object, (x, y), (cImage * slide_width, 0, slide_width, height))
