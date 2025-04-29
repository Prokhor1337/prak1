s = input("Введіть число з плаваючою точкою: ")
try:
    number = float(s)
    formatted = f"{number:.2f}"
    print("Форматоване число (2 знаки після крапки):", formatted)
except ValueError:
    print("Це не число.")
