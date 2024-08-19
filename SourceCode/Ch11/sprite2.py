import pygame
import os

pygame.init()

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 600
window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
window.fill((255, 255, 255))  # Set initial background color to white

frames_directory = "ufo_frames"
frame_filenames = os.listdir(frames_directory)

image_sprite = []
for filename in frame_filenames:
    if filename.endswith(".png"):
        image = pygame.image.load(os.path.join(frames_directory, filename))
        image_sprite.append(image)

clock = pygame.time.Clock()
frame = 0

running = True
while running:
    # set frames per second
    clock.tick(12)

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
