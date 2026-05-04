# write a program to revers the words in a given sentence

def reverse_words(sentence):
    words = sentence.split()  # Split the sentence into words
    reversed_words = words[::-1]  # Reverse the list of words
    return ' '.join(reversed_words)  # Join the reversed words back into a sentence

print(reverse_words("Hello World"))  # Output: World Hello