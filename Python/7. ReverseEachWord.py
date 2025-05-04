text = "Welcome To India"
output = ' '.join([w[::-1] for w in text.split()])
print(output)

#.split() → breaks the sentence into words.
#word[::-1] → reverses each word.
#' '.join(...) → joins them back with spaces.