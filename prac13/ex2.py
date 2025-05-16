def analyze_file():
    filename = input("Введіть ім'я файлу для аналізу: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.readlines()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    line_count = len(content)
    word_count = sum(len(line.split()) for line in content)
    char_count = sum(len(line) for line in content)

    print(f"\nАналіз файлу '{filename}':")
    print(f"{'Кількість рядків:':<20} {line_count}")
    print(f"{'Кількість слів:':<20} {word_count}")
    print(f"{'Кількість символів:':<20} {char_count}")


if __name__ == "__main__":
    analyze_file()
