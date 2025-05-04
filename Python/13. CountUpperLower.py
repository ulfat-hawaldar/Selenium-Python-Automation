word = "aaBBccDD"

# Loop through the string and print characters based on their case
for char in word:
    if char.isupper():
        print(f"Uppercase Character: {char}")
    elif char.islower():
        print(f"Lowercase Character: {char}")
