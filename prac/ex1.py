s = input("Введіть число: ")
try:
    if '.' in s:
        num = float(s)
    else:
        num = int(s)
    result = num * 2
    print("Результат (у вигляді рядка):", str(result))
except ValueError:
    print("Некоректне число.")
