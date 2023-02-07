from turtle import Turtle


class States_Name_Display:

    def __init__(self):
        self.turtle = Turtle()

    def write(self, x, y, state_name):
        self.turtle.hideturtle()
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.write(arg=state_name, font=('Arial', 8, 'normal'))