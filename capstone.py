import os
os.system("clear")
import turtle
import random
import time
import tkinter
import pickle
click = 0

def normal_mode():
	global game_status
	game_status = "normal"
	base_mode()

def adventure_mode():
	global game_status
	game_status = "adventure"
	base_mode()

def rpg_mode():
	global click
	global game_status
	game_stauts = "rpg"
	lines = ["I'm still working on this", "I told u it is not finish yet", "there is nothing!", "there is nothing!!", "ok I'm leaving BYE", "", "", "....", "Why u r still here?", " CAN U PLEASE STOP?", "There is nothing"]
	while click < len(lines):
		lbl_space["text"] = lines[click]
		click += 1
		break
	
	
		

def base_mode():
	wn = turtle.Screen()
	wn.bgcolor("black")
	wn.title("Capstone")
	wn.setup(height=600, width=600)
	wn.tracer(0)
	normal_ranks = {}
	adventure_ranks = {}
	def add_ranking():
		global name
		global ranks
		#ranks = pickle.load(open("ranks.dat", "rb"))
		name = text_input_r.get()
		if game_status == "normal":
			normal_ranks[head.scores] = name
			text_input_r.delete(0, "end")
			lb_ranks.delete(0,"end")
			scorelist = list(ranks.keys())
			scorelist.sort()
			scorelist.reverse()
			for score in scorelist:
				rank = normal_ranks[score] + " SCORE: " + str(score)
				lb_ranks_normal.insert("end", rank)
		elif game_status == "adventure":
			adventure_ranks[head.scores] = name
			text_input_r.delete(0, "end")
			lb_ranks.delete(0,"end")
			scorelist = list(ranks.keys())
			scorelist.sort()
			scorelist.reverse()
			for score in scorelist:
				rank = adventure_ranks[score] + " SCORE: " + str(score)
				lb_ranks_adventure.insert("end", rank)
		#pickle.dump(ranks, open("ranks.dat", "wb"))
		

	class Head(turtle.Turtle):
		def __init__(self):
			turtle.Turtle.__init__(self)
			self.shape("triangle")
			self.color("white")
			self.speed(0)
			self.penup()
			self.lives = 3
			self.scores = 0
			self.switch = 0
	
		def move(self):
			self.fd(20)
# check this later
# have to fix the object
			for food in foods:
				if self.distance(food) < 20:
					pen.clear()
					food.jump()
					body = Body()
					self.scores += 1
					bodies.append(body)
			for object in objects:
				if self.distance(object) < 20:
					pen.clear()
					object.jump()
					if game_status == "normal":
						self.scores += 1
						body = Body()
						bodies.append(body)
					elif game_status == "adventure":
						if isinstance(object, Bad_things):
							self.lives -= 1
						else:
							self.scores += 1
							body = Body()
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
			self.color("black")
			self.penup()
			self.speed(0)
	
		def move(self):
			self.goto(head.xcor(),head.ycor())
			self.color("white")
	


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
	
	class Bad_things(Food):
		def __init__(self):
			Food.__init__(self)
			self.color("green")

	pen = turtle.Turtle()
	pen.penup()
	pen.color("white")
	pen.hideturtle()

	head = Head()
	bodies = []
	foods = []
	objects = []
	bad_things = []
	for i in range(2):
		food = Food()
		food.jump()
		foods.append(food)
	objects.extend(foods)

	if game_status == "adventure":
		for i in range(10):
			bad_thing = Bad_things()
			bad_thing.jump()
			bad_things.append(bad_thing)
		objects.extend(bad_things)

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
				bodies[i].color("white")
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
		if game_status == "adventure":
			if head.switch % 47 == 0:
				pen.goto(0, 250)
				pen.write("SWIRTCH!!!", move = False, align = "right", font = ("Aronal", 20, "normal"))
		
			if head.switch % 53 == 0:

				for bad_thing in bad_things:
					bad_thing.jump()
			head.switch = head.switch+1
		
		for body in bodies:
			if head.check_collision(body):
				head.lives -= 1
				pen.clear()

		if head.check_outofscreen():
			head.lives -= 1
			head.goto(0,0)
			pen.clear()

		if head.lives == 0:
			pen.goto(0,20)
			pen.write("GAME END", move=False, align="center", font=("Arial", 20, "normal"))	
			pen.goto(0,0)
			pen.write("Thanks for playing", move=False, align="center", font=("Arial", 15, "normal"))		
			pen.goto(0,-20)
			pen.write("Your final score: {}".format(head.scores), move=False, align="center", font=("Arial", 20, "normal"))		

			ranking = tkinter.Tk()
			ranking.title("Ranking")
			lbl_title_r = tkinter.Label(ranking, text = "Ranking list!")
			lbl_title_r.grid(row = 0, column = 0)
			lbl_display_r = tkinter.Label(ranking, text = " ")
			lbl_display_r.grid(row = 0, column = 1)

			lbl_name_r = tkinter.Label(ranking, text = "Please write your name: ")
			lbl_name_r.grid(row = 1, column = 0)
			text_input_r = tkinter.Entry(ranking, width = 16)
			text_input_r.grid(row = 1, column = 1)

			btn_ok_r = tkinter.Button(ranking, text = "OK!", command = add_ranking)
			btn_ok_r.grid(row = 2, column = 0)

			lbl_name_normal = tkinter.Label(ranking, text = "Normal Mode")
			lbl_name_normal.grid(row = 0, column = 2)

			lbl_name_adventure = tkinter.Label(ranking, text = "Adventure Mode")
			lbl_name_adventure.grid(row = 0, column = 3)

			lb_ranks_normal = tkinter.Listbox(ranking)
			lb_ranks_normal.grid(row = 1, column = 2, rowspan = 7)

			lb_ranks_adventure = tkinter.Listbox(ranking)
			lb_ranks_adventure.grid(row = 1, column = 3, rowspan = 7)

			ranking.mainloop()
			break

	wn.mainloop()


# menu 
menu = tkinter.Tk()
menu.title("Menu")
lbl_titile = tkinter.Label(menu, text = "Ann's snake game")
lbl_titile.grid(row =0, column = 0)

lbl_space = tkinter.Label(menu, text = "")
lbl_space.grid(row = 1, column = 0)

btn_normal_mode = tkinter.Button(menu, text = "normal mode", command = normal_mode)
btn_normal_mode.grid(row = 2, column = 0)

btn_adventure_mode = tkinter.Button(menu, text = "adventure mode", command = adventure_mode)
btn_adventure_mode.grid(row = 3, column = 0)

btn_rpg_mode = tkinter.Button(menu, text = "RPG mode", command = rpg_mode)
btn_rpg_mode.grid(row = 4, column = 0)

btn_exit = tkinter.Button(menu, text = "exit", command = exit)
btn_exit.grid(row = 5, column = 0)
menu.mainloop()