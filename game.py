import turtle
from pieces import Paddle, Ball, Score

window = turtle.Screen()
window.title("Pong by Derek Robinson")
window.bgcolor("black")
window.setup(width=800, height=600)

# Paddle A
paddle_a = Paddle(-350, 0)

# Paddle B
paddle_b = Paddle(350, 0)

# Ball
ball = Ball()

#Pen
score = Score()

#Keyboard Binding
window.listen()
window.onkeypress(paddle_a.move_up, "w")
window.onkeypress(paddle_a.move_down, "s")
window.onkeypress(paddle_b.move_up, "Up")
window.onkeypress(paddle_b.move_down, "Down")

# Main game loop
while True:
    score_one = 0
    score_two = 0
    window.update()

    # Move the ball
    ball.move()

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_one += 1
        pen.clear()
        score.update(score_one, score_two)

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_two += 1
        pen.clear()
        score.update(score_one, score_two)

    # paddle and ball collisions
    if (340 < ball.xcor() < 350 and ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1

    if (-340 > ball.xcor() > -350 and ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1