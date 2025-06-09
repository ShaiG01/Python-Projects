#wordle
import random
import time

from colorama import init, Fore, Style
init()

wordleWords = ["apple", "grape", "stone", "plant", "brave",
  "crane", "flame", "smile", "shard", "sugar",
  "light", "night", "piano", "dream", "spear",
  "bread", "crown", "blink", "glove", "quiet",
  "charm", "sweep", "vivid", "flock", "trace",
  "frost", "angle", "flute", "whale", "spice", "floss"]




letters = []
newLetters = ["_", "_", "_", "_","_"]
userInput = []
wrongPosition = []
chances = 0
wrong = []
Random = ""

def main():
    global newLetters
    global chances
    global Random
    while True:
        print('''
    Welcome to wordle! Find the mystery word to win.
    click 's' to start and 'q' to quit.
              ''')
        
        action = input('> ')

        if action.lower() == 'q':
            break

        if action.lower() == 's':
            generateRandomWord()
            for letter in Random:
                letters.append(letter)

            while chances  <= 5:
                word = input('Enter word: ')

                if len(word) != 5:
                    print('Make sure to print 5-letter world')

                if word == Random:
                    time.sleep(2)
                    print('\n' + 'Victory! You win.')
                    print(f'word is: {Random}')
                    break

                          
                
                if len(word) == 5:
                
                    for letter in word.lower():
                        userInput.append(letter);
            
                    for i, letter in enumerate(userInput):
                        if letter in letters:
                            if word[i] == letters[i]:
                                newLetters[i] = Fore.GREEN + Style.BRIGHT + letter + Style.RESET_ALL
                                letters[i] = ""
                    
                                            
                               

                            else:
                                wrongPosition.append(letter)
                                newLetters[i] = Fore.YELLOW + Style.BRIGHT + letter + Style.RESET_ALL
                                
                                for sym in wrongPosition:
                                    if sym not in letters:
                                        wrongPosition.remove(sym)
                                        
                        else:
                            newLetters[i] = Fore.RED + Style.BRIGHT + letter + Style.RESET_ALL
                            if letter not in wrong:
                                wrong.append(letter)

                    time.sleep(2)

                  
                      
                    print('--------------------------------')
                    print('\n')
                    for letter in newLetters: 
                        print(f'[{letter}]', end=".")
                        

                    
                   
                    print('\n')          
                    print(f'{wrongPosition} is/are misplaced!')
                    print('\n') 
                    print(f'{wrong} is/are not included.') 
                    chances += 1
                    print(f'You have lost {chances}/5 chance.')

                    print('--------------------------------')

                    letters.clear()
                    for letter in Random:
                        letters.append(letter)
                      
                    userInput.clear()
                    wrongPosition.clear()
                    newLetters =  ["_", "_", "_", "_","_"]
                  

                    
            
            letters.clear()
            userInput.clear()
            wrongPosition.clear()
            wrong.clear()
        letters.clear()
        newLetters = ["_", "_", "_", "_","_"]
        userInput.clear()
        wrongPosition.clear()
        wrong.clear()
        print('\n' + 'You lost. Maybe try again?' + '\n')


    



def generateRandomWord():
    global Random
    randomWord = random.choice(wordleWords)
    Random = randomWord
    print(Random)





if __name__ == '__main__':
  
    

    main()
