rows = int(input('Enter the number of rows'))  # Taking the number of rows from the user
# outer loop
for i in range(rows):  # This loop runs from 0 to rows-1
    # nested loop
    for j in range(i+1):  # This loop runs from 0 to i, so it runs i+1 times
        # display number
        print(i, end=' ')  # Prints the value of i followed by a space on the same line
    # new line after each row
    print('')  # Moves to the next line after each row