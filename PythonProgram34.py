# Guessing Game

from random import randint

guessNumber = int(input("Enter your guess between 1 to 5 : "))
randomNumber = randint(1,5)


if guessNumber == randomNumber:
    print("You have won")
else:
    print("You have lost")
    print("Random number was : ",randomNumber)
