import random
number = random.randint(0,20)
game_over = False
while not game_over:
    guess = int( input("guess a number between 1 and 20"))
    if guess == number:
        game_over = True
        print ("Good job! You got it!")
    elif guess > number:
        print("Too High")
    elif guess < number:
        print("Too Low")
    else:
        print ("LOSER you are wrong. Guess again")
        
