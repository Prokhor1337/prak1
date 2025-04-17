composite_numbers = [
    num for num in range(2, 101)
    if len([div for div in range(1, num + 1) if num % div == 0]) > 2
]
print("Складні числа від 1 до 100:", composite_numbers)
