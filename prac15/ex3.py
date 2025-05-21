class BankAccount:
   def __init__(self, owner, account_number, balance=0):
       self.owner = owner
       self.account_number = account_number
       self.balance = balance


   def deposit(self, amount):
       if amount > 0:
           self.balance += amount
           print(f"Поповнено на {amount} грн. Баланс: {self.balance} грн.")
       else:
           print("Сума поповнення має бути більшою за 0.")


   def withdraw(self, amount):
       try:
           if amount <= 0:
               raise ValueError("Сума зняття має бути більшою за 0.")
           if amount > self.balance:
               raise ValueError("Недостатньо коштів на рахунку.")
           self.balance -= amount
           print(f"Знято {amount} грн. Поточний баланс: {self.balance} грн.")
       except ValueError as e:
           print(f"Помилка: {e}")


   def check_balance(self):
       print(f"Поточний баланс: {self.balance} грн.")


account1 = BankAccount("Макс Кідрук", "1234567890", 1000)
account1.check_balance()


account1.deposit(500)
account1.withdraw(200)
account1.withdraw(2000)
