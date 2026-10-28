# Write a function named list_sum(numbers) that calculates and returns the total of all numbers in a list.

# constrains : 
# Do not use Python's built-in sum() function.
# Return 0 for an empty list.
# Aim for O(n) time complexity.

# hint :
# You need a variable to keep track of the count.
# Remember that % gives you the remainder after division.
# What remainder does an even number have when divided by 2?





def list_sum(numbers):
    total = 0
    for number in numbers:
        total = total + number
    return total

numbers = [2, 4, 6, 8]
print(list_sum(numbers))