import random


def computer_guess():
    play_again = "y"
    min_value = 1
    max_value = 100
    guess = random.randint(min_value, max_value)
    while play_again == "y":
        print(f"The computer guess is {guess}")
        guide = "n"
        counter = 0
        while guide != "c":
            guide = input("Is the guess high(h), Low(l) or correct(c)?: ")
            # print(guide)
            if guide == "h":
                if guess < max_value:
                    max_value = guess - 1
                guess = random.randint(min_value, max_value)
                print(guess)
            if guide == "l":
                if guess > min_value:
                    min_value = guess + 1
                guess = random.randint(min_value, max_value)
                print(guess)
            counter += 1
        print(f"I got {guess} right after {counter} times!")
        play_again = input("Do you want to play again? ")
    
computer_guess()