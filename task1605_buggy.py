def find_max(numbers):
    max_num = 0
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
    return max_num


def average(numbers):
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)


data = [5, 3, 8, 1]
print("Максимум:", find_max(data))
print("Среднее:", average(data))
print("Максимум отрицательных:", find_max([-5, -3]))
print("Среднее пустого:", average([]))
