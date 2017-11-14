import getpass
# step 1: get a word from the first user
#(we're using getpass so the word doesn't appear)
word=getpass.getpass("Enter a word. ")
# if wrong guesses reaches six, we end the game
wrong_guesses = 0
# list of correct guesses from the second user
right_guesses = []
# this makes the indented code below repeat forever
while True:
    # tells user to guess a letter
    letter = input(" Guess a letter.")

    # checking if the user's letter is part of the word
    if letter in word:
        print("Correct!")
        # adding the correct guess to the list
        right_guesses.append(letter)
        print(right_guesses)
        # but, in the case that the letter is not part of the word:
    else:
        print("Incorrect.")
        # increases (increments) wrong_guesses by 1.
        wrong_guesses =  wrong_guesses + 1

    if wrong_guesses == 6:
        print("Sorry, you lose!")
        break
    # for each letter in our word:
    for letter in word:
        # if the letter in the word was guesses correctly:
        if letter in right_guesses:
            print(letter, end="")
            #if the letter in the word was not guessed yet
        else:
            print (" _ ", end="")
    print()
    if wrong_guesses > 0:
        print(" 0 ")
    
