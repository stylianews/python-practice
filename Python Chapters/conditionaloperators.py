answer = 5

print("Please guess number between 1 and 10: ")
guess = int(input())

if guess != answer:
    if guess < answer:
        print("Please guess higher")
    else:   # guess must be greater than answer
        print("Please guess lower")
    guess = int(input()) # Second try to guess the number
    if guess == answer:
        print("Well done, you guessed it")
    else:
        print("Sorry, you have not guessed it correctly")
else:
    print("Sorry you got it first time")

# if guess < answer:
#     print("Please guess higher")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You lost")
# elif guess > answer:
#     print("Please guess lower")
#     guess = int(input())
#     if guess == answer:
#         print("Well done, you guessed it")
#     else:
#         print("You lost")
# else:
#     print("Ypu got it first time")