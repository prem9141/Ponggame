from turtle import Turtle

SCORE_ALIGN = "center"
SCORE_FONT = ("courier", 30, "bold")
LEFT_SCOREBOARD_XPOS = -100
SCOREBOARD_YPOS = 255
RIGHT_SCOREBOARD_XPOS = 100


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.lscore = 0
        self.rscore = 0
        self.display_score()

    def update_lscore(self):
        self.lscore += 1
        self.display_score()

    def update_rscore(self):
        self.rscore += 1
        self.display_score()

    def display_score(self):
        self.clear()
        self.setpos(LEFT_SCOREBOARD_XPOS, SCOREBOARD_YPOS)
        self.write(f"{self.lscore}", False, SCORE_ALIGN, SCORE_FONT)
        self.setpos(RIGHT_SCOREBOARD_XPOS, SCOREBOARD_YPOS)
        self.write(f"{self.rscore}", False, SCORE_ALIGN, SCORE_FONT)

    def reset_score(self):
        self.lscore = 0
        self.rscore = 0
        self.display_score()

    def final_score(self):
        self.clear()
        self.home()
        winner = f"GAME OVER !!! Left Player wins"
        if self.lscore < self.rscore:
            winner = f"GAME OVER !!! Right Player wins"
        self.write(winner, False, SCORE_ALIGN, ("courier", 20, "bold"))
