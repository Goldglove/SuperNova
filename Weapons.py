import Main, os, GameObject
import pygame as pg

class Weapons():
    global x
    global y
    global screen
    global game_object
    global num_slides
    
    def __init__(self, pic_name):
        global game_object
        global x
        global y
        ship_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        game_object = pg.image.load(ship_path)
        x = 20
        y = 0
        num_slides = 6
        slide_on = 1

    def Animate():
        slide on += 1
        
    def Draw():
        screen.blit(game_object, (x, y))
