def process_data(data, operation, dict_mode="values"):
    try:
        if not callable(operation):
            return "Помилка: operation не є функцією"
        if isinstance(data, list):
            return [operation(x) for x in data]
        elif isinstance(data, tuple):
            return tuple(operation(x) for x in data)
        elif isinstance(data, dict):
            if dict_mode == "keys":
                return {operation(k): v for k, v in data.items()}
            elif dict_mode == "values":
                return {k: operation(v) for k, v in data.items()}
            elif dict_mode == "both":
                return {operation(k): operation(v) for k, v in data.items()}
            else:
                return "Помилка: Невідомий режим dict_mode"
        else:
            return "Помилка: Тип колекції не підтримується"
    except Exception as e:
        return f"Помилка обробки: {e}"


def filter_data(data, predicate):
    try:
        if not callable(predicate):
            return "Помилка: predicate не є функцією"
        if isinstance(data, list):
            return [x for x in data if predicate(x)]
        elif isinstance(data, tuple):
            return tuple(x for x in data if predicate(x))
        elif isinstance(data, dict):
            return {k: v for k, v in data.items() if predicate((k, v))}
        else:
            return "Помилка: Тип колекції не підтримується"
    except Exception as e:
        return f"Помилка фільтрації: {e}"


def combine_values(*args, separator="", initial=None):
    try:
        if not args:
            return "Помилка: немає аргументів"
        first = args[0]
        if isinstance(first, str):
            return separator.join(str(x) for x in args)
        elif isinstance(first, (int, float)):
            total = initial if initial is not None else 0
            for x in args:
                if not isinstance(x, (int, float)):
                    raise TypeError("Усі аргументи повинні бути числовими")
                total += x
            return total
        else:
            return "Помилка: підтримуються лише рядки та числа"
    except Exception as e:
        return f"Помилка об'єднання: {e}"

print(process_data([1, 2, 3], lambda x: x * 2))
print(process_data((4, 5, 6), lambda x: x + 1))
print(process_data({"a": 1, "b": 2}, lambda x: x * 10, dict_mode="values"))
print(process_data({"a": 1, "b": 2}, lambda x: x.upper(), dict_mode="keys"))

print(filter_data([1, 2, 3, 4], lambda x: x % 2 == 0))
print(filter_data((5, 6, 7, 8), lambda x: x > 6))
print(filter_data({"a": 1, "b": 2}, lambda x: x[1] > 1))

print(combine_values(1, 2, 3, initial=10))
print(combine_values("a", "b", "c", separator="-"))
