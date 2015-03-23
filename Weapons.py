import Main, os, GameObject

class Weapons():
    global x
    global y
    
    def __init__(self, pic_name, Screen, pygame):
        self.SelF = GameObject.GameObject(pic_name, Screen, pygame)
        return

    def Draw():
        self.SelF.Draw()
