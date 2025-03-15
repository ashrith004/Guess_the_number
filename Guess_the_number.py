# Guessing the correct number 
from random import randint
# Function to check users' guess against actual number
EASY_LEVEL_TURNS = 10
HIGH_LEVEL_TURNS = 5

def check_answer(user_guess , actual_answer,turns):
    """Checks answer and return the number of answer remaining"""
  
    if user_guess > actual_answer:
        print("Guess is TOO HIGH .")
        return turns - 1
    elif user_guess < actual_answer:
        print("Guess is TOO LOW.")
        return turns - 1
    else:
        print("You got it . The answer is{actual_answer}")


# Function to set difficulty>>
def set_difficulty():
    level =input("Choose the difficulty >> Type 'h' for hard or 'e' for easy >> ").lower()
    if level ==  "e": 
        return EASY_LEVEL_TURNS
    else:
        return HIGH_LEVEL_TURNS
def game():
# Choosing a number between 1 an 100 
    print("Welcome to number guessing game >> ")
    print("I'm thinking of a number between 1 and 100 !!")
    answer = randint(0,100)
    print(f"The correct answer is {answer}")

    turns = set_difficulty()
    
# Report the guessing functionality if they get it wrong 


    guess = 0 
    while guess != answer: 
        print(f"You have {turns} remaining to guess the number. ")  
        # Let the user guess a number
        guess = int(input("Guess a number ?  "))
        turns = check_answer(guess, answer, turns)
        if turns == 0:
            print("You are out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again")
     
game()