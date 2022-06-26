############################################################
#     Aidan Weygandt                        05/07/21       #
#     Unit 6 Problems                                      #
#     Turtle Draw Shapes                                   #
############################################################

import turtle
t = turtle
t.setheading(0)

def drawRectangle(color="black", x=0, y=0, width=30, height=30): #moves turtle and draws rectangle
  t.color(color) #allows for rectangle color to be set
  t.goto(x, y)
  t.pendown()
  t.fillcolor(color)
  t.begin_fill()
  for each in range(0, 2): #runs once for each half of the rectangle
    t.forward(width)
    t.right(-90)
    t.forward(height)
    t.right(-90)
  t.end_fill()
  t.penup()

def drawPolygon(color="black", x=0, y=0, sides=4, length=30): #moves turtle and draws any equal sided shape
  t.color(color) #allows for polygon color to be set
  t.goto(x, y)
  t.pendown()
  t.fillcolor(color)
  t.begin_fill()
  for each in range(0, sides): #runs once for each side
    t.forward(length)
    t.right(-360/sides)
  t.end_fill()
  t.penup()

def drawCircle(color="black", x=0, y=0, radius=50): #draws a cirlce at any x and y
  t.color(color) #allows for cicle color to be set too
  t.goto(x, y-radius)
  t.pendown()
  t.fillcolor(color)
  t.begin_fill()
  t.circle(radius)
  t.end_fill()
  t.penup()

#cartesian grid
t.goto(-300, 0)
t.pendown()
t.goto(300, 0)
t.penup()
t.goto(0, 300)
t.pendown()
t.goto(0, -300)
t.penup()

#rotating squares
def fhyp(leg): #finds hypotenuse from leg length of right triangle
  hyp = int((leg**2*2)**0.5)
  return hyp

def fleg(hyp): #finds leg length from hypotenuse of right triangle
  leg = int((hyp**2/2)**0.5)
  return leg

drawRectangle("red", 25, 25, 250, 250) #calls rectangle function VVVV
t.right(-45)
drawRectangle("green", 150, 25, fhyp(125), fhyp(125))
t.right(45)
drawRectangle("yellow", 150-1/2*fleg(fhyp(125)), 25+1/2*fleg(fhyp(125)), fhyp(fhyp(125)/2), fhyp(fhyp(125)/2))
t.right(-45)
drawRectangle("blue", 150-1/2*fleg(fhyp(125)) + fhyp(fhyp(125)/2)/2, 25+1/2*fleg(fhyp(125)), fhyp(fhyp(fhyp(125)/2)/2), fhyp(fhyp(fhyp(125)/2)/2))
t.right(45)
drawRectangle("orange", 150-1/2*fleg(fhyp(125)) + fhyp(fhyp(125)/2)/2 - 1/2*fleg(fhyp(fhyp(fhyp(125)/2)/2)), 25+1/2*fleg(fhyp(125)) + 1/2*fleg(fhyp(fhyp(fhyp(125)/2)/2)), fhyp(fhyp(fhyp(fhyp(125)/2)/2)/2), fhyp(fhyp(fhyp(fhyp(125)/2)/2)/2))

#target
t.goto(150, -150-124)
t.color("black")
t.width(2)
t.pendown()
t.circle(124)
t.penup()
t.width(1)
drawCircle("black", 150, -150, 100) #calls circle function VVV
drawCircle("blue", 150, -150, 75)
drawCircle("red", 150, -150, 50)
drawCircle("yellow", 150, -150, 25)

#hashtag
drawRectangle("red", -25, -200/3-25, -250, -25) #calls rectangle function VVVV
drawRectangle("yellow", -200/3-25, -25, -25, -250)
drawRectangle("green", -25, -250+(200/3), -250, -25)
drawRectangle("blue", -250+(200/3), -25, -25, -250)
drawRectangle("red", -250+(200/3), -200/3-25, -25, -25)

#pentagons
drawPolygon("red", -235, 25, 5, 160) #calls polygon function VVV
drawPolygon("green", -215, 50, 5, 120)
drawPolygon("yellow", -195, 75, 5, 80)
drawPolygon("blue", -175, 100, 5, 40)