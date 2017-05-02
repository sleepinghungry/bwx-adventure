#dumb = (
 #   ikillu = (input("Welcome to the diving score calculator. Please enter a difficulty:"))
 #     
 #   two = input("What is the first judjes score?")
    
 #   three = input("What is the second judjes score?")
    
 #   four = input("What is the third judjes score?")
    
 #   five = input("What is the fourth judjes score?")
    
 #   six = input("What is the fifth judjes score?")
    
 #   one_through_six = [two, three, four, five, six]
    
 #   one_through_six.remove(max(one_through_six))
    
 #   one_through_six.remove(min(one_through_six))
    
 #   one_through_six123 = one_through_six[0] + one_through_six[1] + one_through_six[2])








































































dif = float (input("Welcome to the diving score calculator. Please enter a difficulty:"))
score1 = float (input("Enter a score:"))
score2 = float (input("Enter a score:"))
score3 = float (input("Enter a score:"))
score4 = float (input("Enter a score:"))
score5 = float (input("Enter a score:"))
scores = [score1, score2, score3, score4, score5]
scores.remove(max(scores))
scores.remove(min(scores))
total = scores[0] + scores[1] + scores[2]
print (total*dif)
