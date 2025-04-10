start = int(input("Введіть нижню межу діапазону: "))
end = int(input("Введіть верхню межу діапазону: "))

found = False

print("Прості числа:")
for num in range(start, end + 1):
    if num < 2:
        continue
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            break
    else:
        print(num, end=' ')
        found = True

if not found:
    print("Простих чисел у цьому діапазоні немає.")
