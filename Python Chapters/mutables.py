shopping_list = ["milk",
                 "pasta",
                 "eggs",
                 "spam",
                 "bread",
                 "rice"
                 ]

another_list = shopping_list
print(id(shopping_list))
print(id(shopping_list))

shopping_list += ["cookies"]
print(shopping_list)
print(id(shopping_list))
