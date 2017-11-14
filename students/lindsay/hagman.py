import getpass

ward = getpass.getpass("enter word")

right_guesses = []

wrong = 0


while True:


    letter = input ("guess letter    ")

    if letter in ward:
        print("yay you got it right")
        right_guesses.append(letter)
        print(right_guesses)
    else:
        print("nope ")
        wrong += 1
        print(wrong)

    for letter in ward:
        if letter in right_guesses:
            print(letter, end="")
       else:
           print(" _ ", end ="")



    if wrong == 6:
        break
        print ("you lose")

    if right_guesses == ward:
        print("you win")
