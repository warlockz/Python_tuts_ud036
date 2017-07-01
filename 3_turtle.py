import turtle

def drawSquare(t):
	for i  in range(1,5):
		t.forward(100);
		t.right(90)

def drawart():
	window = turtle.Screen()
	window.bgcolor("red")

	t1 = turtle.Turtle()
	t1.color("yellow")
	t1.speed(20)
	t1.shape("turtle")
	for x in range(1,37):
		drawSquare(t1)
		t1.right(10)

#	t2 = turtle.Turtle()
#	t2.color("blue")
#	t2.speed(1)
#	t2.shape("arrow")
#	t2.circle(100)
	
	t3 = turtle.Turtle()
	t3.color("black")
	t3.speed(10)
	t3.left(90)
	t3.forward(100)
	t3.right(45)
	t3.forward(100)
	t3.right(180)
	t3.forward(100)
	t3.right(180)
	t3.left(90)
	t3.forward(100)

	window.exitonclick()
drawart()

