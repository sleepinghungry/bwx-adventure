#quiz
score = 0
q_1 = input("What is the capitol of Argentina?")
q_2 = input("What is the capitol of Macedonia")
q_3 = input("What is the capitol of Indosisia")
a_1 = "Buenos Aires"
a_2 = "Skopje"
a_3 = "Jakarta"

if q_1 == a_1:
    print ("Question 1 - Correct")
    score += 1
else:
    print ("Question 1 - Wrong")



if q_2 == a_2:
    print ("Question 2 - Correct")
    score += 1
else:
    print ("Question 2 - Wrong")




if q_3 == a_3:
    print ("Question 3 - Correct")
    score += 1
else:
    print ("Question 3 - Wrong")
print("Your score is", score)
