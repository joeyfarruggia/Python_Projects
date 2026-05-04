# write a program to check if two strings are anagrams

def are_anagrams(str1, str2):
    return sorted(str1.lower()) == sorted(str2.lower())

# Example usage

print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("hello", "world"))    # False