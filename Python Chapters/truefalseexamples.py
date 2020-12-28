if 0:
    print("True")
else:
    print("False")

name = input("please enter your name: ")
if name:
    print("Hello, {}".format(name))
else:
    print("Are you the man with no name?")

# More clear way to sepcify an empty string

if name != "":
    print("Hello {}".format(name))
else:
    print("There is no name")