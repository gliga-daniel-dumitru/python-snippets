class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
        self.__year = 2020  # Private attribute

    def get_year(self):
        return self.__year

my_car = Car("Toyota", "Corolla")
print(my_car.make) 
print(my_car.get_year())  