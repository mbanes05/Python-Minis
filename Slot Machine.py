import random

print(''''This is a slot machine game. If you win, you earn 10x the amount you spent. 
Your balance is $100. Get to $1,000 to win.''')
balance = 100
slots = [':)', ':(', ':|']

while True:
    spent = input('How much would you like to spend or (q) to quit: ')
    print('')
    if spent == 'q':
        print('You lose.')
        break
    spent = int(spent)
    if spent > balance or spent < 0:
        print("Invalid Amount.")
        continue

    slot1 = slots[random.randint(0, 2)]
    slot2 = slots[random.randint(0, 2)]
    slot3 = slots[random.randint(0, 2)]
    balance -= spent
    print(slot1, slot2, slot3)
    if slot1 == slot2 and slot2 == slot3:
        balance += spent * 10
        print("WINNER WINNER CHICKEN DINNER!")

    print('New balance: $' + str(balance))
    if balance <= 0:
        print('You lose.')
        break
    if balance >= 1000:
        print('YOU WIN!')
        break
