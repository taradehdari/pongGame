
#turtle used for adding graphics and opening window can also use pygames but for simple games turtle is good to get started

import turtle

#create a window
wn = turtle.Screen()
#name window
wn.title("Pong by Tara")
#background color
wn.bgcolor("black")
#size of window
wn.setup(width=800, height=600)
#stops window from updating speeds game up
wn.tracer(0)

## creating paddle A
paddle_a = turtle.Turtle()
#speed of animation something need to do with turtle this sets to maximum speed
paddle_a.speed(0)

paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

## creating paddle B
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

# Function
# in this case we want to move paddles up and down
def paddle_a_up():
    y = paddle_a.ycor() #.ycor() is from turtle method and returns the y location
    y += 20 #adds 20 to y (adds 20 pixels to y coordinate)
    paddle_a.sety(y)
def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)
#keyboard binding
wn.listen() # says listen to keyboard input
wn.onkeypress(paddle_a_up, "w") # when user presses w call function paddle_a_up, paddle_a_up says go up 20 units and set to new location
wn.onkeypress(paddle_a_down, "s")


#main game loop
while True:
    wn.update()
