import random
dice = []
total = 0

dice_faces = {
    1: (
            "┌───────┐",
            "│       │",
            "│   ●   │",
            "│       │",
            "└───────┘"
        ),
    2: (
            "┌───────┐",
            "│ ●     │",
            "│       │",
            "│     ● │",
            "└───────┘"
        ),
    3: (
            "┌───────┐",
            "│ ●     │",
            "│   ●   │",
            "│     ● │",
            "└───────┘"
        ),
    4: (
            "┌───────┐",
            "│ ●   ● │",
            "│       │",
            "│ ●   ● │",
            "└───────┘"
        ),
    5: (
            "┌───────┐",
            "│ ●   ● │",
            "│   ●   │",
            "│ ●   ● │",
            "└───────┘"
    ),
     6: (
            "┌───────┐",
            "│ ●   ● │",
            "│ ●   ● │",
            "│ ●   ● │",
            "└───────┘"
    ),
}


number = int(input('How many dice to roll: '))

for die in range(number):
    dice.append(random.randint(1,6))


for die in dice:
    total += die



for DICE in dice:
    for line in dice_faces[DICE]:
        print(line)


print('\n' + f'you have rolled: {dice}')

print('------------')
print(f'total: {total}')
print('------------')