import random

draws = 0
wins = 0
losses = 0
is_ended = False
prompt = "Choose Rock(r), Paper(p), Scissors(s) or 'q' tp quit: "

while True:
    user_choice = input(prompt)
    while user_choice not in ['r', 'p', 's', 'q']:
        user_choice = input(prompt)
    if user_choice == 'q':
        is_ended = True
        if is_ended == True:
            break
    else:
        computer_choice = random.choice(['r', 'p', 's'])
        if computer_choice == 'r':
            move = 'rock'
        elif computer_choice == 'p':
            move = 'paper'
        else:
            move = 'scissors'
        print(f'Computer gives a {move} move.')
        if computer_choice == user_choice:
            print('Draw!')
            draws += 1
        elif computer_choice == 'r' and user_choice == 's'\
            or computer_choice == 'p' and user_choice == 's'\
            or computer_choice == 's' and user_choice == 'r':
            print('You win!')
            wins += 1
        else:
            print('You lose!')
            losses += 1
print(f'You had {wins} win(s), {draws} draw(s) and {losses} loss(es).')
        