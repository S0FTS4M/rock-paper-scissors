"""This is a fair Rock, paper, scissors game with multiple options specified by players"""

import random

#rock,gun,lightning,devil,dragon,water,air,paper,sponge,wolf,tree,human,snake,scissors, fire
RATINGS = {}

EXIT_GAME = False

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

OPTIONS_INPUT = input(">")

OPTIONS = OPTIONS_INPUT.split(',')

#user did not specify any options
if len(OPTIONS_INPUT) == 0:
    OPTIONS = ["paper", "scissors", "rock"]


print("Ok, lets start")

OPTIONS_LENGTH = len(OPTIONS)
LOSING_OPTION_COUNT = int((OPTIONS_LENGTH - 1) / 2)

#Fill losing conditions for every option
LOSE_CONDITIONS = {}
for i, option in enumerate(OPTIONS):
    LOSE_CONDITIONS[option] = []
    for x in range(LOSING_OPTION_COUNT):
        LOSE_CONDITIONS[option].append(OPTIONS[(i + (x + 1)) % OPTIONS_LENGTH])

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
