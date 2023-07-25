"""This is a fair endless Rock, paper, scissors game with scores"""

import random

OPTIONS = ["paper", "scissors", "rock"]
OPTIONS_LENGTH = len(OPTIONS)
LOSING_OPTION_COUNT = int((OPTIONS_LENGTH - 1) / 2)
EXIT_GAME = False
RATINGS = {}

# Fill losing conditions for every option
LOSE_CONDITIONS = {}
for user_input, option in enumerate(OPTIONS):
    LOSE_CONDITIONS[option] = []
    for x in range(LOSING_OPTION_COUNT):
        LOSE_CONDITIONS[option].append(
            OPTIONS[(user_input + (x + 1)) % OPTIONS_LENGTH])


PLAYER_NAME = input("Enter your name: ")
print("Welcome ", PLAYER_NAME)

with open("rating.txt", "r", encoding="utf-8") as f:
    content = f.read()
    lines = content.split('\n')
    for line in lines:
        data = line.split()
        RATINGS[data[0]] = int(data[1])

if PLAYER_NAME not in RATINGS:
    RATINGS[PLAYER_NAME] = 0

while EXIT_GAME is False:
    opponent_choice = random.choice(OPTIONS)

    user_input = input(">")

    if user_input in OPTIONS:
        if user_input == opponent_choice:
            print("draw computer picked ", opponent_choice)
            RATINGS[PLAYER_NAME] += 50
        elif opponent_choice in LOSE_CONDITIONS[user_input]:
            print("you lose computer picked ", opponent_choice)
        else:
            print("you win computer picked ", opponent_choice)
            RATINGS[PLAYER_NAME] += 100

    elif user_input == "!rating":
        print("your rating is ", RATINGS[PLAYER_NAME])

    elif user_input == "!exit":
        EXIT_GAME = True
        print("Bye!")
    else:
        print("Invalid Input")
