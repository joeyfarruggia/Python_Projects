def count_vowels(string):
    vowels = 'aeiou'
    count = 0
    for char in string:
        if char.lower() in vowels:
            count += 1
    return count

input_string = "Hello World"
result = count_vowels(input_string)
print("Number of vowels in the string:", result)  # Output: 3