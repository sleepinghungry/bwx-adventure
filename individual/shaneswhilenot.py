game_over = False

while not game_over:
    number = input("Give me a number between 0 and 20:")
    if number != "13":
        print("WRONG!!!!!!!!!")
    if number == "13":
        print("great guess u win nothing.")
        game_over = True
    if number < "13":
        print("To high u suck at video games!")
    if number > "13":
        print("To low u suck at all games!")
