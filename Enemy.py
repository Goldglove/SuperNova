import Main, os
import pygame as pg

class Enemy:
    global x
    global y
    global screen
    global game_object
    
    def __init__(self):
        global game_object
        global x
        global y
        ship_path = os.getcwd() + '\\Images\\Ships\\TestEnemyShip.png'
        game_object = pg.image.load(ship_path)
        x = 200
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
