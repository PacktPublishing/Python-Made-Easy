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

        self.explosion_image = pygame.image.load("explosion.png")
        self.explosion_image = pygame.transform.scale(self.explosion_image, (70, 70))
        self.explosion_rect = self.explosion_image.get_rect()
        self.explosion_timer = 0

        self.speed_x = 5  # Adjust the horizontal speed of UFO movement
        self.speed_y = 5  # Adjust the vertical speed of UFO movement

    def draw(self):
        if self.explosion_timer > 0:
            self.screen.blit(self.explosion_image, self.explosion_rect)
            self.explosion_timer -= 1
        else:
            self.screen.blit(self.image, self.rect)

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        # Check for collision with the screen edges
        if self.rect.left <= 0 or self.rect.right >= self.screen.get_width():
            self.speed_x *= -1  # Reverse horizontal direction
        if self.rect.top <= 0 or self.rect.bottom >= self.screen.get_height():
            self.speed_y *= -1  # Reverse vertical direction

    def reset_position(self):
        self.rect.x = random.randint(0, self.screen.get_width() - self.rect.width)
        self.rect.y = random.randint(0, self.screen.get_height() - self.rect.height)

    def explode(self):
        self.explosion_rect.center = self.rect.center
        self.explosion_timer = 10


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

    # Update and draw the UFO
    ufo.update()
    ufo.draw()

    # Bullet movement
    if bullet_state == "fire":
        bullet.move()
        bullet.draw()
        if bullet.rect.bottom < 0:
            bullet_state = "ready"

    # Check for collision between bullet and UFO
    if bullet_state == "fire" and bullet.rect.colliderect(ufo.rect):
        bullet_state = "ready"
        ufo.explode()
        ufo.reset_position()

    # Update the screen
    pygame.display.update()

pygame.quit()
