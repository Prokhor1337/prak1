products = [
    ("Хліб", 25.5, 3),
    ("Молоко", 32.75, 2),
    ("Яйця", 60, 1),
    ("Сир", 120.99, 5)
]

header = "{:<20} {:>10} {:^8}".format("Назва товару", "Ціна", "К-сть")
print(header)
print("-" * 40)

for name, price, quantity in products:
    row = "{:<20} {:>10.2f} {:^8}".format(name, price, quantity)
    print(row)
