while True:
    try:
        n = int(input("Введіть ціле невід’ємне число: "))
        if n < 0:
            print("Число повинно бути не менше 0.")
            continue
        break
    except ValueError:
        print("Це не ціле число!")

factorial = 1
i = 1
steps = ""

while i <= n:
    factorial *= i
    steps += f"{i}*"
    i += 1

steps = steps.rstrip("*")
print(f"{n}! = {steps} = {factorial}")
