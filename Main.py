import pygame

game_running = True

class main:
    """The Main PyMan Class - This class handles the main 
    initialization and creating of the Game."""
    
	def __init__(self, width=640,height=480):
		pygame.init()
        """Set the window Size"""
		self.width = width
		self.height = height
        """Create the Screen"""
		self.screen = pygame.display.set_mode((self.width, self.height))

if __name__ == "__main__":
	while game_running:	
		for event in pygame.event.get():
			if event.type == pygame.QUIT: 
				sys.exit()
		main()
