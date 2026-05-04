# sort a list of strings based on their lengths from shortest to longest
def sort_by_length(strings):
    return sorted(strings, key=len)

print(sort_by_length(["apple", "banana", "kiwi", "grapefruit"]))  # Output: ['kiwi', 'apple', 'banana', 'grapefruit']