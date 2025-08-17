import turtle
import time

print("Credit: https://www.geeksforgeeks.org/create-pong-game-using-python-turtle/")
print("(Note: This version has been edited for smoother gameplay.)")
print("Use 'W' and 'S' to control the left paddle, and the arrow keys for the right paddle.")
time.sleep(2)

# Create screen
sc = turtle.Screen()
sc.title("Pong Game")
sc.bgcolor("white")
sc.setup(width=1000, height=600)
sc.tracer(0)  # Disable auto screen updates for smooth animation

# Left paddle
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Right paddle
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Ball
hit_ball = turtle.Turtle()
hit_ball.speed(4)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Score initialization
left_player = 0
right_player = 0

# Score display
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write("Left_player : 0    Right_player: 0",
             align="center", font=("Courier", 24, "normal"))

# Paddle movement functions
def paddleaup():
    y = left_pad.ycor()
    if y < 250:
        left_pad.sety(y + 20)

def paddleadown():
    y = left_pad.ycor()
    if y > -240:
        left_pad.sety(y - 20)

def paddlebup():
    y = right_pad.ycor()
    if y < 250:
        right_pad.sety(y + 20)

def paddlebdown():
    y = right_pad.ycor()
    if y > -240:
        right_pad.sety(y - 20)

# Keyboard bindings
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")
sc.onkeypress(paddlebup, "Up")
sc.onkeypress(paddlebdown, "Down")

# Update score display
def update_score():
    sketch.clear()
    sketch.write(f"Left_player : {left_player}    Right_player: {right_player}",
                 align="center", font=("Courier", 24, "normal"))

# Main game loop
def game_loop():
    global left_player, right_player

    # Move the ball
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Bounce off top and bottom
    if hit_ball.ycor() > 280:
        hit_ball.sety(280)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -280:
        hit_ball.sety(-280)
        hit_ball.dy *= -1

    # Right player misses
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        update_score()

    # Left player misses
    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        update_score()

    # Paddle collision
    if (360 < hit_ball.xcor() < 370) and \
       (right_pad.ycor() - 50 < hit_ball.ycor() < right_pad.ycor() + 50):
        hit_ball.setx(360)
        hit_ball.dx *= -1

    if (-370 < hit_ball.xcor() < -360) and \
       (left_pad.ycor() - 50 < hit_ball.ycor() < left_pad.ycor() + 50):
        hit_ball.setx(-360)
        hit_ball.dx *= -1

    sc.update()
    sc.ontimer(game_loop, 10)  # Run every 10ms

# Start game loop
game_loop()

# Keep window open
turtle.mainloop()
