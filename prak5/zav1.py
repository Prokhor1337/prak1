temp = int(input("Введіть градуси Цельсія від 1 до 100:"))
wat = int(input("Введіть % вологості від 1 до 100:"))

if temp >= 30 and wat >= 70:
    print("Активація системи охолодження")
else:
    print("Умови нормальні")
