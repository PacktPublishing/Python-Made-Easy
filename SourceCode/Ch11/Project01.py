import pygame

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



# Game loop.
running = True
while running:
    # Execute loop at 25 frames per second
    clock.tick(25)

    # Clear the screen and add the background image.
    screen.blit(background, (0, 0))

    # Update the screen
    pygame.display.update()



pygame.quit()
