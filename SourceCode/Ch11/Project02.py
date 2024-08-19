import pygame

class Rocket:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("rocket.png")
        self.image = pygame.transform.scale(self.image, (50, 100))
        self.rect = self.image.get_rect()
        self.rect.centerx = screen.get_rect().centerx
        self.rect.bottom = screen.get_rect().bottom

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move_left(self):
        self.rect.centerx -= 10

    def move_right(self):
        self.rect.centerx += 10
        

# Initialize game and create a screen object.
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("My Invaders")

# Set the background image.
background = pygame.image.load("bg.jpg")

# Create our game clock
clock = pygame.time.Clock()

# Turn on key repeat
pygame.key.set_repeat(1, 25)

# Create a rocket object
rocket = Rocket(screen)

# Game loop.
running = True
while running:
    # Execute loop at 25 frames per second
    clock.tick(25)

    # Clear the screen and add the background image.
    screen.blit(background, (0, 0))

    # Draw the rocket
    rocket.draw()

    # Update the screen
    pygame.display.update()

pygame.quit()
