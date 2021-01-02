activity = input("What would you like to do today? ")

# cinema is case sensitive
if "cinema" not in activity:
    print("But I want to go to the cinema")

# .casefold() will fix the problem
if "cinema" not in activity.casefold():
    print("But I want to go to the cinema")

# more types and methods ---> stdtypes
