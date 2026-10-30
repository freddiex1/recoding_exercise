def has_duplicates(numbers):
    jay = set()
    for number in numbers:
        if number in jay:
            return True

        jay.add(number)

    return False

numbers = [1, 2, 3, 9, 5, 0, 9]
print(has_duplicates(numbers))