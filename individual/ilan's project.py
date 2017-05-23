import time

letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

print("""This is a hangman game for two or more players.
Player one is the person who decides the secret word.
Player two is  the person or people who are guessing.
Good luck.""")

time.sleep(1)

word = input("Player 1, please choose any word:")

print("_ " * len(word))

time.sleep(1)

guess1 = 


