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
    global reverse_animate
    global bullet_x
    global bullet_y
    def InitArrays():
        global game_object
        global cImage
        global num_slides
        global slide_width
        global height
        global atk_spd
        global atk_timer
        global reverse_animate
        global bullet_x
        global bullet_y
        height = [0]
        reverse_animate = [""]
        slide_width = [0]
        num_slides = [0]
        cImage = [0]
        num_slides = [0]
        game_object = [0]
        atk_spd = [0]
        atk_timer = [0]
        bullet_x = 100
        bullet_y = 200
        
    def CreateWeapon(pic_name, width, Height, slides, damage, attack_speed, power_req, num_shots, use_missle, backwards):
        global game_object
        global cImage
        global num_slides
        global slide_width
        global height
        global atk_spd
        global atk_timer
        global reverse_animate
        ship_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        game_object.append(pg.image.load(ship_path))
        height.append(Height)
        num_slides.append(slides - 1)
        slide_width.append(width)
        cImage.append(1)
        atk_spd.append(attack_speed)
        atk_timer.append(0)
        reverse_animate.append(backwards)

    def Shoot(init_x, init_y, dest_x, dest_y):
        global bullet_x
        global bullet_y
        bullet_x_speed= round((((init_x ** 2)+(dest_x ** 2)) ** 0.5)/150)
        bullet_y_speed= round((((init_y ** 2)+(dest_y ** 2)) ** 0.5)/150)
        bullet_x+=bullet_x_speed
        bullet_y+=bullet_y_speed
        return (str(bullet_x) + " " + str(bullet_y))
        
    def Animate():
        global cImage
        global atk_timer
        for i in range(len(cImage)):
            atk_timer[i] += 1
            if atk_timer[i] >= atk_spd[i]:
                atk_timer[i] = 0
                if reverse_animate[i] == "0":
                    cImage[i] += 1
                    if cImage[i] > num_slides[i]:
                        cImage[i] = 1
                else:
                    cImage[i] -= 1
                    if cImage[i] < 0:
                        cImage[i] = num_slides[i]
        
    def Draw(screen, x, y, index):
        screen.blit(game_object[index], (x, y), (cImage[index] * slide_width[index], 0, slide_width[index], height[index]))
