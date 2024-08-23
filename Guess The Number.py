#Develop a game where the computer randomly selects a number, and the user has to guess it. This project will help you work with loops and conditionals.
import random
Numbers = [1, 2, 3, 4, 5, 6, 7, 8 ,9 ,10]
Play = True
while Play == True:
    Computer = random.choice(Numbers)
    GuessNum = None
    while GuessNum not in Numbers:
        GuessNum = int(input("Enter Any Number From 1 to 10 Inclusive = "))

    print(f"Players Choice Is {GuessNum}")
    print(f"Computers Choice Is {Computer}")

    if GuessNum == Computer:
        print(f"You Guess It! The Number was {GuessNum}")
    else:
        print("You Didn't Guess Correctly...")
    
    PlayAgain = input("Would You Like To Play The Game Again? (y/n) = ").lower()
    if PlayAgain == "n":
        Play = False


print("Thanks For Playing!")
