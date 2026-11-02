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