import getpass

# step 1: get a word from first user
#(we're using getpass sothe word doesn't appear)
word = getpass.getpass("user 1, enter a word")

# if wrong guesses reaches six, we end the game
wrong_guesses = 0

# list of correct guesses from the second user
right_guesses = []

# this makes the indented code below repeat forever
while True:
    # tells user two to guess a letter
    letter = input ("User 2, guess a letter:")

    #checking if user two's letter is in the word 
    if letter in word:
        print ("correct!")
        # adding the correct guess to the list
        right_guesses.append(letter)
        print(right_guesses)
    # but, if the letter is NOT in the word:
    else:
        print ("wrong!")
        # increases wrong guesses by one
        wrong_guesses = wrong_guesses + 1
    if wrong_guesses == 6:
        print ("you lose!")
        break
    # for each letter in the word
    for letter in word:
        # if the letter in the word was guessed correctly:
        if letter in right_guesses:
            print (letter, end="")
        # if the letter was NOT guessed yet:    
        else:
            print (" _ ", end="")
    print()

    if wrong_guesses > 0:
        print ("0")
    if wrong_guesses > 1:
        print ("/",end="")
    if wrong_guesses > 2:
        print ("\\")
    if wrong_guesses > 3:
        print (" | ")
    if wrong_guesses > 4:
        print ("/",end="")
    if wrong_guesses > 5:
        print ("\\")
        print ("you lose!")
        break  
        
