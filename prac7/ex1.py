deposit = float(input("Введіть початкову суму вкладу: "))
rate = float(input("Введіть процентну ставку (%): "))
target = float(input("Введіть бажану суму: "))

years = 0

while deposit < target:
    deposit += deposit * (rate / 100)
    years += 1
    print(f"Рік {years}: {deposit:.2f} грн")

print(f"Потрібно років: {years}")
