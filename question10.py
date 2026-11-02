# Description
# Write a function named move_zeros(numbers) that returns a list where all zeros have been moved to the end while keeping the other numbers in their original order.

# Hints
# First think about what should happen to the non-zero values.
# Keep track of how many zeros you encounter.
# After processing the numbers, how could you add the correct number of zeros?

# Example 1
# Input: [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Example 2
# Input: [1, 2, 3]
# Output: [1, 2, 3]

# Example 3
# Input: [0, 0, 5]
# Output: [5, 0, 0]




def move_zeros(numbers):
    august_alsina = []
    zero_count = 0

    for number in numbers:
        if number == 0:
            zero_count+= 1
        else:
            august_alsina.append(number)
    for _ in range(zero_count):
        august_alsina.append(0)

    return august_alsina

numbers = [0, 1, 0, 3, 12]
# numbers = [0, 0, 5]
print(move_zeros(numbers))