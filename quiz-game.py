def game():
    print("Let's begin with the game!")
    print("**Hint**: Use small caps for all the letter or the first letter of every word can begin with big cap.")
    correctAnswer = 0
    answer = input("What does CPU stand for? ")
    if answer.lower() == "central processing unit":
        print("Correct!")
        correctAnswer += 1
    else:
        print("Wrong!")
    
    answer = input("What 9x9 equals to? ")
    if answer == "81":
        print("Correct!")
        correctAnswer += 1
    else:
        print("Wrong!")
        
    answer = input("What does IEEE stand for? ")
    if answer.lower() == "institute of electrical and electronics engineers":
        print("Correct!")
        correctAnswer += 1
    else:
        print("Wrong!")
        
    answer = input("What is the value of cos at 90? ")
    if answer == "0":
        print("Correct!")
        correctAnswer += 1
    else:
        print("Wrong!")
        
    answer = input("What does MVC stand for in programming? ")
    if answer.lower() == "model view controller":
        print("Correct!")
        correctAnswer += 1
    else:
        print("Wrong!")
        
    totalScore = (correctAnswer / 5) * 100
    print("Your score is " + str(correctAnswer) + " out of 5. You got " + str(totalScore) + "%.")
    
    if totalScore > 80 and totalScore <= 100:
        print("Remarks: Great")
    elif totalScore > 50 and totalScore <= 80:
        print("Remarks: Average")
    else:
        print("Remarks: Poor")
        
    
def quit():
    print("Game Quit......")
    
print("Welcome to our Computer Quiz")
play = input("Do you want to play the quiz game? ")

if play.lower() == "yes":
    game()
else:
    quit()
