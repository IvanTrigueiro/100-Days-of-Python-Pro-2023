from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, location):
        super().__init__()
        self.location = location
        self.shape("square")
        self.penup()
        self.color("white")
        self.goto(location)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
