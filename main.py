import random
user_wins = 0
computer_wins = 0

options = ["rock","paper","scissors"]
while True:
    user_input = input("type Rock/paper/scissors or Q to quit:").lower()
    if user_unput == "q":
        break
    if user_input not in option:
        continue
    random_number = random.randit(0,2)
    computer_pick = options