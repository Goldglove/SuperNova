import pygame as pg
import GameObject, Weapons, Player, Enemy
import sys, os

game_running = True

wep_data = open("weapon.data", 'r')
wep_data.readline()

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
    global enemy1
    global weapon
    def __init__(self):
        pg.init()
        pg.display.set_caption("SuperNova")
        window_icon_path = os.getcwd() + '\\Images\\window_icon.jpg'
        window_icon = pg.image.load(window_icon_path)
        pg.display.set_icon(window_icon)
        global player1
        global weapon
        global enemy1
        weapon = []
        Weapons.Weapons.InitArrays()
        enemy1 = Enemy.Enemy()
        #(pic name, slide width, slide height, num slides)
        player1 = Player.Player()

    def Draw():
        screen.fill(white)
        Player.Player.Draw(screen)
        Enemy.Enemy.Draw(screen)
        Weapons.Weapons.Draw(screen, 20, 0, 3)
        Weapons.Weapons.Draw(screen, 20, 200, 7)
        Weapons.Weapons.Draw(screen, 20, 400, 1)
        pg.time.delay(60)
        pg.display.flip()

    def LoadWeapon():
    #will add the reverse animate during tomorros class
        i = 0
        for line in wep_data:
            i += 1
            temp_string = line
            temp_array = []
            temp_array = temp_string.split(' ')
            ship_name = temp_array[0]
            slide_width = temp_array[1]
            slide_height = temp_array[2]
            num_slides = temp_array[3]
            attack_dmg = temp_array[4]
            attack_spd = temp_array[5]
            power_req = temp_array[6]
            num_shots = temp_array[7]
            use_missle = temp_array[8]
            weapon.append(Weapons.Weapons.CreateWeapon(ship_name, int(slide_width), int(slide_height), int(num_slides), int(attack_dmg), int(attack_spd)))
        
        
    def Update():
        Weapons.Weapons.Animate()
        
    def Quit():
        wep_data.close()
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
    main.LoadWeapon()
    while game_running:
        main.InputEvents()
        if pause % 2 == 1:
            main.Update()
            main.Draw()
    

