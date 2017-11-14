import getpass

word = getpass.getpass("enter a word:")

wrong_guesses=0

right_guesses=[]

while True:
    
    letter = input("guess a letter ")

    if letter in word:
        
		print("good job")
		
		right_guesses.append(letter)
		
	else:
                print ("wrong!!!")
		
		wrong_guesses=wrong_guesses + 1
		
		print(wrong_guesses)

	print(right_guesses)


	for letter in word:
	
		if letter in right_guesses:
		
			print(letter, end="")
			
		else:
		
			print("_", end="")
			
			print()
