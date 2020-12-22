day = "Saturday" # Testing values
temperature = 30
raining = True

if day == "Saturday" and temperature > 27 and not raining: # and not -> opposite
    print("Go swimming")
else:
    print("Learn Python")

if day == "Saturday" and temperature > 27 or not raining:
    print("Go swimming")
else:
    print("Learn Python")

# Using parenthesis makes code easier to read especially when using AND and OR together
if (day == "Saturday" and temperature > 27) or not raining:
    print("Go swimming")
else:
    print("Learn Python")