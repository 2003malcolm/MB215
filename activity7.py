import turtle
import tkinter.simpledialog as simpledialog
# Set up the window
turtle.Screen().setup(width=0.5, height=0.75, startx=None, starty=None)

# Create a turtle
turt = turtle.Turtle

# Set pen size to 3
turtle.pensize(3)

# Set drawing color to blue
turtle.pencolor('red')

# Move the turtle forward by 100 units
turtle.forward(100)

# Turn the turtle right by 90 degrees
turtle.right(90)

# Move the turtle forward by 50 units
turtle.forward(50)

# Turn the turtle left by 90 degrees
turtle.left(90)

# Lift the pen up – no drawing when moving
turtle.penup()

# Move the turtle to a specific location
turtle.goto(50,75)

# Put the pen down – drawing when moving
turtle.pendown()

# Draw a circle with radius of 25
turtle.circle(25)

# Draw a dot with diameter 10
turtle.dot(10)

# Set the turtle heading to 0 (East)
turtle.heading()

# Change the turtle color
turtle.fillcolor('green')


# Draw a filled shape
turtle.fillcolor('blue')

turtle.begin_fill()
turtle.end_fill()
# Clear the drawing
turtle.clearscreen()

# Reset the turtle's state
turtle.reset()

# Hide the turtle
turtle.hideturtle()

# Display the turtle
turtle.showturtle()

# Set the animation speed (0:fastest, 1:slowest, 10:normal)
turtle.speed(5)

# Display text
turtle.write('Hello Malcolm')

# Get input with a dialog box
turtle.numinput("input","Give me a number")

# Respond to user input
turtle.penup()
turtle.goto(50,175)
turtle.pendown()
turtle.write('Hi')

# Filling a shape with color, this may not be functional
turtle.fillcolor('orange')
turtle.begin_fill()
turtle.end_fill()
# Close the window on a click
turtle.exitonclick()

