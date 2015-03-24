import Main, os


class GameObject:
    global x
    global y
    
    
    def __init__(self, pic_name, Screen, pygame):
        global screen
        screen = Screen
        pg = pygame
        self.ship_path = os.getcwd() + '\\Images\\' + pic_name
        #self.weapon_path = os.getcwd() + '\\Images\\Weapons\\' + pic_name
        global game_object
        game_object = pg.image.load(self.ship_path)
        self.x = 20
        self.y = 0

    def SetXPosition(self, X):
        self.x = X

    def SetYPosition(self, Y):
        self.y = Y

    def GetXPosition(self):
        return self.x

    def GetYPosition(self):
        return self.y    

    def Draw(self):
        screen.blit(game_object, (self.x, self.y))
