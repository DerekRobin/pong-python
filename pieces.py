from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, pos_x, pos_y):
        super().__init__(shape='square')
        self.color('White')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.speed(0)
        self.goto(pos_x, pos_y)

    def move_up(self):
        y = self.ycor()
        y += 20
        self.sety(y)

    def move_down(self):
        y = self.ycor()
        y -= 20
        self.sety(y)

class Ball(Turtle):
    def __init__(self):
        super().__init__(shape='square')
        self.color('White')
        self.penup()
        self.speed(0)
        self.goto(0, 0)
        self.dx = 6
        self.dy = 6

    def move(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write("Player 1: 0  Player 2: 0", align = "center", font = ("Courier", 24, "normal"))

    def update(self, score_one, score_two):
        self.write("Player 1: {}  Player 2: {}".format(score_one, score_two), align = "center", font = ("Courier", 24, "normal"))
        