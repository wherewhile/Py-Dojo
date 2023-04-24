from turtle import *

canvas = turtle.Screen()
canvas.bgcolor("black")
pen = turtle.Turtle()
pen.speed(0)
pen.penup()
pen.hideturtle()

def fireworks(x, y, pen):
    pen.color("white") 
    pen.goto(x, y) 
    pen.pendown()   
    for i in range(25):
         pen.forward(i) 
         pen.right(random.randint(0, 360)) 
         pen.penup()
         x = random.randint(-300, 300)  y = random.randint(-300, 300) fireworks(x, y, pen)
        
       