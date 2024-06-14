print("welcome to my general knowledge quiz!")
playing = input("Do you want to play?")
if playing != "yes":
    quit()
print("okay! let's play")

score = 0
answer1 = input("what does cpu stands for?")
if answer1 == "central processing unit":
    print('correct!')
    score1 = score + 1
    print("Your Score:",score1)
else:
    print('incorrect')
    score1 = score - 1
    print("Your Score:",score1)
answer2 = input(" what does gpu stands for?")
if answer2 == "graphing processing unit":
    print('correct!')
    score2 = score + 1
    print("Your Score:",score2)
else:
    print('incorrect')
    score2 = score - 1
    print("Your Score:",score2)
score=score1 + score2
print("score=",score)