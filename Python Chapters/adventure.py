# Use of while loops in an example
available_exits = ["north", "south", "east", "west"]

chosen_exit = ""

# The loop will repeat itself unless the user inputs an available exit
while chosen_exit not in available_exits:
    chosen_exit = input("Please choose a direction: ")

print("arent you glad you got out of there")