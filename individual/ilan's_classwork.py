import random
import turtle
turtle.colormode(255)
turtle.speed(0)


def draw_shape():
    turtle.goto(random.randint(-200,200), random.randint(-200,200))
    random_number = random.randint(0,500)
    turtle.pencolor(random.randint(0,255), random.randint(0,255), random.randint(0,255))
    turtle.pensize(random.randint(1,30))
    def square():
        for i in range(4):
            turtle.forward(random_number)
            turtle.right(90)

    def triangle():
        for i in range(3):
            turtle.forward(random_number)
            turtle.left(120)
    def hexegon():
        for i in range(6):
            turtle.forward(random_number)
            turtle.right(120) 
    def octogon():
        for i in range(8):
            turtle.forward(random_number)
            turtle.right(315)

while True:
    draw_shape
