import json
import os

FILENAME = "clients.json"

def load_clients():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_clients(clients):
    with open(FILENAME, "w", encoding="utf-8") as f:
        json.dump(clients, f, indent=4)

def add_client(clients):
    name = input("Ім'я: ")
    email = input("Email: ")
    phone = input("Телефон: ")
    clients.append({"name": name, "email": email, "phone": phone})
    print("Клієнт доданий.")

def search_client(clients):
    query = input("Пошук за ім’ям або email: ")
    results = [c for c in clients if query.lower() in c["name"].lower() or query.lower() in c["email"].lower()]
    if results:
        for c in results:
            print(c)
    else:
        print("Нічого не знайдено.")

def update_client(clients):
    email = input("Email для оновлення: ")
    for client in clients:
        if client["email"] == email:
            client["name"] = input("Нове ім’я: ")
            client["phone"] = input("Новий телефон: ")
            print("Оновлено.")
            return
    print("Клієнта не знайдено.")

def delete_client(clients):
    email = input("Email для видалення: ")
    before = len(clients)
    clients[:] = [c for c in clients if c["email"] != email]
    if len(clients) < before:
        print("Видалено.")
    else:
        print("Клієнта не знайдено.")

def main():
    clients = load_clients()
    while True:
        print("\n1. Додати")
        print("2. Пошук")
        print("3. Оновити")
        print("4. Видалити")
        print("5. Вихід")
        choice = input("Оберіть дію: ")
        if choice == "1":
            add_client(clients)
        elif choice == "2":
            search_client(clients)
        elif choice == "3":
            update_client(clients)
        elif choice == "4":
            delete_client(clients)
        elif choice == "5":
            save_clients(clients)
            break
        else:
            print("Невірна дія.")

if __name__ == "__main__":
    main()
