# Write a program to print out all the numbers from 0 to 100 that are divisible by 7.
# Note that zero is considered to be divisible by all other integers, so your output should include zero.

numbers = ""

for i in range (0,101):
    if i%7 == 0:
        numbers = numbers + str(i)
print(numbers)

for i in range (0,101):
    if i%7 == 0:
        print(i)

# This solution uses a step value for the range function
for i in range(0, 101, 7):
    print(i)

# This solution uses a slice
for i in range(101)[::7]:
    print(i)