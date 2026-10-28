def find_largest(numbers):
    if not numbers:
        return None


    largest = numbers[0]

    for number in numbers:
        if number > largest:
            largest = number
    
    return largest
numbers = [3, 4, 12, 100, 80, 10]
# numbers = [-10, -5, -2, -18]
print(find_largest(numbers))