name = input("Please enter your name: ")
age = int(input("How old are you, {0}? ".format(name)))
print(age)
if age >= 18:
    print("The person can vote")
    print("Please put an X in the box")
else:
    print("The person cannot vote")
    print("Please come back in {0} years".format(18 - age))

# if age < 18:
#     print("Please come back in {0} years".format(18 - age))
# else:
#     print("The person can vote")
#     print("Please put an X in the box")



