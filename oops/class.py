# Definition: A class is a blueprint for creating objects that encapsulate data and behavior.


class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"Car make: {self.make}, Model: {self.model}, Year: {self.year}")

    def update_year(self, new_year):
        self.year = new_year

        print(f"the year of the car has been update: {self.year}")

my_car = Car("Honda", "city", 2010)

my_car.display_info()
my_car.update_year(2011)
my_car.display_info()

