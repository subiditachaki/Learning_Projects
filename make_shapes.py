import turtle

def open_window():
	window = turtle.Screen()
	window.bgcolor("pink")
	draw_circle()
	draw_square()
	draw_triangle()
	window.exitonclick()

def draw_square():
	brad = turtle.Turtle()
	brad.shape("turtle")
	brad.color("blue")
	brad.speed(2)
	side = 1

	while side <= 4:
		brad.forward(100)
		brad.right(90)
		side += 1

def draw_circle():
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("purple")
	brad.circle(100)

def draw_triangle():
	brad = turtle.Turtle()
	brad.shape("arrow")
	brad.color("green")
	brad.speed(2)
	side = 1

	while side <= 3:
		brad.backward(100)
		brad.left(120)
		side += 1

open_window()