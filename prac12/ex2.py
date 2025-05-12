grades = {"Іван": 80, "Марія": 95, "Олег": 78, "Анна": 85}

name = input("Введіть імʼя студента: ").strip()

if name in grades:
    print(f"Оцінка студента {name}: {grades[name]}")
else:
    print(f"Студента з іменем {name} не знайдено")
