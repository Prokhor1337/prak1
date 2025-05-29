from abc import ABC, abstractmethod

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class BookManager:
    def __init__(self):
        self.books = []

    def add(self, title, author):
        book = Book(title, author)
        self.books.append(book)

    def update(self, index, title, author):
        self.books[index].title = title
        self.books[index].author = author

    def display_all(self):
        return [f"{i + 1}. {b.title} - {b.author}" for i, b in enumerate(self.books)]

class PaymentMethod(ABC):
    @abstractmethod
    def pay(self, amount):
        pass

class CreditCard(PaymentMethod):
    def pay(self, amount):
        return f"Оплата {amount} грн кредитною карткою"

class PayPal(PaymentMethod):
    def pay(self, amount):
        return f"Оплата {amount} грн через PayPal"

class Crypto(PaymentMethod):
    def pay(self, amount):
        return f"Оплата {amount} грн криптовалютою"

class PaymentProcessor:
    def process(self, method: PaymentMethod, amount):
        return method.pay(amount)

class Notifier(ABC):
    @abstractmethod
    def notify(self, message):
        pass

class Email(Notifier):
    def notify(self, message):
        return f"Email: {message}"

class SMS(Notifier):
    def notify(self, message):
        return f"SMS: {message}"

class Push(Notifier):
    def notify(self, message):
        return f"Push: {message}"

class NotificationService:
    def __init__(self, notifiers):
        self.notifiers = notifiers

    def send(self, message):
        return [n.notify(message) for n in self.notifiers]

def main():
    books = BookManager()
    notifier = NotificationService([Email(), SMS(), Push()])
    payments = PaymentProcessor()

    while True:
        print("\nПанель керування:")
        print("1. Додати книгу")
        print("2. Оновити книгу")
        print("3. Показати книги")
        print("4. Оплата")
        print("5. Надіслати повідомлення")
        print("0. Вихід")
        choice = input("Оберіть опцію: ")

        if choice == "1":
            t = input("Назва: ")
            a = input("Автор: ")
            books.add(t, a)
            print("Книгу додано.")

        elif choice == "2":
            for line in books.display_all():
                print(line)
            idx = int(input("Номер книги: ")) - 1
            t = input("Нова назва: ")
            a = input("Новий автор: ")
            books.update(idx, t, a)
            print("Оновлено.")

        elif choice == "3":
            for line in books.display_all():
                print(line)

        elif choice == "4":
            print("1. Кредитна картка")
            print("2. PayPal")
            print("3. Криптовалюта")
            m = input("Метод: ")
            s = float(input("Сума: "))
            method = {"1": CreditCard(), "2": PayPal(), "3": Crypto()}.get(m)
            if method:
                print(payments.process(method, s))
            else:
                print("Невірний метод.")

        elif choice == "5":
            msg = input("Текст повідомлення: ")
            for line in notifier.send(msg):
                print(line)

        elif choice == "0":
            break

        else:
            print("Невірна опція")

if __name__ == "__main__":
    main()
