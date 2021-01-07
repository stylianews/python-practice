# Create a code so that it stops printing when it reaches a number greater than zero that's exactly divisible by 11.
# That number should be the last value printed.
# Reminder: If a value, x, is divisible by 11 then x % 11 will be zero.
# Hint: 0 is exactly divisible by every number, so your solution will need to allow for that.

# Modify the code inside this loop to stop when i is greater than zero and exactly divisible by 11
for i in range(0, 100, 7):
    print(i)
    if i % 11 == 0 and i != 0:
        break
