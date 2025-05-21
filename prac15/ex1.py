class Person:
   def __init__(self, name, age, city):
       self.name = name
       self.age = age
       self.city = city


   def display(self):
       print(f"Ім'я: {self.name}, Вік: {self.age}, Місто проживання: {self.city}")


person1 = Person("Макс", 25, "Київ")
person1.display()
