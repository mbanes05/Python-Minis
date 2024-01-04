import random

User_score = 0
Com_score = 0
options = ['Rock', 'Paper', 'Scissors']
print("5 wins to finish the game")

while True:
    computer = random.randrange(3)
    user = int(input("0 for Rock, 1 for Paper, or 2 for Scissors or (q) to quit: "))

    # Parameters
    if user > 2 or user < 0:
        print("""
        Invalid Amount
        """)
        continue
    if user == 'q':
        print("Thanks for Playing!")
        break

    print("")
    print("Computer played", options[computer])
    if computer == user:
        print("Match")
    if computer == 0 and user == 2 or computer == 1 and user == 0 or computer == 2 and user == 1:
        print("Computer Wins!")
        Com_score += 1
    if user == 0 and computer == 2 or user == 1 and computer == 0 or user == 2 and computer == 1:
        print("User Wins!")
        User_score += 1

    # Ends the game
    if User_score == 5:
        print("You Won!")
        break
    if Com_score == 5:
        print("You Lost!")
        break
    print("User:", User_score, "Computer:", Com_score)
