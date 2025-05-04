from collections import Counter

text = "hello"
count = Counter(text)

# Print only characters that appear more than once
for char, freq in count.items():
    if freq > 1:
        print(f"Character: {char} Count: {freq}")

# Full count
print(count)
