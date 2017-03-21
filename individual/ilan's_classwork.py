import random
import turtle
turtle.colormode(255)

turtle.speed(0)

while True:
    turtle.goto(random.randint(0,200), random.randint(0,200))
    turtle.pencolor(random.randint(0,155), random.randint(0,155), random.randint(0,155))
    turtle.pensize(random.randint(1,50))
    for i in range(random.randint(1,360)):
        turtle.forward(random.randint(1,300))
        turtle.right(random.randint(1,500))
        
