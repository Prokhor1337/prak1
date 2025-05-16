def simple_text_editor():
    filename = input("Введіть назву нового файлу (з розширенням .txt): ")

    print("Введіть текст (для завершення введення залиште рядок пустим і натисніть Enter):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)

    with open(filename, "w", encoding="utf-8") as f:
        for line in lines:
            f.write(line + "\n")

    print(f"\nФайл '{filename}' успішно створено. Вміст файлу:")

    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        print(content)


if __name__ == "__main__":
    simple_text_editor()
