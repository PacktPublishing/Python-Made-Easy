import turtle

# Create a turtle object
my_turtle = turtle.Turtle()

# Set the initial color and size
my_turtle.pensize(2)
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

# Draw the spiral pattern
for i in range(360):
    my_turtle.pencolor(colors[i % len(colors)])
    my_turtle.forward(i)
    my_turtle.left(59)

# Close the turtle graphics window
turtle.done()
