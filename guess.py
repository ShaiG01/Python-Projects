import random
import time

# Fix typo: 'sissors' -> 'scissors'
selection = {
    'rock': {'beats': 'scissors'},
    'paper': {'beats': 'rock'},
    'scissors': {'beats': 'paper'}
}

running = False
yourScore = 0
computerScore = 0

# Pre-create selection list
select = list(selection.keys())

def computerSelection():
    randomIndex = random.randint(0, 2)
    return select[randomIndex]

def iswinner(yourSelection, opponentSelection):
    return selection[yourSelection]['beats'] == opponentSelection

run = input('Press s to start: ')
if run.lower() == 's':
    running = True

while running:
    enterSelection = input('\n' + 'Enter your selection (rock, paper, scissors): ').lower()

    if enterSelection not in selection:
        print('Invalid input!')
        continue

    computerSelect = computerSelection()
    time.sleep(1)
    print(f'Computer selected: {computerSelect}')

    if enterSelection == computerSelect:
        print("It's a tie!")
    elif iswinner(enterSelection, computerSelect):
        print('You win!')
        yourScore += 1
    else:
        print('Computer wins!')
        computerScore += 1

    print(f"Your score: {yourScore} | Computer's score: {computerScore}")
    time.sleep(1)
    tryagain = input('Do you wish to try again? (y/n): ')
    if tryagain.lower() == 'n':
        if yourScore > computerScore:
            print('You win!')
        else:
            print('Computer wins!')
        print('Goodbye!')
        running = False
