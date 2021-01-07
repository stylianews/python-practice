import random

answer = random.randint(1,10)
print(answer)   # TODO: Remove after testing

print("Please guess number between 1 and 10: ")
guess = 0
while guess != answer:
    try:
        guess = int(input())

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


