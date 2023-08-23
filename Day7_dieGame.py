import random

start_place = 0
end_place = 50
user_place = 0
computer_place = 0
user_win = False
computer_win = False
quit_game = False

while not user_win or not computer_win:
    user_input = input("Enter 't' to toss a die, or 'q' to quit the game: ")
    if user_input == 'q':
        quit_game = True
        break
    if user_input == 't':
        user_move = random.randint(1, 6)
        user_place += user_move
        print(f'You move for {user_move} steps.')
        if user_place > end_place:
            overshoot = user_place - end_place
            user_place = end_place - over_shoot
        print(f'You are now at {user_place}')
        if user_place == end_place:
            user_win = True
            break
    computer_move = random.randint(1, 6)
    computer_place += computer_move
    print(f'Computer moves for {computer_move} steps.')
    if computer_place > end_place:
        over_shoot = computer_place - end_place
        computer_place = end_place - over_shoot
    print(f'Computer is at position {computer_place}')
    if computer_place == end_place:
        computer_win = True
        break
if quit_game:
    print(f'You have quit the game. You need {end_place - user_place} steps to win')
elif user_win:
    print('User Wins!')
elif computer_win:
    print('Computer Wins!')
    
    
    