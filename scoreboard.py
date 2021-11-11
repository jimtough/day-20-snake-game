from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 18, "normal")
HIGH_SCORE_FILENAME = "data.txt"


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.read_high_score()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color("white")
        self.update_scoreboard()

    def read_high_score(self):
        with open(HIGH_SCORE_FILENAME) as file:
            high_score_text = file.read()
            self.high_score = int(high_score_text)

    def write_high_score(self):
        with open(HIGH_SCORE_FILENAME, mode="w") as file:
            file.write(f"{self.high_score}")

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_high_score()
        self.update_scoreboard()
        self.score = 0

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()

