class Car:
    brand = None
    model = None

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


myTesla = ElectricCar("Tesla", "Model ", "85K")

print(myTesla.battery_size)
