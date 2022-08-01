import turtle


object_ = turtle.Turtle()
screen = turtle.Screen()


def forward():
    object_.forward(10)


def backward():
    object_.backward(10)


def counter_clockwise():
    object_.right(10)


def clockwise():
    object_.left(10)


def clear_drawing():
    object_.reset()


def draw():
    screen.listen()
    screen.onkey(key="Up", fun=forward)
    screen.onkey(key="Down", fun=backward)
    screen.onkey(key="Left", fun=counter_clockwise)
    screen.onkey(key="Right", fun=clockwise)
    screen.onkey(key="C", fun=clear_drawing)


draw()
screen.exitonclick()