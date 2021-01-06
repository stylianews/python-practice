shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# Use continue
for item in shopping_list:
    if item == "spam":
        # Continue causes all remaining code in the block to be ignored when we have item == spam
        # Continue makes code easier to read
        continue

    print("Buy " + item)

print("-"*8)

# Use break
for item in shopping_list:
    if item == "spam":
        break

    print("Buy " + item)