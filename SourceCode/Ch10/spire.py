import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# Function to draw a square spiral
def draw_square_spiral(length, angle):
    for _ in range(36):
        my_turtle.forward(length)
        my_turtle.right(angle)
        length += 5

# Function to draw a complex pattern
def draw_pattern():
    for _ in range(8):
        draw_square_spiral(50, 90)
        my_turtle.right(45)

# Set turtle attributes
my_turtle.speed(0)  # Set the fastest speed
my_turtle.pensize(2)

# Move turtle to starting position
my_turtle.penup()
my_turtle.goto(-100, 100)
my_turtle.pendown()

# Draw the pattern
draw_pattern()

turtle.done()
