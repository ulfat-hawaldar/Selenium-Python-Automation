def check_anagram(str1, str2):
    return "It is an Anagram" if sorted(str1) == sorted(str2) else "It is Not an Anagram"

# Test
print(check_anagram("EAT", "AET"))
