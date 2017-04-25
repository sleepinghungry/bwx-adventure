import random

lol = ("This is a programmed magic 8 ball.")

print(lol)
while True:
    input("What is your yes or no question?")

    mylisd = ["yes","no","maybe","sure...","defiatly","prob not","nope","for sure"]

    print(random.choice(mylisd))
