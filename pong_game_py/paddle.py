from turtle import Turtle

class Paddle(Turtle):
  def __init__(self, position):
    super().__init__()

    self.shape("square")
    self.color("white")
    self.shapesize(5, 1)
    self.penup()
    self.goto(position)


  def move(self, direction) :
    step_y = 20 if direction == "Up" else -20
    new_y = self.ycor() + step_y
    self.goto(self.xcor(), new_y)