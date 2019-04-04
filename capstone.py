import os
os.system("clear")
import turtle
import random

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Capstone")
wn.setup(height=600, width=600)
wn.tracer(0)


class Head(turtle.Turtle):
	def __init__(self):
		turtle.Turtle.__init__(self)
		self.shape("triangle")
		self.color("white")
		self.speed(0)
		self.penup()
	
	def move(self):
		self.fd(3)
	
	def turn_left(self):
		self.setheading(180)
	
	def turn_right(self):
		self.setheading(0)
	
	def go_down(self):
		self.setheading(270)
	
	def go_up(self):
		self.setheading(90)
	
	def check_outofscreen(self):
		if self.xcor <= -600 or self.xcor >= 600 or self.ycor <= -600 or self.ycor >= 600:
			return True


class Body(turtle.Turtle):
	pass


head = Head()

wn.listen()
wn.onkeypress(head.turn_left, "Left")
wn.onkeypress(head.turn_right, "Right")
wn.onkeypress(head.go_down, "Down")
wn.onkeypress(head.go_up, "Up")

while True:
	wn.update()
	head.move()
	if head.check_outofscreen():
		break



print("MAINLOOP ENDED")
wn.mainloop()