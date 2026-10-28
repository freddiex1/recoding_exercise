# Count Occurrences :
# Description:
# Write a function named count_occurrences(numbers, target) that returns how many times target appears in the list.
# Constraints :
# Do not use the built-in count() method.
# Aim for O(n) time complexity.


# Input: numbers = [2, 5, 2, 8, 2], target = 2
# Output: 3

# Input: numbers = [1, 4, 7], target = 10
# Output: 0

# Hints :
# Start a counter at 0.
# Check every value in the list.
# Increase the counter whenever the current value equals target.



def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count = count + 1


    return count
numbers = [2, 5, 2, 8, 2]

target = 2
print(count_occurrences(numbers, target))


