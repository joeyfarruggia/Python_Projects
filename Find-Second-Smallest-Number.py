# write a program to find the second smallest element in a list
def find_second_smallest(numbers):
    sorted_nums = sorted(set(numbers))  # Remove duplicates and sort the list
    return sorted_nums[1]

# Example usage
print (find_second_smallest([3, 1, 4, 1, 5, 9]))  # Output: 3
