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
    #This currently only draws one weapon. pic_name is overridden. pic_name should
    #be an array. 
    def __init__(self, pic_name, width, Height, slides):
        global game_object
        global cImage
        global num_slides
        global slide_width
        global height
        ship_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        game_object = pg.image.load(ship_path)
        height = Height
        num_slides = slides - 1
        cImage = 1
        slide_width = width

    def Animate():
        #Animation needs to be refined:
        #Should draw frames based on how charged the weapon is, then animate the firing
        global cImage
        cImage += 1
        if cImage > num_slides:
            cImage = 1
        
    def Draw(screen, x, y):
        screen.blit(game_object, (x, y), (cImage * slide_width, 0, slide_width, height))
