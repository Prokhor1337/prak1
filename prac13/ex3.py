def search_and_replace():
    filename = input("Введіть ім'я файлу для пошуку та заміни: ")
    try:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
    except FileNotFoundError:
        print("Файл не знайдено.")
        return

    search_text = input("Введіть слово або фразу для пошуку: ")
    replace_text = input("Введіть слово або фразу для заміни: ")

    new_content = content.replace(search_text, replace_text)

    new_filename = input("Введіть ім'я нового файлу для збереження змін: ")
    with open(new_filename, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"Заміна виконана. Зміни збережено у файл '{new_filename}'.")


if __name__ == "__main__":
    search_and_replace()
