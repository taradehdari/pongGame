# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

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

#main game loop
while True:
    wn.update()