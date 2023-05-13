#3
class Car:
    def __init__(self, brand, model, year):
        self.brand = brand
        self.model = model
        self.year = year

    def info(self):
        print(f"Марка {self.brand}, Модель {self.model}, Рік  {self.year}")
car1 = Car("Porshe", "Taycan", 2021)
car1.info()
car2 = Car("Maclaren", "P1", 2023)
car2.info()
