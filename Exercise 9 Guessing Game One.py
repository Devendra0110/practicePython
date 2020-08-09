import random
play = True
while play:
    randomNum = random.randint(1,10)
    guessNum = input("Guess a number between 1-10\n->")
    if str(randomNum) == guessNum:
        print("Your guess is right. It is " + guessNum)
    elif guessNum == 'exit':
        print("Game over")
        play=False
    else:
        print("Sorry the number is "+str(randomNum)+".Try again")
