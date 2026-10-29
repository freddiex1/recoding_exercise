# Description :

# Write a function named find_number(numbers, target) that searches for target.
# Return its index if it exists. Return -1 if it does not exist.
# If the target appears more than once, return the index of its first occurrence.

# CONSTRAINTS :
# Do not use index().
# Do not use in.
# Aim for O(n) time complexity.

# HINTS :
# You need both the value and its position while looping.
# Think about range() or enumerate().
# As soon as you find the target, you can return its position.


def find_number(numbers, target):
    for g in range(len(numbers)):
        if numbers[g] == target:
            return g

    return -1

# numbers = [5, 8, 5, 9],
numbers = [10, 25, 30, 45]
target = 30
print(find_number(numbers, target))




# Example 1
# Input: numbers = [10, 25, 30, 45], target = 30
# Output: 2
# Example 2
# Input: numbers = [5, 8, 5, 9], target = 5
# Output: 0
# Example 3
# Input: numbers = [10, 20, 30], target = 99
# Output: -1

    