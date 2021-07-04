import random
import time

list_of_moves =  ['rock', 'paper', 'scissors']
print('Instruction to play the game:')
print('Type in the keyword rock paper or scissors', end='\n\n')
playerscore = 0
computerscore = 0
draw = 0
while True:
    if playerscore == 5 or computerscore == 5 or draw == 5:
        break


    player = input('Type in the move:')
    print('################################################')
    player = player.lower()
    bot = random.choice(list_of_moves)  # the computer choosing
    if not player in list_of_moves:
        print('Read the instructions properly and try again', end='\n\n')
        quit()
        
    print('The compurer has chosen.........')
    time.sleep(1)
    print(f'{bot}')
    
    if (player == 'paper' and bot == 'rock') or (player == 'scissors' and bot == 'paper') or (player == 'paper' and bot == 'rock') or (player == 'rock' and bot == 'scissors') or (player == 'paper' and bot == 'scissors') or (player == 'scissors' and bot == 'rock'):
        playerscore += 1
    elif player == bot:
        draw += 1
    else:
        computerscore += 1
    print('################################################')
    print(f'Score: player- {playerscore} computer- {computerscore} draw- {draw}')

if playerscore > computerscore:
    print('You have won!!!!!!!!!!!!!!!')
elif computerscore > playerscore:
    print("You lose.........")
else:
    print('It is a draw')

