import random

number = random.randint(1, 100)
attempts = 0

print("number-guessing game")
print("i'm thinking of a number between 1 and 100.")

while True:
    guess = int(input("enter your guess: "))
    attempts += 1

    if guess < number:
        print("too low! ")
    elif guess > number:
        print("too high! ")
    else:
        print(f"correct! the number was {number}.")
        print(f"you got it in {attempts} attempts!")
        break
