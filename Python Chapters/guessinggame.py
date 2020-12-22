answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess == answer:
    print("You got it first time!")
elif guess < answer:
    print("Please guess higher")
else:
    print("Please guess lower")
