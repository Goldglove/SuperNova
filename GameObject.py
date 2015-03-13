import Main, os


class GameObject:
    global x
    global y
    x = 20
    y = 0
    
    def __init__(self, pic_name, Screen, pygame):
        global screen
        screen = Screen
        pg = pygame
        self.ship_path = os.getcwd() + '\\Images\\Ships\\' + pic_name
        global game_object
        game_object = pg.image.load(self.ship_path)

    def Draw(self):
        screen.blit(game_object, (x, y))
