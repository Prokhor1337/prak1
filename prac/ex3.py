s = input("Введіть числа, розділені комами: ")
try:
    parts = s.split(',')
    numbers = []
    for part in parts:
        numbers.append(float(part.strip()))
    total = sum(numbers)
    average = total / len(numbers)
    print("Сума чисел:", total)
    print("Середнє значення:", average)
except ValueError:
    print("Помилка перетворення елементів у числа.")
