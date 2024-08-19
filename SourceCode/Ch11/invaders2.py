import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the game window
WIDTH = 800
HEIGHT = 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Invaders")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Bullet dimensions
bullet_width = 10
bullet_height = 20

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("rocket.png")
        self.image = pygame.transform.scale(self.image, (40, 70))  # Resize player image
        self.rect = self.image.get_rect()
        self.rect.x = WIDTH // 2 - self.rect.width // 2
        self.rect.y = HEIGHT - self.rect.height - 10
        self.speed = 5

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and self.rect.x > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.x < WIDTH - self.rect.width:
            self.rect.x += self.speed

    def shoot(self):
        bullet = Bullet(self.rect.x + self.rect.width // 2 - bullet_width // 2, self.rect.y)
        all_sprites.add(bullet)
        bullets.add(bullet)

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill((255, 255, 0))  # Fill with yellow color
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()

# Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("ufo.png")
        self.image = pygame.transform.scale(self.image, (40, 30))  # Resize enemy image
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.direction = 1
        self.bomb_timer = 0

    def drop_bomb(self):
        bomb = Bomb(self.rect.x + self.rect.width // 2 - bullet_width // 2, self.rect.y + self.rect.height)
        all_sprites.add(bomb)
        bombs.add(bomb)

    def update(self):
        self.rect.x += self.speed * self.direction

        if self.rect.right >= WIDTH or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += self.rect.height

        # Bomb dropping logic
        self.bomb_timer += 1
        if self.bomb_timer >= random.randint(1, 99999):  # Adjust the bomb drop frequency as desired
            self.drop_bomb()
            self.bomb_timer = 0

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((bullet_width, bullet_height))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5

    def update(self):
        self.rect.y += self.speed
        if self.rect.y > HEIGHT:
            self.kill()

# Group for all sprites
all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
enemies = pygame.sprite.Group()
bombs = pygame.sprite.Group()

# Create player
player = Player()
all_sprites.add(player)

# Create enemies
enemy_width = 40
enemy_height = 30
for row in range(5):
    for column in range(10):
        enemy = Enemy(column * (enemy_width + 10) + 50, row * (enemy_height + 10) + 50)
        all_sprites.add(enemy)
        enemies.add(enemy)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.shoot()

    # Update sprites
    all_sprites.update()

    # Update bombs
    bombs.update()

    # Collision detection
    hits = pygame.sprite.groupcollide(enemies, bullets, True, True)

    # Create new enemies after all are destroyed
    if len(enemies) == 0:
        for row in range(5):
            for column in range(10):
                enemy = Enemy(column * (enemy_width + 10) + 50, row * (enemy_height + 10) + 50)
                all_sprites.add(enemy)
                enemies.add(enemy)

    # Draw the elements
    window.fill(BLACK)
    all_sprites.draw(window)
    bombs.draw(window)

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
