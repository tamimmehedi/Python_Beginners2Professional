Just like we can have many different integers in a program, we can have many turtles. Each of them is called an
instance. Each instance has its own attributes and methods — so alex might draw with a thin black pen and be at
some position, while tess might be going in her own direction with a fat pink pen.

import turtle
window = turtle.Screen()
window.bgcolor("lightgreen")
window.title("Tess & Alex")
tess = turtle.Turtle()
tess.color("hotpink")
tess.pensize(5) # Create tess and set some attributes
alex = turtle.Turtle() # Create alex
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)
tess.left(120) # Complete the triangle
tess.right(180)
tess.forward(80) # Turn tess around
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90) # Make alex draw a square
window.mainloop()

