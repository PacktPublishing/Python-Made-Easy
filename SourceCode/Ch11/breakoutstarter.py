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

'''
Define a Paddle class
    Initialize the paddle object
    Set the initial position and size of the paddle
    
Define a Ball class
    Initialize the ball object
    Set the initial position, size, and speed of ball
    Update the ball position based on speed 
    Handle collisions with walls, paddle & bricks
    
Define a Brick class
    Initialize a brick object with position & color

Create the paddle object
Create the ball object
Create a group to hold the bricks

Create bricks by iterating over rows and columns
    Calculate the position of each brick
    Choose a random color for each brick
    Create a brick object with the calculated 
    position and chosen color
    Add the brick to the group of bricks
    
Create a group to hold all sprites
Add the paddle, ball, and bricks to the group of sprites

Initialize the score and game_over variables

Set key repetition delay and interval

Game loop
    Handle events (e.g., window close, key presses)
    Update all sprites and check for game over
    Clear the screen
    Draw all sprites on the window
    Render and display the score text
    Update the window
    Limit the frame rate
Display “Game Over” text
'''





# Quit the game
pygame.quit()
