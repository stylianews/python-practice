# The lines are not displayed nicely.
for i in range(1,13):
    print("No. {0} squared is {1} and cubed is {2}".format(i, i ** 2, i ** 3))

# The lines are displayed nicely.
for i in range(1,13):
    print("No. {0:2} squared is {1:3} and cubed is {2:4}".format(i, i ** 2, i ** 3))

print()

# Left aligned or right aligned or center aligned
for i in range(1,13):
    print("No. {0:2} squared is {1:<3} and cubed is {2:<4} and ^4 is {3:^5}".format(i, i ** 2, i ** 3, i ** 4))

print()

print("Pi is approx {0:12}".format(22/7))
print("Pi is approx {0:12f}".format(22/7))
print("Pi is approx {0:12.50f}".format(22/7))
print("Pi is approx {0:52.50f}".format(22/7))
print("Pi is approx {0:62.50f}".format(22/7))
print("Pi is approx {0:<72.50f}".format(22/7))
print("Pi is approx {0:<72.54f}".format(22/7))
print("Pi is approx {0}".format(22/7))

for i in range(1,13):
    print("No. {} squared is {} and cubed is {} and ^4 is {:>7}".format(i, i ** 2, i ** 3, i ** 4))
