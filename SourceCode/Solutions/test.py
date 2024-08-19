import pygame
pygame.init()

width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")

background_color = (255, 255, 255)  # white
shape_color = (255, 0, 0)  # red
shape_width = 100
shape_height = 100
shape_x = width // 2 - shape_width // 2
shape_y = height // 2 - shape_height // 2

movement_x = 0
movement_y = 0
movement_speed = 5

clock = pygame.time.Clock()

shape_rect = pygame.Rect(shape_x, shape_y, shape_width, shape_height)

window.fill(background_color)
pygame.draw.rect(window, shape_color, shape_rect)
pygame.display.flip()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                movement_x = -movement_speed
            elif event.key == pygame.K_RIGHT:
                movement_x = movement_speed
            elif event.key == pygame.K_UP:
                movement_y = -movement_speed
            elif event.key == pygame.K_DOWN:
                movement_y = movement_speed
        else:
            movement_x = 0
            movement_y = 0

    shape_rect.x += movement_x
    shape_rect.y += movement_y

    window.fill(background_color)
    pygame.draw.rect(window, shape_color, shape_rect)
    pygame.display.flip()

    clock.tick(60)  # Adjust the value to control frame rate

pygame.quit()
