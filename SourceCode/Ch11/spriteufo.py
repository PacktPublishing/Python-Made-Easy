import pygame
import os

class UFO(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.images = []
        self.index = 0
        self.animation_speed = 5
        self.load_images()
        self.image = self.images[self.index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.animation_count = 0

    def load_images(self):
        # Specify the directory containing the UFO sprite frames
        directory = "ufo_frames"
        frame_files = os.listdir(directory)
        frame_files.sort()

        for filename in frame_files:
            image = pygame.image.load(os.path.join(directory, filename)).convert_alpha()
            self.images.append(image)

    def update(self):
        self.animation_count += 1

        if self.animation_count >= self.animation_speed:
            self.index = (self.index + 1) % len(self.images)
            self.image = self.images[self.index]
            self.animation_count = 0

class GameWindow:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("My Game")

        # Create sprite groups
        self.all_sprites = pygame.sprite.Group()
        self.ufos = pygame.sprite.Group()

        # Create the UFO sprite and add it to the groups
        ufo = UFO(self.width // 2, self.height // 2)
        self.all_sprites.add(ufo)
        self.ufos.add(ufo)

    def run(self):
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            # Update all sprites
            self.all_sprites.update()

            # Fill the background
            self.screen.fill((0, 0, 0))

            # Draw all sprites onto the screen
            self.all_sprites.draw(self.screen)

            pygame.display.flip()  # Update the window display

        pygame.quit()  # Close the Pygame window and exit the game

# Create an instance of the GameWindow class and run the game
game = GameWindow(800, 600)
game.run()
