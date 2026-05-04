# Write a program to check if a given string is a pangram or not. A pangram is a sentence that contains every letter of the alphabet at least once.

from string import ascii_lowercase

def is_pangram(string):
    alphabet = set(ascii_lowercase)
    return set(string.lower()) >= alphabet

print(is_pangram("The quick brown fox jumps over the lazy dog"))  # Output: True
print(is_pangram("Hello World"))  # Output: False