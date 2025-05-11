shopping_list = ["молоко", "хліб", "масло", "яйця", "сир", "яблука"]
long_items = [item for item in shopping_list if len(item) > 4]
print("Товари з назвою понад 4 символи:", long_items)
print("Кількість таких товарів:", len(long_items))
