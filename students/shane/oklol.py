from turtle import Turtle

t=Turtle()
t.screen.bgcolor("grey")
t.color("purple")

t.write("Shane is Super Cool!!!", move=True, align='center',
       font=('Autor One', 34, 'normal'))
yes = input("You: ")

if yes == "yes":
    input("Woo-Hoo")
