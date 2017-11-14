import getpass
#getting word and keeping score

ward = getpass.getpass("enter word")

right_guesses = []

wrong = 0

#repting

while True:

#guessing letters
 
    letter = input ("guess letter    ")

#check if letter is right or rong 	
    if letter in ward:
        print("yay you got it right")
		# addto right guesses
        right_guesses.append(letter)
        print(right_guesses)
    else:
        print("nope ")
        wrong += 1
        print(wrong)

		
#for each letter in our word 
		
        for letter in ward:
	#correct guess
            if letter in right_guesses:
                print(letter, end="")
	if wrong > 0:
            print(" O ")
        if wrong > 1:
            print("/", end="")
        if wrong > 2:
            print("\\")
        if wrong > 3:
            print("|")
        if wrong > 4:
            print("/", end="")
        if wrong > 5:
            print("\\")          
            else:
               print(" _ ", end ="")

    
#winnig or loosing
    if wrong == 7:
        break
        print ("you lose")

    if right_guesses == ward:
        print("you win")
