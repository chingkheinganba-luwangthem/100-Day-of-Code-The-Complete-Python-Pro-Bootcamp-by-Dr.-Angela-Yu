from random import randint
from artt import logo


EASY_LEVEL = 10
HARD_LEVEL =5

def check_answer(guess, answer,turns):
    """ Check answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high")
        return turns -1
    elif guess < answer:
        print("Too low")
        return turns -1
    else:
        print(f"You got it! The answer was {answer}.")

def set_deficulty():
    level = input("Choose difficulty. Type 'easy' or 'hard': ")
    if level == 'easy':
        global turns
        return   EASY_LEVEL
    else:
        return HARD_LEVEL

def game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Choose a defficult. Type'easy' or 'hard'")
    answer = randint(1,100)
    print(f"pass, the correct answer is {answer}")

    turns =set_deficulty()
    guess =0
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))
        turns = check_answer(guess,answer,turns)
        if turns ==0:
            print("You ran out of guess, you lose.")
            return
        elif guess != answer:
            print("Guess again")
game()







