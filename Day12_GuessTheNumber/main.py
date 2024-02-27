import random
from art import logo

print(logo)
print("Welcome to the Number guessing game!")
print("I'm thinking of a number between 1 and 100")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == 'easy':
    nChances = 10
else:
    nChances = 5

n = nChances
rNumber = random.randint(1, 100)

while not n == 0:
    print(f"You have {n} attempts left.")
    guess = int(input("Make a guess: "))
    if guess > rNumber:
        print("Too high.")
        n -= 1
    elif guess < rNumber:
        print("Too Low.")
        n -= 1
    else:
        print(f"✅Correct guess. The number was {rNumber}")
        break

if n == 0:
	print(f"You are out of moves. The correct number was {rNumber}")