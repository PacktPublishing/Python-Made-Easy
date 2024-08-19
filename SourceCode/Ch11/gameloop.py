import pygame

class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            
            pygame.display.flip()  # Update the window display
        
        pygame.quit()  # Close the Pygame window and exit the game

# Create an instance of the GameWindow class and run the game
game = GameWindow(800, 600)

game.run()

