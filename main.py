import turtle               #1. import modules
import random

#Part A
window = turtle.Screen()       # 2.  Create a screen
window.bgcolor('lightblue')

michelangelo = turtle.Turtle()    # 3.  Create two turtles
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up()          # 4.  Pick up the pen so we don’t get lines
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

## 5. your code goes here
#Race 1
leonardo.down()
michelangelo.down()

x = random.randrange(0,101)
michelangelo.forward(x)

y = random.randrange(0,101)
leonardo.forward(y)

michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

michelangelo.clear()
leonardo.clear()
#Race 2 
michelangelo.down()
leonardo.down()

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

m = random.randrange(0,11)
michelangelo.forward(m)

n = random.randrange(0,11)
leonardo.forward(n)

michelangelo.clear()
leonardo.clear()

# Part B - complete part B here
michelangelo.down()

for i in range(3):
  num_sides = 3
  michelangelo.forward(25)
  michelangelo.right(360/num_sides)
michelangelo.clear()

for i in range(4):
  num_sides = 4
  michelangelo.forward(25)
  michelangelo.right(360/num_sides)
michelangelo.clear()

for i in range(6):
  num_sides = 6 
  michelangelo.forward(25)
  michelangelo.right(360/num_sides)
michelangelo.clear()

for i in range(9):
  num_sides = 9 
  michelangelo.forward(25)
  michelangelo.right(360/num_sides)
michelangelo.clear()

for i in range(12):
  num_sides = 12
  michelangelo.forward(25)
  michelangelo.right(360/num_sides)
michelangelo.clear()


window.exitonclick()
