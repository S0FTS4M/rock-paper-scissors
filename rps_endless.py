"""This is a fair endless Rock, paper, scissors game"""

import random

OPTIONS = ["paper", "scissors", "rock"]
OPTIONS_LENGTH = len(OPTIONS)
LOSING_OPTION_COUNT = int((OPTIONS_LENGTH - 1) / 2)

#Fill losing conditions for every option
LOSE_CONDITIONS = {}
for i, option in enumerate(OPTIONS):
    LOSE_CONDITIONS[option] = []
    for x in range(LOSING_OPTION_COUNT):
        LOSE_CONDITIONS[option].append(OPTIONS[(i + (x + 1)) % OPTIONS_LENGTH])

print(LOSE_CONDITIONS)
EXITGAME = False

while EXITGAME is False:
    opponent_choice = random.choice(OPTIONS)

    user_input = input(">")

    if user_input in OPTIONS:
        if user_input == opponent_choice:
            print("draw computer picked ", opponent_choice)
        elif opponent_choice in LOSE_CONDITIONS[user_input]:
            print("you lose computer picked ", opponent_choice)
        else:
            print("you win computer picked ", opponent_choice)
    elif user_input == "!exit":
        EXITGAME = True
        print("Bye!")
    else:
        print("Invalid Input")
