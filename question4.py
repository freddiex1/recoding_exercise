# Write a function named count_occurrences(numbers, target) that returns how many times target appears in the list.
# Constraints:
# Do not use the built-in count() method.
# Aim for O(n) time complexity.
# hint :Start a counter at 0.
# Check every value in the list.
# Increase the counter whenever the current value equals target.



def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count
numbers = [1, 2, 3, 4, 6]
print(count_even(numbers))