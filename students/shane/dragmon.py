import turtle

def createWord(max_it, axiom, proc_rules):

    word = axiom
    t = 1

    while (t < max_it):
        word = rewrite(word, proc_rules)
        t=t+1

    newWord = word

def rewrite(word, proc_rules):

    wordList = list(word)

    for i in range(len(wordList)):
        curChar = wordList[i]
        if curChar in proc_rules:
            wordList[i] = proc_rules[curChar]

    return "".join(wordList)

def drawit(newWord, d, angle):

    newWordLs = list(newWord)
    for i in range(len(newWordLs)):
        cur_Char = newWordLs[i]
        if cur_Char == 'F':
            turtle.forward(d)
        elif cur_Char == '+':
            turtle.right(angle)
        elif cur_Char == '-':
            turtle.left(angle)
        else:
            i = i+1

#sample test of dragon curve

def main():
    createWord(10, 'FX', {'X':'X+YF','Y':'FX-Y'})
    drawit('FX+YF+FX-YF+FX+YF-FX-YF+FX+YF+FX-YF-FX+YF-FX-YF', 20, 90)

if __name__=='__main__': main()
