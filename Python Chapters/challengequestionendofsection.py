# Write a program to print a number of otions, and allow the user to select an option from the list.
# The options should be numbered from 1- 9 - although you can use less that 9 options if you want
# Make sure the are at least 4 options.

list = [ "Exit", "Learn Python", "Learn Java", "Go swimming", "Have Dinner", "Go to bed"]
numbers = ["0", "1", "2", "3", "4", "5"]
selection = ""

while selection not in numbers:
    print("Please choose your option from the list below: ")
    for i in range(0,6):
        print(str(numbers[i]) + "." + " " + list[i])

    selection = input("Please type the number of the selection you want: ")

    if selection in numbers:
        if selection == "0":
            print("You are exitining the program")
        else:
            print("You selected option {}. Transfering you to '{}'".format(selection, list[int(selection)]))
            break
    else:
        print()
        print("-"*10)
        print("You selected option {}".format(selection))
        print("This is not a valid option, try again")
        print("-"*10)
        print()
else:
    print("Bye Bye")