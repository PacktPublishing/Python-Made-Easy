import pygame
import random

# Define colors
BLACK = (0, 0, 0)  # RGB value for black
BLUE = (0, 0, 255)  # RGB value for blue
RED = (255, 0, 0)  # RGB value for red
YELLOW = (255, 255, 0)  # RGB value for yellow
WHITE = (255, 255, 255)  # RGB value for white
GREEN = (0, 255, 0)  # RGB value for green
ORANGE = (255, 165, 0)  # RGB value for orange
PURPLE = (128, 0, 128)  # RGB value for purple
PINK = (255, 105, 180)  # RGB value for pink

# Define constants
WIDTH = 800  # Width of the game window
HEIGHT = 600  # Height of the game window
PADDLE_WIDTH = 100  # Width of the paddle
PADDLE_HEIGHT = 10  # Height of the paddle
BALL_RADIUS = 10  # Radius of the ball
BRICK_WIDTH = 100  # Width of each brick
BRICK_HEIGHT = 30  # Height of each brick
BRICK_ROWS = 5  # Number of rows of bricks
BRICK_COLS = 8  # Number of columns of bricks

pygame.init()  # Initialize pygame
window = pygame.display.set_mode((WIDTH, HEIGHT))  # Create the game window
pygame.display.set_caption("Breakout Game")  # Set the title of the game window
clock = pygame.time.Clock()  # Create a clock object to control the frame rate
font = pygame.font.Font(None, 30)  # Create a font object for rendering text

# Define class to represent the paddle inheriting from the built in Sprite class
class Paddle(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((PADDLE_WIDTH, PADDLE_HEIGHT))  # Create a surface for the paddle
        self.image.fill(BLUE)  # Fill the paddle surface with the blue color
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the paddle surface
        self.rect.x = (WIDTH - PADDLE_WIDTH) // 2  # Set the initial x-coordinate of the paddle
        self.rect.y = HEIGHT - 50  # Set the initial y-coordinate of the paddle

# Define class to represent the ball inheriting from the built in Sprite class
class Ball(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((BALL_RADIUS * 2, BALL_RADIUS * 2), pygame.SRCALPHA)  # Create a surface for the ball
        pygame.draw.circle(self.image, RED, (BALL_RADIUS, BALL_RADIUS), BALL_RADIUS)  # Draw a red circle on the ball surface
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the ball surface
        self.rect.x = WIDTH // 2  # Set the initial x-coordinate of the ball
        self.rect.y = HEIGHT // 2  # Set the initial y-coordinate of the ball
        self.speed_x = random.choice([-2, 2])  # Set the initial x-axis speed of the ball randomly as -2 or 2
        self.speed_y = -2  # Set the initial y-axis speed of the ball as -2

    def update(self):
        self.rect.x += self.speed_x  # Update the x-coordinate of the ball based on its x-axis speed
        self.rect.y += self.speed_y  # Update the y-coordinate of the ball based on its y-axis speed

        # Collision detection with walls
        if self.rect.x < 0 or self.rect.x > WIDTH - BALL_RADIUS * 2:  # If the ball hits the left or right wall
            self.speed_x *= -1  # Reverse the x-axis speed of the ball
        if self.rect.y < 0:  # If the ball hits the top wall
            self.speed_y *= -1  # Reverse the y-axis speed of the ball

        # Collision detection with paddle
        if self.rect.colliderect(paddle.rect):  # If the ball collides with the paddle
            self.speed_y *= -1  # Reverse the y-axis speed of the ball

        # Collision detection with bricks
        collided_bricks = pygame.sprite.spritecollide(self, bricks, True)  # Check for collision between the ball and the bricks
        if collided_bricks:  # If the ball collides with any brick
            self.speed_y *= -1  # Reverse the y-axis speed of the ball

        # Check game over conditions
        if self.rect.y > HEIGHT:  # If the ball goes below the screen
            return True  # Signal that the game is over

# Define class to represent a single brick inheriting from the built in Sprite class
class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((BRICK_WIDTH, BRICK_HEIGHT))  # Create a surface for the brick
        self.image.fill(color)  # Fill the brick surface with the specified color
        self.rect = self.image.get_rect()  # Get the rectangle that encloses the brick surface
        self.rect.x = x  # Set the x-coordinate of the brick
        self.rect.y = y  # Set the y-coordinate of the brick




# MAIN PROGRAM        

paddle = Paddle()  # Create the paddle object
ball = Ball()  # Create the ball object
bricks = pygame.sprite.Group()  # Create a group to hold the bricks

for row in range(BRICK_ROWS):  # Iterate over the rows of bricks
    for col in range(BRICK_COLS):  # Iterate over the columns of bricks
        brick_x = col * BRICK_WIDTH  # Calculate the x-coordinate of the brick
        brick_y = row * BRICK_HEIGHT  # Calculate the y-coordinate of the brick
        brick_color = random.choice([BLUE, RED, YELLOW, GREEN, ORANGE, PURPLE, PINK])  # Choose a random color for the brick
        brick = Brick(brick_x, brick_y, brick_color)  # Create a brick object
        bricks.add(brick)  # Add the brick to the group of bricks

all_sprites = pygame.sprite.Group()  # Create a group to hold all sprites
all_sprites.add(paddle, ball, bricks)  # Add the paddle, ball, and bricks to the group of sprites

score = 0  # Initialize the score
game_over = False  # Variable to control the game loop

pygame.key.set_repeat(50, 10)  # Sets a delay of 50 milliseconds and an interval of 10 milliseconds for key repetition

# Game loop
while not game_over:
    # Event loop
    for event in pygame.event.get():  # Check for events
        if event.type == pygame.QUIT:  # If the user closes the window
            game_over = True  # End the game loop
        elif event.type == pygame.KEYDOWN:  # If a key is pressed
            if event.key == pygame.K_LEFT:  # If the left arrow key is pressed
                paddle.rect.x -= 10  # Move the paddle to the left
            elif event.key == pygame.K_RIGHT:  # If the right arrow key is pressed
                paddle.rect.x += 10  # Move the paddle to the right

    all_sprites.update()  # Update all sprites

    if ball.update():  # Update the ball and check if the game is over
        game_over = True  # End the game loop

    window.fill(BLACK)  # Fill the window with the black color (clear screen)
    all_sprites.draw(window)  # Draw all sprites on the window
    score_text = font.render("Score: " + str(score), True, WHITE)  # Render the score text
    window.blit(score_text, (10, 10))  # Display the score text on the window
    pygame.display.update()  # Update the contents of the window
    clock.tick(60)  # Limit the frame rate to 60 FPS
    

# Game over
game_over_text = font.render("Game Over", True, WHITE)  # Render the game over text
window.blit(game_over_text, (WIDTH // 2 - 50, HEIGHT // 2))  # Display the game over text on the window
pygame.display.update()  # Update the contents of the window
