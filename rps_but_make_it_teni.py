from random import randint

play = ["Rock", "Paper", "Scissors"]

computer = play[randint(0,2)]

player = False

while player == False:
    player= input("Rock.\nPaper.\nScissors Bitch?\n")
    if player == computer:
        print("Tie motherfucker! Play that shit again!")
    elif player == "Rock":
        if computer == "Paper":
            print("Gtfoh here with that terrible play. Fucking clown!", computer,"covers", player,"!")
        else:
            print("You lucky son of a bitch.",player,"crushes",computer,"sadly.")
    elif player == "Paper":
        if computer == "Rock":
            print("Don't smile, it's not that deep, and yes",player,"covers",computer,".")
        else:
            print("Ha! Got you bitch!",computer,"cuts",player,"ass.")
    elif player == "Scissors":
        if computer == "Papers":
            print("Okay you get this one but only because", player,"slices tf outta",computer,".")
        else:
            print("What? Thought you were going to win this one? Honey",computer,"has",player,"pummelled to dust.")
    else:
        print("Use your brain will you? Type in something sensible fool!")
    player = False
    computer = play[randint(0,2)]
    exit()
