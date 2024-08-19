import pygame
import random

# Initialize pygame
pygame.init()

# Create the game window
window_width = 800
window_height = 600
window = pygame.display.set_mode((window_width, window_height))

# Set the title of the game window
pygame.display.set_caption("Brick Breaker")

# Create a clock object for frame rate control
clock = pygame.time.Clock()

# Create a font object for rendering text
font = pygame.font.Font(None, 36)

# Define a Paddle class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((100, 20))  # Create a surface for the paddle image
        self.image.fill((255, 255, 255))        # Fill the paddle image with white color
        self.rect = self.image.get_rect()       # Get the rectangle of the paddle image
        self.rect.centerx = window_width // 2   # Set the initial x-coordinate of the paddle
        self.rect.bottom = window_height - 10   # Set the initial y-coordinate of the paddle
        self.speed = 5                          # Set the speed of the paddle

    def update(self):
        keys = pygame.key.get_pressed()         # Get the state of all keyboard keys
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed           # Move the paddle to the left
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed           # Move the paddle to the right
        self.rect.clamp_ip(window.get_rect())   # Keep the paddle within the game window

# Define a Ball class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.radius = 10  # Set the radius of the ball
        self.image = pygame.Surface((self.radius * 2, self.radius * 2), pygame.SRCALPHA)          # Create a surface for the ball image with alpha transparency
        pygame.draw.circle(self.image, (255, 255, 255), (self.radius, self.radius), self.radius)  # Draw a white circle on the surface
        self.rect = self.image.get_rect()       # Get the rectangle of the ball image
        self.rect.centerx = window_width // 2   # Set the initial x-coordinate of the ball
        self.rect.centery = window_height // 2  # Set the initial y-coordinate of the ball
        self.speed_x = random.choice([-2, 2])   # Set the initial x-axis speed of the ball
        self.speed_y = -2                       # Set the initial y-axis speed of the ball

    def update(self):
        self.rect.x += self.speed_x  # Move the ball horizontally
        self.rect.y += self.speed_y  # Move the ball vertically

        if self.rect.left <= 0 or self.rect.right >= window_width:
            self.speed_x *= -1       # Reverse the horizontal speed when the ball hits the sides
        if self.rect.top <= 0:
            self.speed_y *= -1       # Reverse the vertical speed when the ball hits the top

        if pygame.sprite.collide_rect(self, paddle):
            self.speed_y *= -1       # Reverse the vertical speed when the ball hits the paddle

# Define a Brick class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((80, 20))  # Create a surface for the brick image
        self.image.fill(color)                 # Fill the brick image with the specified color
        self.rect = self.image.get_rect()      # Get the rectangle of the brick image
        self.rect.x = x                        # Set the x-coordinate of the brick
        self.rect.y = y                        # Set the y-coordinate of the brick

# Create the paddle object
paddle = Paddle()

# Create the ball object
ball = Ball()

# Create a group to hold the bricks
bricks_group = pygame.sprite.Group()

# Create bricks by iterating over rows and columns
rows = 5                                                 # 5 rows of bricks
columns = 10                                             # 10 columns of bricks
brick_width = 80                                         # width of an individual brick in pixels
brick_height = 20                                        # height of an individual brick in pixels
brick_group_width = columns * brick_width                # total horizontal space occupied by the bricks.
brick_group_height = rows * brick_height                 # total vertical space occupied by the bricks.
brick_group_x = (window_width - brick_group_width) // 2  # calculates the x-coordinate of the top-left corner of the brick group
brick_group_y = 50                                       # y-coordinate of the top-left corner of the brick group

for row in range(rows):                                  # iterates over the range of rows specified by the row variable
    for col in range(columns):                           # iterates over the range of columns specified by the col variable
        x = brick_group_x + col * brick_width            # x-coordinate of the top-left corner of the current brick being created
        y = brick_group_y + row * brick_height           # calculates the y-coordinate of the top-left corner of the current brick being created
        color = (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) # Generate a random color for the current brick.
        brick = Brick(x, y, color)                       # This line creates a new Brick object with the calculated position (x and y) and random color (color).
        bricks_group.add(brick)                          # adds the newly created brick to the bricks_group, which is a pygame.sprite.Group. The bricks_group is a collection that holds all the bricks together.

# Create a group to hold all sprites
all_sprites_group = pygame.sprite.Group()
all_sprites_group.add(paddle, ball, bricks_group)

# Initialize the score and game_over variables
score = 0
game_over = False

# Set key repetition delay and interval
pygame.key.set_repeat(1, 10)

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update all sprites and check for game over
    if not game_over:
        all_sprites_group.update()

        if ball.rect.bottom >= window_height:  #  If this condition is true, it means the ball has reached or crossed the bottom of the window,   
            game_over = True

        if len(bricks_group) == 0:             # If this condition is true, it means all the bricks have been destroyed (collided with the ball and removed)
            game_over = True

        if pygame.sprite.spritecollide(ball, bricks_group, True):  # checks for collisions between the ball sprite and any sprite in the bricks_group. 
            ball.speed_y *= -1                                     # if this is true the ball has hit the brick so we reverse the direction to bounce the ball
            score += 10                                            # increase score count by 10

    # Clear the screen
    window.fill((0, 0, 0))

    # Draw all sprites on the window
    all_sprites_group.draw(window)

    # Render and display the score text
    score_text = font.render("Score: " + str(score), True, (255, 255, 255))
    window.blit(score_text, (10, 10))

    # Update the window
    pygame.display.update()

    # Limit the frame rate
    clock.tick(60)

# Display "Game Over" text
game_over_text = font.render("Game Over", True, (255, 255, 255))
game_over_rect = game_over_text.get_rect(center=(window_width // 2, window_height // 2))
window.blit(game_over_text, game_over_rect)
pygame.display.update()

# Wait for a while before quitting
pygame.time.wait(2000)

# Quit the game
pygame.quit()
