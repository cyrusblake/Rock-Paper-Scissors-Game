def start():
    loose = "The computer wins"
    win = "You win"
    lives = 5
    score = 0
    drew = 0
    computer_lives = 7
    start_menu = """
    Live Rules You start with 5 lives 
    If you loose you loose a life
    If you draw the lives stay the same
    --------------------------------------
    To see a list of rules type rules
    --------------------------------------
    At any point type exit to leave the game
    --------------------------------------
    The computer has lives as well
    Can you beat the computer?
    Good Luck!!
    --------------------------------------
    """
    print(start_menu)
    while True:
        rps = input("Rock, Paper, Scissors? ")
        rps = rps.title()
        import random

        computer = ("rock", "paper", "scissors")
        computer = random.choice(computer)
        # rock if statements
        if rps == "Rock" and computer == "paper":
            print("The computer choose", computer)
            print("")
            print(loose)
            print("")
            print("")
            lives -= 1
        if rps == "Rock" and computer == "scissors":
            print("The computer choose", computer)
            print("")
            print(win)
            print("")
            print("")
            score += 1
            # paper if statements
        if rps == "Paper" and computer == "rock":
            print("The computer choose", computer)
            print("")
            print(win)
            computer_lives -= 1
            print("")
            print("")
            score += 1
        if rps == "Paper" and computer == "scissors":
            print("The computer choose", computer)
            print("")
            print(loose)
            print("")
            print("")
            lives -= 1
            # scissors if statements
        if rps == "Scissors" and computer == "paper":
            print("The computer choose", computer)
            print("")
            print(win)
            computer_lives -= 1
            print("")
            print("")
            score += 1
        if rps == "Scissors" and computer == "rock":
            print("The computer choose", computer)
            print("")
            print(loose)
            print("")
            print("")
            lives -= 1
            # duplicates
        if rps == "Rock" and computer == "rock":
            print("The computer choose", computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
        if rps == "Paper" and computer == "paper":
            print("The computer choose", computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
        if rps == "Scissors" and computer == "scissors":
            print("The computer choose", computer)
            print("")
            print("You Drew")
            print("")
            print("")
            drew += 1
            # system
        if rps == "Rules":
            print("###############################")
            print("Rules")
            print("###############################")
            print("-Rock loses against Paper")
            print("-Rock beats Scissors")
            print("-Paper beats Rock")
            print("-Paper loses against Scissors")
            print("-Scissors beats Paper")
            print("-Scissors loses against Rock")
        if rps == "Display lives":
            print(lives)
        if rps == "Display score":
            print(score)
        if rps == "Display drew":
            print(drew)
            # lives
        if lives == 0 or rps == "Test":
            print("Thanks for playing.")
            print("You have run out of lives")
            print("You got", score, "correct")
            print("You drew", drew, "times")
            stop = input("Press enter to exit.")
            exit()
        if computer_lives == 0:
            print("Thanks for playing.")
            print("The computer lost all it's lives. Uou Win")
            print("You got", score, "correct")
            print("You drew", drew, "times")
            exit()

            # exit
        if rps == "Exit":
            exit()