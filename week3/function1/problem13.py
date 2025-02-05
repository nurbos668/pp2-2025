import random

print("Hello! What is your name?")
name = input()

print(f"Well, {name}, I am thinking of a number between 1 and 20.", "Take a guess.", sep='\n')
num = random.randint(1, 20)
cnt = 0

while True:
    cnt += 1
    n = int(input())

    if num > n:
        print("Your guess is too low.", "Take a guess.", sep='\n')
        continue

    elif num < n:
        print("Your guess is too high.", "Take a guess.", sep='\n')
        continue

    else:
        print(f"Good job, {name}! You guessed my number in {cnt} guesses!")
        break