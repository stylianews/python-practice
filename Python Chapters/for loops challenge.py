# Write a program to print out the capital letters in the string
# "Alright, but apart from the Sanitation, the Medicine, Education, Wine, " \
# "Public Order, Irrigation, Roads, the Fresh-Water System, and Public Health, " \
# "what have the Romans ever done for us?"
# Check out the string methods for one way to test if a character is in uppercase.

capital = ""
quote = """
Alright, but apart from the Sanitation, the Medicine, Education, Wine,
Public Order, Irrigation, Roads, the Fresh-Water System,
and Public Health, what have the Romans ever done for us?
"""

# Use a for loop and an if statement to print just the capitals in the quote above.

for char in quote:
    if char.isupper():
        capital = capital + char
print(capital)