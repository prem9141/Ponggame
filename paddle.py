from turtle import Turtle

STRETCH_WIDTH = 5
STRETCH_HEIGHT = 1
MAX_UP_POS = 240
MAX_DOWN_POS = -220
MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos, color):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.resizemode("user")
        self.shapesize(STRETCH_WIDTH, STRETCH_HEIGHT)
        self.penup()
        self.setpos(x_pos, y_pos)

    def move_up(self):
        if self.ycor() < MAX_UP_POS:
            self.setpos(self.xcor(), self.ycor() + MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > MAX_DOWN_POS:
            self.setpos(self.xcor(), self.ycor() - MOVE_DISTANCE)
