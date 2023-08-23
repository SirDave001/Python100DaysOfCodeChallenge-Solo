import random

def guess_game():
    play_again = "y"
    while play_again == "y":
        answer = random.randint(1, 100)
        guess = int(input("Guess a number between 1 and 100: "))
        counter = 0
        while guess != answer:
            if guess < answer:
                print("Guess is low.")
            if guess > answer:
                print("Guess is high.")
            guess = int(input("Guess a number between 1 and 100: "))
            #each time the loop is iterated counter is increased by one
            counter += 1
        print(f"You guessed right! You tried {counter} times.")
        play_again = input("Do you want to play again?")
        
guess_game()