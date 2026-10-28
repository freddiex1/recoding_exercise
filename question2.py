# write a function named find_smallest(numbers) that returns the smallest nimbers in a list
# constrains 
# do not use min(), max() and return None if list is empty
# hints : start by remembring one number from the list, visit every number, ask is this number smalller than the smallest one i have seeen? 

def find_smallest(numbers):
    if not numbers:
        return None


    smallest = numbers[0]

    for number in numbers:
        if number < smallest:
            smallest = number

    return smallest
numbers = [8, 3, 12, 1, 7] 
print(find_smallest(numbers))