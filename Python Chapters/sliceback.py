letters = "abcdefghijklmnopqrstuvwxyz"

backwards = letters[25::-1]
backwards2 = letters[::-1]
#backwards = letters[25::-1] will not work
print(backwards)
print(backwards2)

# Create a slice that produces the characters qpo
print(letters[16:13:-1])

# Slice the string to produce edcba

print(letters[4::-1])

# Slice the string to produce the last 8 characters in reverse order

print(letters[:-9:-1])

#------
#Printing last 4 values
print(letters[-4:])
print(letters[-1:])

#printing first letter
print(letters[:1])
#not print(letters[1:])
print(letters[0])
#if letters was empty it would give an index error ^^


