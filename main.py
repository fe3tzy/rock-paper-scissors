import random

options = ['rock', 'paper' , 'scissors']
running = True
aiscore = 0
plrscore = 0
print('Welcome to my GAME')
while running:

    player = None
    computer = random.choice(options)

    print('Options : '+str(options))
    while player not in options:
        player = input('Enter a choice: ')

        continue

    print(f'Player: {player}')
    print(f'Computer: {computer}')


    if player == computer:
        print('Its a tie!')
        print('Player score: ' + str(plrscore))
        print('Computer score: ' + str(aiscore))
    elif player == 'rock' and computer == 'paper':
        print('You lost!')
        aiscore = aiscore + 1
        print('Player score: ' + str(plrscore))
        print('Computer score: ' + str(aiscore))
    elif player == 'paper' and computer == 'scissors':
        print('You lost!')
        aiscore = aiscore + 1
        print('Player score: ' + str(plrscore))
        print('Computer score: ' + str(aiscore))
    elif player == 'scissors' and computer == 'rock':
        print('You lost!')
        aiscore = aiscore + 1
        print('Player score: ' + str(plrscore))
        print('Computer score: ' + str(aiscore))
    else:
        print('You won!')
        plrscore = plrscore + 1
        print('Player score: ' + str(plrscore))
        print('Computer score: ' + str(aiscore))

    rematch = input('Play again? (y/n): ').lower()
    if not rematch == 'y':
        running = False
        print('Thanks for playing!')
        aiscore = 0
        plrscore = 0
    else:
        running = True
