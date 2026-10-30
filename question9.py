# Write a function named first_duplicate(numbers) that returns the first number that appears more than once while moving from left to right.
# Return None if there are no duplicates.
# Example 1
# Input: [4, 7, 2, 7, 5, 4]
# Output: 7

# Example 2
# Input: [1, 2, 3, 4]
# Output: None

# Example 3
# Input: [5, 5, 3]
# Output: 5

# Hints :
# Keep track of values you have already visited.
# For every new number, check whether it has already been seen.
# You can return immediately when you discover the first repeated value.



def first_duplicate(numbers):
    jay = set()

    for number in numbers:
        if number in jay:
            return number

        jay.add(number)
    return None

numbers = [4, 7, 2, 7, 5, 4]
# numbers = [1, 2, 3, 4]
print(first_duplicate(numbers))