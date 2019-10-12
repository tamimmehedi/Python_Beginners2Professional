Let’s write a couple of lines of Python program to create a new turtle and start drawing a rectangle.
 
import turtle             # Allows us to use turtles
window = turtle.Screen()  # Creates a playground for turtles
alex = turtle.Turtle()    # Creates a playground for turtles

alex.forward(50)          # Tell alex to turn by 90 degrees
alex.left(90)             # Complete the second side of a rectangle
alex.forward(30)          # Tell alex to move forward by 50 units
window.mainloop()         # Wait for user to close window

import turtle
window = turtle.Screen()     # Set the window background color
window.bgcolor("lightgreen") # Set the window title
window.title("Hello, Tess!")

tess = turtle.Turtle()
tess.color("blue")          # Tell tess to change her color
tess.pensize(3)             # Tell tess to set her pen width

tess.forward(50)
tess.left(120)

tess.forward(50)
window.mainloop()

