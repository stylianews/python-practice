#         000000000011111
#         012345678901234
parrot = "Norwegian Blue"
print(parrot)
print(parrot[3])
print(parrot[4])
print(parrot[9])
print(parrot[3])
print(parrot[6])
print(parrot[8])
# EVERYTHINGS START COUNTING FROM ZERO
print()

print(parrot[-11])
print(parrot[-1])
print(parrot[-5])
print(parrot[-11])
print(parrot[-8])
print(parrot[-6])

print()

print(parrot[3-14])
print(parrot[4-14])
print(parrot[9-14])
print(parrot[3-14])
print(parrot[6-14])
print(parrot[8-14])

print()

parrot = "Norwegian Blue"
print(parrot[0:6])
# Norweg
# Last character is not included in slicing #Up to but no including!!!!
print(parrot[0:9])
print(parrot[:9])
print(parrot[10:])
# The inverse does not start from 0
parrot = "Norwegian Blue"
print(parrot[:6]+parrot[6:])
print(parrot[:])
print(parrot)
print()
print(parrot[-6:12])

#If we want to add steps in our slicing

parrot = "Norwegian Blue"
print(parrot[2:7:2])

number = "9,223;372:036 854"
seperators = number[1::4]
print(seperators)

values = "".join(char if char not in seperators else " " for char in number).split()
print([int(val) for val in values])

