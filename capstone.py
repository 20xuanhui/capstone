import os
os.system("clear")
import turtle
import random
import time

# menu 
menu = turtle.Screen()
menu.title("Menu")
menu.tracer(0)


x = input("normal mode? y/n")
if x == "y":
	normal_mode = True



if normal_mode:
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
			self.lives = 3
			self.scores = 0
	
		def move(self):
			self.fd(20)
			for food in foods:
				if self.distance(food) < 20:
					pen.clear()
					food.jump()
					body = Body()
					self.scores += 1
					bodies.append(body)
				
		def check_collision(self, body):
			if self.distance(body) < 5:
				return True
			else:
				return False

	
		def turn_left(self):
			if self.heading() != 0:
				self.setheading(180)
	
		def turn_right(self):
			if self.heading() != 180:
				self.setheading(0)
	
		def go_down(self):
			if self.heading() != 90:
				self.setheading(270)
	
		def go_up(self):
			if self.heading() != 270:
				self.setheading(90)
	
		def check_outofscreen(self):
			if self.xcor() <= -300 or self.xcor() >= 300 or self.ycor() <= -300 or self.ycor() >= 300:
				return True
	

	class Body(turtle.Turtle):
		def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("square")
			self.color("white")
			self.penup()
			self.speed(0)
	
		def move(self):
			self.goto(head.xcor(),head.ycor())
	


	class Food(turtle.Turtle):
		def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("circle")
			self.color("red")
			self.penup()
			self.speed(0)
	
		def jump(self):
			x = random.randint(-250,250)
			y = random.randint(-250,250)
			self.goto(x,y)

	pen = turtle.Turtle()
	pen.penup()
	pen.color("white")
	pen.hideturtle()

	head = Head()
	bodies = []
	foods = []
	for i in range(2):
		food = Food()
		food.jump()
		foods.append(food)

	time_number = 0
		
	wn.listen()
	wn.onkeypress(head.turn_left, "Left")
	wn.onkeypress(head.turn_right, "Right")
	wn.onkeypress(head.go_down, "Down")
	wn.onkeypress(head.go_up, "Up")


	while True:
		wn.update()
		if len(bodies) > 1:
			for i in range(len(bodies) -1, -1, -1):
				bodies[i].goto(bodies[i-1].xcor(), bodies[i-1].ycor())
		if len(bodies) > 0:
			bodies[0].move()
		time.sleep(0.1)
		head.move()
		pen.goto(250, 250)
		pen.write("lifes: {}".format(head.lives), move=False, align="right", font=("Arial", 20, "normal"))
		pen.goto(250,220)
		pen.write("scores: {}".format(head.scores), move=False, align="right", font=("Arial", 20, "normal"))
	
		if time_number < 10:
			pen.goto(0,20)
			pen.write("Use your ↑↓←→ to control the snake!".format(head.scores), move=False, align="center", font=("Arial", 20, "normal"))
		
			pen.goto(foods[0].xcor()+15,foods[0].ycor()+10)
			pen.write("EAT THIS↓↓", move = False, align = "right", font = ("Aroal", 20, "normal"))
			time_number += 1
		
		for body in bodies:
			if head.check_collision(body):
				head.lives -= 1
				pen.clear()

		if head.check_outofscreen():
			head.lives -= 1
			head.goto(0,0)
			pen.clear()

		if head.lives == 0:
			break

	pen.goto(0,20)
	pen.write("GAME END", move=False, align="center", font=("Arial", 20, "normal"))	
	pen.goto(0,0)
	pen.write("Thanks for playing", move=False, align="center", font=("Arial", 15, "normal"))		
	pen.goto(0,-20)
	pen.write("Your final score: {}".format(head.scores), move=False, align="center", font=("Arial", 20, "normal"))		
	print("MAINLOOP ENDED")
	wn.mainloop()

if adverture_mode:
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
			self.lives = 3
			self.scores = 0
	
		def move(self):
			self.fd(20)
			for food in foods:
				if self.distance(food) < 20:
					pen.clear()
					food.jump()
					body = Body()
					self.scores += 1
					bodies.append(body)
				
		def check_collision(self, body):
			if self.distance(body) < 5:
				return True
			else:
				return False

	
		def turn_left(self):
			if self.heading() != 0:
				self.setheading(180)
	
		def turn_right(self):
			if self.heading() != 180:
				self.setheading(0)
	
		def go_down(self):
			if self.heading() != 90:
				self.setheading(270)
	
		def go_up(self):
			if self.heading() != 270:
				self.setheading(90)
	
		def check_outofscreen(self):
			if self.xcor() <= -300 or self.xcor() >= 300 or self.ycor() <= -300 or self.ycor() >= 300:
				return True
	

	class Body(turtle.Turtle):
		def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("square")
			self.color("white")
			self.penup()
			self.speed(0)
	
		def move(self):
			self.goto(head.xcor(),head.ycor())
	


	class Food(turtle.Turtle):
		def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("circle")
			self.color("red")
			self.penup()
			self.speed(0)
	
		def jump(self):
			x = random.randint(-250,250)
			y = random.randint(-250,250)
			self.goto(x,y)

	pen = turtle.Turtle()
	pen.penup()
	pen.color("white")
	pen.hideturtle()

	head = Head()
	bodies = []
	foods = []
	objects = [foods, bad_things]
	bad_things = []
	for i in range(2):
		food = Food()
		food.jump()
		foods.append(food)
	
	for i in range(5):
		bad_thing = Food()
		bad_thing.jump()
		bad_things.append(bad_thing)

	time_number = 0
		
	wn.listen()
	wn.onkeypress(head.turn_left, "Left")
	wn.onkeypress(head.turn_right, "Right")
	wn.onkeypress(head.go_down, "Down")
	wn.onkeypress(head.go_up, "Up")


	while True:
		wn.update()
		if len(bodies) > 1:
			for i in range(len(bodies) -1, -1, -1):
				bodies[i].goto(bodies[i-1].xcor(), bodies[i-1].ycor())
		if len(bodies) > 0:
			bodies[0].move()
		time.sleep(0.1)
		head.move()
		pen.goto(250, 250)
		pen.write("lifes: {}".format(head.lives), move=False, align="right", font=("Arial", 20, "normal"))
		pen.goto(250,220)
		pen.write("scores: {}".format(head.scores), move=False, align="right", font=("Arial", 20, "normal"))
	
		if time_number < 10:
			pen.goto(0,20)
			pen.write("Use your ↑↓←→ to control the snake!".format(head.scores), move=False, align="center", font=("Arial", 20, "normal"))
		
			pen.goto(foods[0].xcor()+15,foods[0].ycor()+10)
			pen.write("EAT THIS↓↓", move = False, align = "right", font = ("Aroal", 20, "normal"))
			time_number += 1
		
		for body in bodies:
			if head.check_collision(body):
				head.lives -= 1
				pen.clear()

		if head.check_outofscreen():
			head.lives -= 1
			head.goto(0,0)
			pen.clear()

		if head.lives == 0:
			break

	pen.goto(0,20)
	pen.write("GAME END", move=False, align="center", font=("Arial", 20, "normal"))	
	pen.goto(0,0)
	pen.write("Thanks for playing", move=False, align="center", font=("Arial", 15, "normal"))		
	pen.goto(0,-20)
	pen.write("Your final score: {}".format(head.scores), move=False, align="center", font=("Arial", 20, "normal"))		
	print("MAINLOOP ENDED")
	wn.mainloop()




menu.mainloop()