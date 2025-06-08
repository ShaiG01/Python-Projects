# Slot Machine

import json
import time
import random
from bankingGame import setPin

bet = 0
symbols = ["🌸", "🌷", "🌼", "🌈", "🍄", "🌙"]

# Load bank data from JSON
def loadBankData():
    try:
        with open("bankdata.json", "r") as f:
            data = json.load(f)
            return data  # returns a dictionary
    except FileNotFoundError:
        return {"balance": 0, "pin": ""}

# Save bank data back to JSON
def saveBankData(data):
    with open("bankdata.json", "w") as f:
        json.dump(data, f)

# Load initial data
bank_data = loadBankData()
balance = bank_data["balance"]
pin = bank_data['pin']
running = False


def pressStart():
    global running
    print('Welcome to the ultimate Slot Machine game!')
    print('Rules are simple. Simply place your bet and roll the machine.')
    print("Test your luck and see if you'll double your money!")

    press = input('\n' + 'Press s to start: ')

    if press.lower() == 's':
        running = True


def balanceManipulator():
    global balance
    print('''
          1. Check balance
          2. Deposit
          3. Exit
          ''')

    action = int(input('> '))

    def showBalance():
        print('---------------')
        print(f'Total balance is: ${balance}')
        print('---------------')

    def deposit():
        global balance
        amount = int(input('How much would you like to deposit? '))

        confirmation = input(f'Proceed to deposit ${amount} (Y/N)? ')
        if confirmation.lower() == 'y':
            time.sleep(1)
            print(f'Depositing ${amount} to your balance...')
            time.sleep(2)
            balance += amount
            print('Successful!')
            # Save updated balance
            saveBankData({"balance": balance, "pin": bank_data["pin"]})
            return balance

    if action == 1:
        if pin == "":
                print('You have no pin yet.')
                setPin()
        else: 
            enter = input('Enter pin code: ')
            if enter == pin:
                showBalance()
            else:
                time.sleep(1)
                print('Wrong pin. Try again.')

    elif action == 2:
        if pin == "":
                print('You have no pin yet.')
                setPin()
        else: 
            enter = input('Enter pin code: ')
            if enter == pin:
                deposit()
            else:
                time.sleep(1)
                print('Wrong pin. Try again.')

    elif action == 3:
        print("Exiting...")
        return


def generateRandomIndex():
    index = random.randint(0, len(symbols) - 1)
    return index
    
def rollSymbols():
    global balance
    object1= symbols[generateRandomIndex()]
    object2 = symbols[generateRandomIndex()]
    object3 = symbols[generateRandomIndex()]
    print('Rolling...')
    time.sleep(2)

    print(f'''
            ************
            |{object1} |{object2} | {object3}|
            ************
            ''')

    if object1 == object2 == object3:
        print('You win!')
        time.sleep(1)
        print(f'${bet*2} is added to your bank account!')
        balance += (bet*2)
        return balance 

    else: 
        print('Sorry. You lost this round.')
        print(f'${bet} is taken from your bank account!')
        balance -= bet
        return balance

def startGame():
    global bet
    try:
        bet = 0
        placeBet = int(input('Place your bet: $'))
        if placeBet > balance:
            print('Not enough balance to play.')
        else:
            bet = placeBet
            time.sleep(1)
            print(f'You have risked ${bet} of your money!')

            print('\n' + 'Here are the symbols: 🌸 🌷 🌼 🌈 🍄 🌙')

            roll = input('\n' + 'Press r to roll: ')

            if roll.lower() =='r':
                rollSymbols()
    except ValueError:
        print('Invalid input. Only enter numbers!')

    

# Start the game
pressStart()

while running:
    action = int(input("\n" + "What would you like to do?\n1. Start Game\n2. Check/Deposit Balance\n> "))

    if action == 1:
        startGame()
        saveBankData({"balance": balance, "pin": bank_data["pin"]})
    elif action == 2:
        balanceManipulator()

