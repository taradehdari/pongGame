
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
# paddle B

# Ball

#main game loop
while True:
    wn.update()
