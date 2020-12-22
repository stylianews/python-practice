age = int(input("How old are you? "))

if age >= 16 and age <= 65: # "AND" in Python stops checking aas soon as it finds one condition that is False
    print("Have a good day at work")

# Chained operation can be simplified
if 16 <= age <= 65:
    print("Have a good day at work")
else:
    print("Enjoy your free time!")

print("-" * 80)

if age < 16 or age > 65: # "OR" in Python stops checking aas soon as it finds one condition that is True
    print("Enjoy your free time")
else:
    print("Have a good day at work")

# True and True gives True
# True and False gives False
# False and False gives False
#
# True or True gives True
# True or False gives True
# False or False gives False


