import pygame

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill((255, 255, 255))  # Set initial background color to white

# Create a list of frames for the animation
image_sprite = [pygame.image.load("frame01.png"),
                pygame.image.load("frame02.png"),
                pygame.image.load("frame03.png")]

clock = pygame.time.Clock()
frame = 0

running = True
while running:
    # set frames per second
    clock.tick(3)

    # check for end of list, if end of list is found reset frame counter to 0
    if frame >= len(image_sprite):
        frame = 0

    # Clear the window with white background
    window.fill((255, 255, 255))

    # display current frame in image_sprite list at co-ordinates 0, 140
    window.blit(image_sprite[frame], (0, 140))

    pygame.display.update()

    # increment frame counter
    frame += 1
