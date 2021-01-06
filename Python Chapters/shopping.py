shopping_list = ["milk", "pasta", "eggs", "spam", "bread", "rice"]

# Iterates over a list
for item in shopping_list:
    # Exclude spam
    if item != "spam":
        print("Buy " + item)

print("-"*8)

# Use continue
for item in shopping_list:
    if item == "spam":
        continue

    print("Buy " + item)
