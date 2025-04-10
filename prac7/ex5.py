start_bacteria = 10
growth_rate = float(input("Введіть відсоток зростання за годину (наприклад, 20): "))
max_population = int(input("Введіть максимальну кількість бактерій: "))

population = start_bacteria
hours = 0

while population < max_population:
    print(f"Година {hours}: {int(population)} бактерій")
    population += population * (growth_rate / 100)
    hours += 1

print(f"Година {hours}: {int(population)} бактерій")
print(f"Потрібно годин: {hours}")
