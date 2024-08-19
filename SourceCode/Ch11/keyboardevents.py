import pygame

class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")

        # Load the image
        self.image = pygame.image.load("rocket.png")
        self.image_rect = self.image.get_rect()
        self.image_rect.center = (self.width // 2, self.height // 2)

        # Set key repeat delay and interval
        pygame.key.set_repeat(200, 50)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                # Check for key presses and repeats
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.image_rect.x -= 10
                    elif event.key == pygame.K_RIGHT:
                        self.image_rect.x += 10
                    elif event.key == pygame.K_UP:
                        self.image_rect.y -= 10
                    elif event.key == pygame.K_DOWN:
                        self.image_rect.y += 10

            # Fill the background
            self.screen.fill((0, 0, 0))

            # Blit the image on the screen
            self.screen.blit(self.image, self.image_rect)

            pygame.display.flip()  # Update the window display

        pygame.quit()  # Close the Pygame window and exit the game

# Create an instance of the GameWindow class and run the game
game = GameWindow(800, 600)
game.run()
