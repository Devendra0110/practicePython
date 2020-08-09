print("Let's play Rock Paper Scissors")
choices = ["Rock", "Paper", "Scissors"]
play = True
p1Wins = "Player 1 wins"
while(play):
    p1Answer = input("P1 Choose between Rock Paper Scissors")
    
    p2Answer = input("P2 Choose between Rock Paper Scissors")
    
    if p1Answer in choices and p2Answer in choices:
        if p1Answer == "Rock" and p2Answer == "Scissors" : print(p1Wins)
        elif p1Answer == "Scissors" and p2Answer == "Paper" : print(p1Wins)
        elif p1Answer == "Paper" and p2Answer == "Rock" : print(p1Wins)
        elif p1Answer == p2Answer : print("Draws")
        else : print("Player 2 Wins")
        print("Want a rematch, yes or no?")
        answer = input("").lower()
        if answer == "yes" : play = True
        else : play = False
    else:
        if p1Answer in choices: print("P2 available choices are : Rock Paper Scissors")
        else: print("P1 available choices are : Rock Paper Scissors")
