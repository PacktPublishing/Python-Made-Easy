import turtle

# Create a turtle object
my_turtle = turtle.Turtle()


for sides in range(6):
    my_turtle.forward(100)
    my_turtle.right(60)

my_turtle.penup()
my_turtle.setpos(46, 146)
my_turtle.pendown()

for counter in range(5):
    my_turtle.right(144)
    my_turtle.forward(100)


# Close the turtle graphics window
turtle.done()
