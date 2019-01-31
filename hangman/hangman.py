score = 0
def opencat(category):
    line = open(category+".txt")
    for i in line:
        n = i.strip().split(",")
        word = n[0].lower()
        hint = n[1]
        play(word,hint)
        print()

def play(word,hint):
    global score
    wrong = 10;
    wordLen = len(word)
    blindWord = ""
    wrongGuess = ""
    print ("Hint: "+ hint)
    for i in range (wordLen):
        blindWord = blindWord + "_"
    for i in blindWord:
        print(i,end = " ")
    print("score " + str(score)+", " + "remaining wrong guess " + str(wrong)
                  +", "+ "wrong guessed: " + wrongGuess)
    while True:
        if (wrong<=0):
            print("Game Over")
            exit(0)
        if (blindWord.find("_") == -1):
            break
        a = input("Enter your character : ").lower()
        if (a==""):
            print("Please enter character !")
            continue
        if (len(a)>1):
            print("Please enter just 1 character !")
            continue
        if (word.find(a) != -1):
            x = 0
            while(word.find(a,x) >= 0):
                x = word.find(a,x)
                if (blindWord[x] == "_"):
                    blindWord = blindWord[0:x]+blindWord[x:].replace("_",a,1)
                    score += 10
                x=x+1
            for i in blindWord:
                print(i,end = " ")
            print("score " + str(score)+", " + "remaining wrong guess " + str(wrong)
                  +", "+ "wrong guessed: " + wrongGuess)
        else:
            wrongGuess = wrongGuess + a + " "
            wrong = wrong-1
            print("score " + str(score)+", " + "remaining wrong guess " + str(wrong)
                  +", "+ "wrong guessed: " + wrongGuess)

print("Select Category Number : ")                
categories = ["Game Name","Vehicle"]
for i in range (0,len(categories)):
    print(str(i+1)+"."+categories[i])
x = int(input(">"))
opencat(categories[x-1])
