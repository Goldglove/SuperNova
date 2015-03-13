import Main, os


class GameObject:
    def __init__(self, pic_name, Screen, pygame):
        screen = Screen
        pg = pygame
        self.ship_path = os.getcwd() + '\\Images\\Ships\\' + pic_name
        global game_object
        game_object = pg.image.load(self.ship_path)

       

    def Draw(self, Screen):
        screen = Screen
        screen.blit(game_object, (0, 0))
