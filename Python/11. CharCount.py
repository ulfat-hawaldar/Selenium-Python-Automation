from collections import Counter

word = "aabbcccdd"
print(''.join([f"{char}{count}" for char, count in Counter(word).items() if count > 1]))

#Counter(word) counts the occurrences of each character.
#A list comprehension filters and formats characters with a count greater than 1.
#''.join() combines the formatted strings into one single output without any extra spaces.