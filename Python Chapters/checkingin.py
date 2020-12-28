parrot = "Norwegian Parrot"

letter = input("Enter a character: ")

# String comparisons are case sensitive!!
if letter in parrot:
    print("{} is in {}".format(letter, parrot))
else:
    print("I don't need that letter")