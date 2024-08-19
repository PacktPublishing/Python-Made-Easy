import pygame

pygame.init()

pygame.mixer.music.load('music.mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)

pygame.mixer.music.stop()

pygame.quit()
