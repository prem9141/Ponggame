from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("The Pong Game")
screen.tracer(0)

right_paddle = Paddle(350, 0, "red")
left_paddle = Paddle(-350, 0, "blue")

ball = Ball()

screen.listen()
screen.onkey(right_paddle.move_up, "Up")
screen.onkey(right_paddle.move_down, "Down")

screen.onkey(left_paddle.move_up, "w")
screen.onkey(left_paddle.move_down, "s")

scoreboard = ScoreBoard()

is_game_over = False

while not is_game_over:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # Detect ball collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect ball collision with paddle
    if (ball.xcor() == 340 and ball.distance(right_paddle) < 43) or \
            (ball.xcor() == -340 and ball.distance(left_paddle) < 43):
        ball.bounce_x()

    # Detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.update_lscore()

    # Detect if left paddle misses the ball
    if ball.xcor() < -390:
        ball.reset_position()
        scoreboard.update_rscore()

    # Detect if player wins
    if scoreboard.lscore == 2 or scoreboard.rscore == 2:
        is_game_over = True
        scoreboard.final_score()


screen.exitonclick()
