import turtle

my_window = turtle.Screen()
my_window.bgcolor("light blue")
my_window.title("Him Turtle")

my_turtle = turtle.Turtle()
size = 0

while True:
    for i in range(4):
        my_turtle.fd(size + 1)
        my_turtle.left(90)
        size = size - 5
    size = size + 1

turtle.done()
