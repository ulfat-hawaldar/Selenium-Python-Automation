word = "I am Indian".lower()
print([c for c in word if c in "aeiou"],  #list of vowels.
      sum(1 for c in word if c in "aeiou"))  # total vowel count

