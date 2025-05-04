# Object is an instance of a class with its own data.

class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def display_info(self):
        print(f"car make: {self.make}, model: {self.model}, year: {self.year}")


my_car1 = Car("Honda", "city", 2011)
my_car2 = Car("maruti", "alto", 2008)
my_car3 = Car("kia", "seltos", 2014)

my_car1.display_info()
my_car2.display_info()
my_car3.display_info()