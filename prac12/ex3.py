import random

numbers = [random.randint(1, 100) for _ in range(1000)]

counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1

most_frequent = max(counter, key=counter.get)
count = counter[most_frequent]

print(f"Число, що повторюється найчастіше: {most_frequent}")
print(f"Кількість повторень: {count}")
