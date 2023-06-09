
# turtle used for adding graphics and opening window can also use pygames but for simple games turtle is good to get started

import turtle
import winsound

# create a window
wn = turtle.Screen()
# name window
wn.title("Pong by Tara")
# background color
wn.bgcolor("black")
# size of window
wn.setup(width=800, height=600)
# stops window from updating speeds game up
wn.tracer(0)

# Score
score_a = 0
score_b = 0

# creating paddle A
paddle_a = turtle.Turtle()
# speed of animation something need to do with turtle this sets to maximum speed
paddle_a.speed(0)

paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

# creating paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

# Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 0.1
ball.dy = 0.1 # every time ball moves it moves by two pixels (up 2 (y) and right 2 (x))

# Pen (just a turtle like the ball and paddle)
pen = turtle.Turtle()
pen.speed(0) #animation speed not movement speed
pen.color("white")
pen.penup() #so we dont have a line when pen moves
pen.hideturtle() # because we do not wanna see it on screen just wanna see text it will write
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function
# in this case we want to move paddles up and down
def paddle_a_up():
    y = paddle_a.ycor()  # .ycor() is from turtle method and returns the y location
    if(y < 250): #so paddle doesnt go off screen
        y += 20  # adds 20 to y (adds 20 pixels to y coordinate)
        paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    if(y > -250):
        y -= 20
        paddle_a.sety(y)
def paddle_b_up():
    y = paddle_b.ycor()
    if(y < 250):
        y += 20
        paddle_b.sety(y)
def paddle_b_down():
    y = paddle_b.ycor()
    if(y > -250):
        y -= 20
        paddle_b.sety(y)
# keyboard binding
wn.listen() # says listen to keyboard input
wn.onkeypress(paddle_a_up, "w")   # when user presses w call function paddle_a_up, paddle_a_up says go up 20 units and set to new location
wn.onkeypress(paddle_a_down, "s")
wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")
# main game loop
while True:
    wn.update()

    # move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1  # reverses the direction

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1  # reverses the direction

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear() #clears what is on screen so the score doesnt overlap on top of the zero happens so fast we dont see it
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear() 
        pen.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center", font=("Courier", 24, "normal"))

    # paddle and ball collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC) # the snd_async will play song in background so that the sound doesnt stop the game and plays while game goes on 

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        winsound.PlaySound("bounce.mp3", winsound.SND_ASYNC)
