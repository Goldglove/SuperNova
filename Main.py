#Main class for the game... Will work on gettign multiple files with classes working tomorrow.
class SuperNova:
    #Different functions and methods in main class.
    def printHello():
        return ("Hello World!")

#Where the main loop will be in the game.
if __name__ == "__main__":
    #Supernova tells which class to take from .printHello tells what function in the class to use.
    print(SuperNova.printHello())
