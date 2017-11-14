import getpass

wrong_guesses = 0

right_guesses = []

word = getpass.getpass  ("enter a word")


while True:
    letter = input("enter a letter")

    if letter in word:
        print ("great")
        right_guesses . append (letter)
        print ("right_guesses")
        


    else:
        print ("great try but you got it wrong")
        wrong_gusses = wrong_guesses = + 1

    for letter in word:
        if letter in right_guesses,
        print (letter end="")

        else:
            print ("_",end"")


        if rong_gusses = 6
           print ("you lose")

         
         

        

