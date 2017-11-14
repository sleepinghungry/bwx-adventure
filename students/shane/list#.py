print("Pick a # between 1 and 10? Don't enter that #, just save it in your head")

fudge = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

thenumber0 = input("Is the # your thinking about an odd #?")
thenumber1 = input("is your # a prime #?")

if thenumber0 == "yes":
    fudge.remove("2")
    fudge.remove("4")
    fudge.remove("6")
    fudge.remove("8")
    fudge.remove("10")
    if thenumber1 == "no":
        fudge.remove("1")
        fudge.remove("3")
        fudge.remove("7")

if thenumber0 == "no":
    fudge.remove("1")
    fudge.remove("3")
    fudge.remove("5")
    fudge.remove("7")
    fudge.remove("9")
    if thenumber1 == "no":
        fudge.remove("4")
        fudge.remove("6")
        fudge.remove("8")
        fudge.remove("10")

print(fudge)
