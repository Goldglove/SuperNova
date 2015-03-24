import Main, os, GameObject
import pygame as pg

class Player:
    global x
    global y
    global screen
    global game_object
    
    def __init__(self):
        global game_object
        global x
        global y
        ship_path = os.getcwd() + '\\Images\\Ships\\placeHolderShip.png'
        game_object = pg.image.load(ship_path)
        x = 20
        y = 0

    def SetXPosition(X):
        global x
        x = X

    def SetYPosition(Y):
        global y
        y = Y

    def GetXPosition():
        return x

    def GetYPosition():
        return y
    
    def Draw(Screen):
        screen = Screen
        screen.blit(game_object, (x, y))
