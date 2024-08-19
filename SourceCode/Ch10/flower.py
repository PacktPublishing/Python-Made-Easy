import turtle

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

for _ in range(36):
    for _ in range(2):
        my_turtle.forward(100)
        my_turtle.right(60)
        my_turtle.forward(100)
        my_turtle.right(120)
    my_turtle.right(10)

turtle.done()
