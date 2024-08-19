import pygame

pygame.mixer.init()
sound_effect = pygame.mixer.Sound("laser.mp3")
sound_effect.play()

while pygame.mixer.get_busy():
    pygame.time.Clock().tick(10)

pygame.mixer.quit()



