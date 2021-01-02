for i in range(1,20): # 20 is not included
    print("i is now {}".format(i))
    # print("i is now", i)

# When we start from 0 we don't need to state an initial value
for i in range(20): # 20 is not included
    print("i is now {}".format(i))
    # print("i is now", i)

# If we want to use step, we need an initial value
for i in range(0,20,2): # 20 is not included
    print("i is now {}".format(i))
    # print("i is now", i)

# If we want to go backwards, then we can use minus step
for i in range(10,0,-2): # 20 is not included
    print("i is now {}".format(i))
    # print("i is now", i)

print("-"*80)

age = int(input("How old are you? "))

# Chained operation can be simplified
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time!")

# Using range
if age in range(16,66):
    print("Have a good day at work")
else:
    print("Enjoy your free time!")
