import turtle  # Allows us to use turtles
import random
wn = turtle.Screen()  # Creates a playground for turtles
alex = turtle.Turtle()  # Create a turtle, assign to alex
for povtorchik in range(1,5):
 alex.width(random.randint(3, 17))
 for povtor in range(1,5):
     alex.pencolor(random.random(), random.random(), random.random())
     alex.forward(50)  # Tell alex to move forward by 50 units
     alex.left(90)  # Tell alex to turn by 90 degrees
     alex.forward(40)  # Complete the second side of a rectangle
 alex.clear()

wn.mainloop()  # Wait for user to close window