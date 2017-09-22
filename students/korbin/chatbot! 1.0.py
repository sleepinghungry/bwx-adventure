import random
import time
import sys

yes = ['ya','yep','yes','sure']
no = ['no','nope','no thanks']
bye = ['bye','Bye','bye!','Bye!']
bad_name = ['idiot','asshole','ass','dumb','dumbby','turd','buttface']

print("bot- hello!")

trash = input(" you- ")

time.sleep(.3)
    
if trash in bye:
    print("okay, bye-bye")
else:
    print("bot- nice to meet you, i do not have a name yet! could you name me?")

    time.sleep(1.3)

    print()

    print("bot- please enter my name! ")

    bot = input(" you- ")
    if bot in bad_name:
        print("u suck, im leaving")
        sys.exit()
    elif bot in bye:
        print("okay, bye-bye")
    else:
        print(bot + "- Aw thanks! I LOVE " + bot + " as a name!!!")

        print()

        print(bot + "- now whats your name?") 

        name = input(" you- ")

        if name in bye:
            print("okay, bye-bye")
        else:
            print (bot + "-" , name , "is a really cool name, thank you")

            game0 = input(bot + "-" + name + ", wana play a game?")

            if game0 in yes:
                print("okay!")

                time.sleep(.3)
                
                print("what game do you wana play?")

                time.sleep(.3)
                
                print("1. madlib")

                print()

                print("OR")

                print()
                
                print("2. guess a number")

                gamechoice0 = input("1 or 2? ")

                if gamechoice0 == 1:
                    print("okay cool, mad lib it is then")
                    
                elif gamechoice0 == 2:

                    print("okay cool, lets guess some numbers!")

                    time.sleep(.3)

                    print

            elif bot in bye:
                print("okay, bye-bye")


            else:
                print ()
                
            
            
            

            


