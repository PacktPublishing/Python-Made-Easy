import turtle

def draw_triangle(length):
    if length < 10:
        return
    else:
        for _ in range(3):
            turtle.forward(length)
            draw_triangle(length / 2)
            turtle.backward(length)
            turtle.right(120)

my_turtle = turtle.Turtle()
my_screen = turtle.Screen()

draw_triangle(200)

turtle.done()
