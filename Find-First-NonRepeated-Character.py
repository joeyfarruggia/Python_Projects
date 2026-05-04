#find the first non repeated character in a string

from collections import Counter

def first_non_repeated_character(string):
    char_count = Counter(string)
    for char in string:
        if char_count[char] == 1:
            return char
    return None

print(first_non_repeated_character("swiss"))  # Output: 'w'
print(first_non_repeated_character("abracadabra"))  # Output: 'c'
print(first_non_repeated_character("aabbcc"))  # Output: None