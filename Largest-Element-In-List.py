def find_largest(numbers):
    largest = numbers[0]  # Assume the first number is the largest
    for num in numbers:
        if num > largest:
            largest = num  # Update largest if current number is greater
    return largest

print(find_largest([10, 5, 8, 15, 3, 9]))  # Output: 15