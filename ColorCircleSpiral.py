# ColorCircleSpiral.py
# Billy Ridgeway
# Draws colorful spiral of circles.

import turtle                       # Imports turtle graphics.
t = turtle.Pen()                    # Creates a new turtle called t.
turtle.bgcolor("black")             # Sets the background to black.
t.speed(0)                          # Sets the speed of the pen to fast.

# Creates a list of colors to be used in the drawing.
colors = ["red", "yellow", "blue", "green"]

for x in range (200):               # Sets the variable 'x' to 200.
    t.pencolor( colors[ x % 4] )    # Cycles through the list of colors.
    t.circle(x)                     # Draws 200 circles.
    t.left(95)                      # Move the pen left by 95 degrees.
