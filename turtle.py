import turtle
def dream():
 for step in range(6):
   turtle.begin_fill()
   for i in range(3):
      turtle.forward(30)
      turtle.left(120)
   turtle.end_fill()
   turtle.forward(50)
   turtle.right(60)
turtle.shape('turtle')
turtle.shapesize(2)
turtle.color('red','yellow')
turtle.speed(6)
dream()
turtle.backward(200)
dream()




