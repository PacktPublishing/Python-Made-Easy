import pygame

class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill((0, 255, 0))  # Green color for the platform
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((40, 40))
        self.image.fill((255, 0, 0))  # Red color for the player
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 100
        self.vel_x = 0
        self.vel_y = 0
        self.gravity = 0.5

    def update(self):
        self.rect.x += self.vel_x
        self.rect.y += self.vel_y

        self.vel_y += self.gravity

class GameWindow:
    def __init__(self, width, height):
        pygame.init()
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Platformer Game")
        self.clock = pygame.time.Clock()

        self.background_color = (135, 206, 250)  # Sky Blue color

        self.all_sprites = pygame.sprite.Group()
        self.platforms = pygame.sprite.Group()

        self.player = Player()
        self.all_sprites.add(self.player)

        self.create_platforms()

    def create_platforms(self):
        platforms_data = [
            (0, self.height - 40, self.width, 40),
            (200, 400, 200, 20),
            (400, 300, 200, 20),
            (600, 200, 200, 20),
        ]

        for data in platforms_data:
            platform = Platform(*data)
            self.all_sprites.add(platform)
            self.platforms.add(platform)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.player.vel_y = -12  # Jumping
                    elif event.key == pygame.K_LEFT:
                        self.player.vel_x = -5  # Move left
                    elif event.key == pygame.K_RIGHT:
                        self.player.vel_x = 5  # Move right
                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.player.vel_x = 0  # Stop horizontal movement

            self.update()
            self.render()

            pygame.display.flip()
            self.clock.tick(60)  # Limit frame rate to 60 FPS

        pygame.quit()

    def update(self):
        self.all_sprites.update()

        # Collision check between player and platforms
        if pygame.sprite.spritecollide(self.player, self.platforms, False):
            self.player.vel_y = 0
            self.player.rect.y -= 1  # Move player slightly up to avoid getting stuck

    def render(self):
        self.screen.fill(self.background_color)
        self.all_sprites.draw(self.screen)

# Create an instance of the GameWindow class and run the game
game = GameWindow(800, 600)
game.run()
