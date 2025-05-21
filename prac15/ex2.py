class Car:
   def __init__(self, brand, model, year, color):
       self.brand = brand
       self.model = model
       self.year = year
       self.color = color


   def display(self):
       print(f"Марка: {self.brand}, Модель: {self.model}, Рік випуску: {self.year}, Колір: {self.color}")


   def change_color(self, new_color):
       self.color = new_color
       print(f"Колір змінено на {self.color}")




car1 = Car("Toyota", "Corolla", 2020, "червоний")
car1.display()


car1.change_color("синій")
car1.display()
