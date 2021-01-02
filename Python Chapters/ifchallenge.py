# The challenge asks the user to write a small program
# to ask for a name and an age.
# When both values have been entered, check if the age is 18-30 (over 18 and under 31)
# if they are, welcome them to the holiday. If not then refuse entry

name = input("Hello, what is your name? ")
age = int(input("Hello {}, how old are you? ".format(name)))

if 18 <= age < 31:
    print("Welcome to the holiday! Enjoy!")
else:
    if age < 18:
        print("I am sorry, but you don't meet the age requirements. You need to be older")
    else:
        print("I am sorry, but you don't meet the age requirements. You need to be younger")