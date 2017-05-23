import time

print("""This is a hangman game for two or more players.
Player one is the person who decides the secret word.
Player two is  the person or people who are guessing.
Good luck.""")

time.sleep(1)

word = input("Player 1, please choose any word:")

length = len(word)

print("_ " * length)

time.sleep(1)

yes = 0

no = 0

guess1 = input("Player 2, guess a letter:")

if guess1 == word[length - 1]:
    print ("Correct")
    yes += 1
    print ("_ " * (length - 1), guess1)
elif

    


