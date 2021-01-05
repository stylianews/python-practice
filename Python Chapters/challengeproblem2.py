# Find the smallest number in list

LIST = [1, 2, 7, 2, -1990, -2000, 5, 100000000000]
smallnumber = LIST[0]
for i in range(0,7):
    if LIST[i] < smallnumber:
        smallnumber = LIST[i]
print(smallnumber)
