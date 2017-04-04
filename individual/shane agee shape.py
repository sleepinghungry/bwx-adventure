import turtle

turtle.shape("turtle")

#turtle.colormode(255)

#turtle.pencolor(255,1,1)

#turtle.pensize(5)

def draw_swastica():
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)

        turtle.up()
        turtle.goto(0,0)
        turtle.down()
        turtle.forward(100)
        turtle.right(90)
        turtle.forward(100)
def draw_NO():
        turtle.up()
        turtle.goto(-300,-250)
        turtle.down()
        turtle.left(90)
        turtle.forward(75)

        turtle.right(135)
        turtle.forward(110)
        turtle.left(135)
        turtle.forward(75)

        turtle.up()
        turtle.right(90)
        turtle.forward(20)
        turtle.down()
        turtle.forward(65)
        turtle.right(90)
        turtle.forward(75)
        turtle.right(90)
        turtle.forward(65)
        turtle.right(90)
        turtle.forward(75)

        turtle.right(90)
        turtle.up()
        turtle.forward(85)
        turtle.down()

        turtle.right(90)
        turtle.forward(65)
        turtle.up()
        turtle.forward(10)
        turtle.down()
        turtle.forward(20)

        turtle.up()
        turtle.backward(95)
        turtle.right(90)
        turtle.up()
        turtle.forward(20)
        turtle.down()
        turtle.left(90)

answer = "Y"

while answer == "Y":
    draw_swastica()
    draw_NO()
    answer = input("Do u want 2 play again.")
