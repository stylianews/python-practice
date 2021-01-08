import random

highest = 1000
answer = random.randint(1,highest)
print(answer)   # TODO: Remove after testing

print("Please guess number between 1 and {}: ".format(highest))
guess = 0
while guess != answer:
    try:
        guess = int(input())
        if guess == 0:
            break
        if guess == answer:
            print("Well done!")
            break
        else:
            if guess < answer:
                print("The number is higher")
            else:
                print("The number is lower")

    except ValueError:
        print("This is not a number")


