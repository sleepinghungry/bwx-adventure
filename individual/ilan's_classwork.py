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
