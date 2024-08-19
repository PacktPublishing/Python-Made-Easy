import turtle
import colorsys

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

# Set turtle attributes
my_turtle.speed(0)  # Set the fastest speed
my_turtle.width(3)

# Move turtle to starting position
my_turtle.penup()
my_turtle.goto(0, -200)
my_turtle.pendown()

# Function to draw a starburst pattern
def draw_starburst(length, num_rays):
    angle = 360 / num_rays

    for _ in range(num_rays):
        my_turtle.forward(length)
        my_turtle.backward(length)
        my_turtle.right(angle)

# Draw the starburst pattern
for i in range(36):
    # Set color based on current angle
    hue = i / 36.0
    rgb = colorsys.hsv_to_rgb(hue, 1.0, 1.0)
    my_turtle.color(rgb)
    
    draw_starburst(200, 12)
    my_turtle.right(11)

turtle.done()
