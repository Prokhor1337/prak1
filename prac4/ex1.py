name = input("Введіть ім'я: ")
surname = input("Введіть прізвище: ")
city = input("Введіть місто: ")

try:
    age = float(input("Введіть вік: "))
    print(f"Ім'я: {name:<10} Прізвище: {surname} Вік: {age:.2f} Місто: {city:>15}")
except ValueError:
    print("Помилка: вік має бути числом.")
