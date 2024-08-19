import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# Function to draw the Koch Snowflake
def draw_koch_snowflake(length, level):
    if level == 0:
        my_turtle.forward(length)
    else:
        for angle in [60, -120, 60, 0]:
            draw_koch_snowflake(length/3, level-1)
            my_turtle.left(angle)

# Set turtle attributes
my_turtle.speed(0)  # Set the fastest speed

# Move turtle to starting position
my_turtle.penup()
my_turtle.goto(-150, 150)
my_turtle.pendown()

# Draw the Koch Snowflake
for _ in range(3):
    draw_koch_snowflake(300, 4)
    my_turtle.right(120)

turtle.done()
