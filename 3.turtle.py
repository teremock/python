import turtle  # Allows us to use turtles
import random
wn = turtle.Screen()  # Creates a playground for turtles
alex = turtle.Turtle()  # Create a turtle, assign to alex
while True:
 for povtorchik in range(1,5):
  alex.width(random.randint(3, 17))
  for povtor in range(1,50):
     alex.pencolor(random.random(), random.random(), random.random())
     alex.forward(8)
     alex.left(7)
     alex.forward(8)
  alex.clear()

wn.mainloop()