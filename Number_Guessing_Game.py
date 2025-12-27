import random

num = random.randint(1, 10)

while True:
    guess = int(input("Guess number (1-10): "))

    if guess == num:
        print("Correct! You won 🎉")
        break
    elif guess > num:
        print("Too high")
    else:
        print("Too low")
