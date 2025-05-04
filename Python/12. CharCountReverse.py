# Input string where each letter is followed by a number representing how many times it repeats
word = "a2b4c1"

# Loop through the string in steps of 2 (to handle the character and its corresponding count)
for i in range(0, len(word), 2):
    # The character is at index i (e.g., 'a', 'b', 'c', etc.)
    char = word[i]

    # The count is at index i+1 (the number after the character)
    count = int(word[i + 1])  # Convert the count to an integer

    # Print the character repeated 'count' times
    print(char * count, end="")  # end="" ensures the output is on the same line
