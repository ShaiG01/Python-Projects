import random
import time

wordsEasy = ("apple", "bread", "chair", "dance", "happy", "light", "money", "quiet", "river", "sleep")
wordsMedium = ("blanket", "dolphin", "imagine", "journey", "mystery", "rainbow", "theater", "trouble", "village", "whisper")
wordsHard = ("atmosphere", "brainstorm", "catastrophe", "dictionary", "enlightened", "handcrafted", "nightingale", "revolution", "trampoline", "watermelon")

currentIndex = 0
wrongs = 0

hangManArt= {   0: (" ",
                    " ",
                    " " ),
                1: (" o ",
                    "   ",
                    "   " ),
                2: (" o " ,
                    " | ",
                    "   " ),
                3: (" o " ,
                    "/| ",
                    "   " ),
                4: (" o " ,
                    "/|\\",
                    "   " ),
                5: (" o " ,
                    "/|\\",
                    "/  " ),
                6: (" o " ,
                    "/|\\",
                    "/ \\ " ),
                 
            }




def countDown():
    time.sleep(2)
    print('ready?')
    time.sleep(1)
    for num in range(3, 0, -1):
        print(num)
        time.sleep(1)
    print('Timer starts now!' + '\n')

    
def indexIncrement():
    global currentIndex
    global wrongs
    currentIndex += 1
    wrongs += 1

def startGame(difficulty):
    mysteryWord = random.choice(difficulty)
    countDown()
    hints = ["_"] * len(mysteryWord)
    while True:
        print('\n')
        print(hints)
        guess = input('Enter letter: ')

        if guess in mysteryWord:
            if guess == mysteryWord:
                time.sleep(1)
                print('victory!! Goodjob.')
                break
            else:
                for i, letter in enumerate(mysteryWord):
                    if guess == letter:
                        hints[i] = guess
        else:
            indexIncrement()
            for line in hangManArt[currentIndex]:
                print(line)
            print(f'{wrongs} out of 6 chances')
        
        if currentIndex == 6:
            time.sleep(1)
            print('You lose.')
            break

        if "_" not in hints:
            time.sleep(1)
            print('Victory!')
            break

    print('\n' + 'gameover')
    print(f'Mystery Word: {mysteryWord}')
        


    

def main():
    while True:
        try:
            time.sleep(1)
            print('\n')
            print('''
                Welcome to the hangman game!
                Select difficulty to start:
                
                1. Easy (1 minute to solve)
                2. Medium (2 minutes to solve)
                3. Hard (3 minutes to solve)

                ''')
            print('Input 10 to exit: ')
            difficulty = int(input('> '))

            if difficulty == 1:
                print('You have selected easy!' + '\n')
                startGame(wordsEasy)
            
            elif difficulty == 2:
                print('You have selected medium!' + '\n')
                startGame(wordsMedium)
            elif difficulty == 3:
                print('You have selected difficult!' + '\n')
                startGame(wordsHard)

            else:
                break

        except ValueError:
            print('Invalid Input')





while __name__== '__main__':
    main()

