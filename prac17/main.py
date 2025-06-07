from datetime import date
from calendar_tools import UkrainianCalendar
from math_utils import Calculator
from text_analysis import TextStats

# --- Завдання 1 ---
print("=== Модуль обробки дат ===")
calendar = UkrainianCalendar()
today = date.today()
print("Список свят:", calendar.get_holiday_list())
print("Чи сьогодні робочий день:", calendar.is_working_day(today))

# --- Завдання 2 ---
print("\n=== Модуль калькулятора ===")
calc = Calculator()
a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
operation = input("Оберіть операцію (+, -, *, /): ")

if operation == "+":
    print("Результат:", calc.add(a, b))
elif operation == "-":
    print("Результат:", calc.subtract(a, b))
elif operation == "*":
    print("Результат:", calc.multiply(a, b))
elif operation == "/":
    print("Результат:", calc.divide(a, b))
else:
    print("Невідома операція")

# --- Завдання 3 ---
print("\n=== Модуль аналізу тексту ===")
user_text = input("Введіть текст для аналізу: ")
analyzer = TextStats(user_text)
print("Кількість слів:", analyzer.count_words())
common = analyzer.most_common_letter()
if common:
    print(f"Найчастіша літера: '{common[0]}' ({common[1]} разів)")
else:
    print("Немає літер для аналізу")
