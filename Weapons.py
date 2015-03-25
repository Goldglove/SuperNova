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
    global atk_speed
    global atk_timer
    #This currently only draws one weapon. pic_name is overridden. pic_name should
    #be an array.
    def InitArrays():
        global game_object
        global cImage
        global num_slides
        global slide_width
        global height
        global atk_spd
        global atk_timer
        height = [0]
        slide_width = [0]
        num_slides = [0]
        cImage = [0]
        num_slides = [0]
        game_object = [0]
        atk_spd = [0]
        atk_timer = [0]
        
    def CreateWeapon(pic_name, width, Height, slides, damage, attack_speed):
        global game_object
        global cImage
        global num_slides
        global slide_width
        global height
        global atk_spd
        global atk_timer
        ship_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        game_object.append(pg.image.load(ship_path))
        height.append(Height)
        num_slides.append(slides - 1)
        slide_width.append(width)
        cImage.append(1)
        atk_spd.append(attack_speed)
        atk_timer.append(0)

    def Animate():
        #Animation needs to be refined:
        #Should draw frames based on how charged the weapon is, then animate the firing
        global cImage
        global atk_timer
        for i in range(len(cImage)):
            atk_timer[i] += 1
            if atk_timer[i] >= atk_spd[i]:
                atk_timer[i] = 0
                cImage[i] += 1
                if cImage[i] > num_slides[i]:
                    cImage[i] = 1
        
    def Draw(screen, x, y, index):
        screen.blit(game_object[index], (x, y), (cImage[index] * slide_width[index], 0, slide_width[index], height[index]))
