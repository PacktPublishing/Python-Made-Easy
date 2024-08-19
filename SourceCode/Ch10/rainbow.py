import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for color in colors:
    my_turtle.color(color)
    my_turtle.circle(100)
    my_turtle.right(60)

turtle.done()
