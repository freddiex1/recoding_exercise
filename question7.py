# Write a function named reverse_list(items) that returns the elements of a list in reverse order.
# Constraints :
# Do not use reverse().
# Do not use reversed().
# Do not use [::-1].
# Examples
# Example 1
# Input: [1, 2, 3, 4]
# Output: [4, 3, 2, 1]
# Example 2
# Input: ["a", "b", "c"]
# Output: ["c", "b", "a"]
# Hints
# Think about the position of the last element.
# Can you move through the list from the last index toward index 0?
# Add each value you visit to a new list.



def reverse_list(items): 
    lizzy = [] 
    i = len(items) - 1 
    while i >= 0:
        lizzy.append(items[i]) 
        i -= 1 

    return lizzy 
# items = ["a", "b", "c", "d"] 
items = [1, 2, 3, 4]
print(reverse_list(items))
