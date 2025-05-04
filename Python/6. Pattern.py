rows = 5

for i in range(1, rows + 1):   #loop from 1 to 5.
    spaces = rows - i  #how many spaces before stars.
    stars = 2 * i - 1  #how many stars in that row.
    print(" " * spaces + "*" * stars)  #spaces + stars, together forming a centered pyramid