import pygame
import random

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

class Bullet:
    def __init__(self, screen, rocket):
        self.screen = screen
        self.image = pygame.image.load("bullet.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = rocket.rect.centerx
        self.rect.bottom = rocket.rect.top

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move(self):
        self.rect.y -= 10

class UFO:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.image.load("ufo.png")
        self.image = pygame.transform.scale(self.image, (70, 50))
        self.rect = self.image.get_rect()
        self.reset_position()

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def reset_position(self):
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, self.screen.get_height() // 2 - self.rect.height)



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

# Create a bullet object
bullet = Bullet(screen, rocket)
bullet_state = "ready"  # Indicates whether the bullet is ready to be fired or in motion

# Create a UFO object
ufo = UFO(screen)

# Game loop.
running = True
while running:
    # Execute loop at 25 frames per second
    clock.tick(25)

    # Clear the screen and add the background image.
    screen.blit(background, (0, 0))

    # Event handling.
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                rocket.move_left()
            elif event.key == pygame.K_RIGHT:
                rocket.move_right()
            elif event.key == pygame.K_SPACE:
                if bullet_state == "ready":
                    bullet_state = "fire"
                    bullet.rect.centerx = rocket.rect.centerx
                    bullet.rect.bottom = rocket.rect.top

    # Draw the rocket
    rocket.draw()

    # Draw the UFO
    ufo.draw()

    # Bullet movement
    if bullet_state == "fire":
        bullet.move()
        bullet.draw()
        if bullet.rect.bottom < 0:
            bullet_state = "ready"



    # Update the screen
    pygame.display.update()

pygame.quit()

