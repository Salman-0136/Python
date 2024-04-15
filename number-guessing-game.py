import random

print("Welcome to Random Number Guessing Game!")

def guessNumber():
    start = input("Select from where the number starts from: ")
    end = input("Select where the number ends: ")
    start = int(start)
    end = int(end)

    randomNumber = random.randint(start, end)

    while True:
        guess = input("Guess the number: ")
        guess = int(guess)
        if guess == randomNumber:
            print("You guessed it right!")
            break
        elif guess > randomNumber:
            print("Your guess is too high!")
        elif guess < randomNumber:
            print("Your guess is too low!")

def playGame():
    answer = input("Do you want to play game? ")
    if answer.lower() == "yes":
        guessNumber()
    else:
        print("Thank you for playing!")

playGame()
