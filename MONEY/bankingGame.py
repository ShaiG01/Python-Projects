#Welcome to bank for the cuties

import time
import json

running = True
balance = 0
pin = ""

def loadData():
    global balance, pin
    try:
        with open("bankdata.json", "r") as f:
            data = json.load(f)
            balance = data.get("balance", 0)
            pin = data.get("pin", "")
    except FileNotFoundError:
        balance = 0
        pin = ""


def saveData():
    with open("bankdata.json", "w") as f:
        json.dump({"balance": balance, "pin": pin}, f)

def showBalance():
    global balance
    print('...')
    time.sleep(2)
    print('------------------------')
    print('\n' + f'total balance is: ${balance}')
    print('------------------------')

def deposit():
    try:
        global balance
        howMuch = int(input('How much would you like to deposit? (enter digits only): '))
        time.sleep(1)
        print(f'Okay! Depositing ${howMuch} amount... ')
        time.sleep(2)
        print(f'Deposit for ${howMuch} is successful!')
        balance = balance + howMuch
        saveData()
        return balance
    except (ValueError, TypeError):
        print('Enter Digits Only! Try again.')

def withdraw():
    global balance
    try:
        howMuch = int(input('How much would you like to withdraw?(Enter digits only): '))

        if howMuch > balance:
            print(f'Not enough balance to make a withdrawal of ${howMuch} amount...')
        else:
            confirmation = input(f'Proceed to widthraw ${howMuch}?(Y/N): ')
            if confirmation.lower() == 'y': 
                time.sleep(1)
                print(f'Okay! Withdrawing ${howMuch} from your account...')
                balance -= howMuch
                time.sleep(2)
                print(f'Withdrwal is successful!')
                return balance
    except (ValueError, TypeError):
        print('Enter Digits Only! Try again.')

def transfer():
    global balance
    toWhom = input('Input name of the receiver: ')
    try:
        howMuch = int(input('How much would you like to transfer?(enter digits only): '))

        if howMuch > balance:
            print(f'You do not have enough balance to make a transfer of ${howMuch} amount.')
        else:
            confirmation = input(f'Proceed to tranfer ${howMuch} to {toWhom}?(Y/N): ')

            if confirmation.lower() == 'y':
                time.sleep(1)
                print('Okay! Transfering process ongoing...')
                balance -= howMuch
                time.sleep(2)
                print(f'Transfer successful!')
                saveData()
                return balance
    except (ValueError, TypeError):
        print('Enter Digits Only! Try again.')
        


def setPin():
    global pin
    newpin = input('Enter your 6-digit pin: ')

    if len(newpin) > 6:
        print('Should be 6 digits. Try again!')
    if len(newpin) < 6:
        print('Should be 6 digits. Try again')
    else:
        print('Setting new pin...')

        time.sleep(2)
        print('Successful!')
        pin = newpin
    saveData()
    
def changePin():
    global pin
    print('---Change pin---')
    newpin = input('Enter your 6-digit pin: ')

    if len(newpin) > 6:
        print('Should be 6 digits.')
    if len(newpin) < 6:
        print('Should be 6 digits.')
    if newpin == pin:
        print('\n' + 'New pin should be a different one!')
    else:
        print('Setting new pin...')

        time.sleep(2)
        print('Successful!')
        pin = newpin
    saveData()





def bankGame():
    global running
    loadData()

    def pressToStart():
        global running
        press = input('Press s to start: ')
        if press.lower() == "s":
            running = True
            print('Welcome to bank for the cuties!')

    pressToStart()

    while running == True:
        whatToDo = '''
        What would you like to do?

        1. Show balance
        2. Deposit
        3. Withdraw
        4. Exit Bank
        5. Transfer
        6. Set/Change Pin
        '''
        print(whatToDo)

        action = int(input("> "))

        if action == 4:
            running = False
            break

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

        
        if action ==2:
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

        if action == 3:
            if pin == "":
                print('You have no pin yet.')
                setPin()
            else: 
                enter = input('Enter pin code: ')
                if enter == pin:
                    withdraw()
                else:
                    time.sleep(1)
                    print('Wrong pin. Try again.')
        
        if action == 5:
            if pin == "":
                print('You have no pin yet.')
                setPin()
            else: 
                enter = input('Enter pin code: ')
                if enter == pin:
                    transfer()
                else:
                    time.sleep(1)
                    print('Wrong pin. Try again.')

        if action == 6:
            if pin == "":
                print('You have no pin yet.')
                setPin()
            else:
                enter = input('Enter old pin code: ')
                if enter == pin:
                    changePin()
                else:
                    time.sleep(1)
                    print('Wrong pin. Try again.')
            




if __name__ == "__main__":
    bankGame()


