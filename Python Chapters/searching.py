shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

item_to_find = "spam"

# Position in the list "found_at"
# None is kinda equal to null
found_at = None

# len function is used to get how many items are in a sequence
for index in range(len(shopping_list)):
    if shopping_list[index] == item_to_find:
        found_at = index
        break
# Counting starts at zero, so if we need to find the position in the list we need to add 1
print("Item found at position {}".format(int(found_at)+1))