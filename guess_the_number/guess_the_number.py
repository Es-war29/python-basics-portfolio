
~
# number guessing game

import random

lowest_num = 1
highest_num = 100

answer = random.randint(lowest_num,highest_num)

guesses = 0
is_running = True

print("Python number guessing game")
print(f"select a number between {lowest_num} and {highest_num}")

while is_running:
    guess = input("Enter you guess:")

    if guess == "q":
            print("Game stopped. Better luck next time!")
            print(f"The present answer is {answer}")
            break

    if guess.isdigit():
        guess = int(guess)
        guesses +=1

        if guess < lowest_num or guess > highest_num:
            print("That is not in range")
            print(f"Please select a number between {lowest_num} and {highest_num}")
        elif guess < answer:
            print("Too low! Try Again!")
        elif guess > answer:
            print("Too high! Try Again!")
        else:
            print(f"Correct! The answer was {answer}")
            print(f"Number of guesses {guesses}")
            is_running = False

    else:
        print("Invalid guess")
        print(f"Please select a number between {lowest_num} and {highest_num}")
