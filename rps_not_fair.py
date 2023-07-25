"""This is an unfair Rock, paper, scissors game"""

LOSE_CONDITIONS = {
    "rock" : "paper",
    "scissors" : "rock",
    "paper": "scissors"
}

user_input = input(">")

if user_input in LOSE_CONDITIONS:
    print("Sorry, but the computer chose ", LOSE_CONDITIONS[user_input])
