from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.xdist = 10
        self.ydist = 10
        self.ball_speed = 0.2

    def move(self):
        new_x = self.xcor() + self.xdist
        new_y = self.ycor() + self.ydist
        self.setpos(new_x, new_y)

    def bounce_y(self):
        self.ydist *= -1
        self.move()

    def bounce_x(self):
        self.xdist *= -1
        self.move()
        self.ball_speed *= 0.9

    def reset_position(self):
        self.home()
        self.ball_speed = 0.2
        self.bounce_x()
