import json
import os

FILENAME = "contacts.json"

def load_contacts():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return {}

def save_contacts(contacts):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Ім'я: ")
    phone = input("Телефон: ")
    contacts[name] = phone
    print("Контакт додано.")

def show_contacts(contacts):
    if not contacts:
        print("Список порожній.")
    else:
        for name, phone in contacts.items():
            print(f"{name}: {phone}")

def main():
    contacts = load_contacts()
    while True:
        print("\n1. Додати контакт")
        print("2. Показати всі контакти")
        print("3. Вихід")
        choice = input("Оберіть дію: ")
        if choice == "1":
            add_contact(contacts)
            save_contacts(contacts)
        elif choice == "2":
            show_contacts(contacts)
        elif choice == "3":
            save_contacts(contacts)
            break
        else:
            print("Невірний вибір.")

if __name__ == "__main__":
    main()
