a = input("Введіть перше число: ")
b = input("Введіть друге число: ")
try:
    x = float(a)
    y = float(b)
    print(f"Сума: {x + y}")
    print(f"Різниця: {x - y}")
    print(f"Добуток: {x * y}")
    if y != 0:
        print(f"Частка: {x / y}")
    else:
        print("Ділення на нуль неможливе.")
except ValueError:
    print("Одне з введених значень не є числом.")
