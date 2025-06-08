#Python Quiz Game

questions = (
    "What color is the sky on a clear day? ",
    "How many legs does a spider have? ",
    "Which planet is known as the 'Red Planet'? ",
    "What do bees make? "
)

options = (
    ("a. Blue", "b. Violet", "c. Red"),
    ("a. 7", "b. 6", "c. 8"),
    ("a. Venus", "b. Mars", "c. Saturn"),
    ("a. Honey", "b. Jam", "c. Olives")
)

answers = ("a", "c", "b", "a")
score = 0

gameStart = input('Press Y to start: ')

if gameStart.lower() == 'y':
    for question_num in range(len(questions)):
        print("\n" + questions[question_num])

        for option in options[question_num]:
            print(option)

        ans = input('Enter answer: ')

        if ans == answers[question_num]:
            print('Correct!')
            score += 1
        else:
            print('Wrong!')
    
    print('--------------')
    print(f'Your total score is: {score}')

