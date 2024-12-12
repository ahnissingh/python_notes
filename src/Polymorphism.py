class Car:
    total_car = 0  # static variable

    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute
        self.__model = model  # Private attribute
        Car.total_car += 1

    # Getter method for brand
    def get_brand(self):
        return self.__brand

    # Setter method for brand
    def set_brand(self, brand):
        self.__brand = brand

    # Getter method for model
    def get_model(self):
        return self.__model

    # Setter method for model
    def set_model(self, model):
        self.__model = model

    # Method to display car details (base class)
    def display_info(self):
        return f"Brand: {self.__brand}, Model: {self.__model}"

    @staticmethod
    def general_description(self):
        print('general desc of a car')

    @property
    def model(self):
        # Makes immutable
        return self.__model


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.__battery_size = battery_size  # Private attribute

    # Getter method for battery size
    def get_battery_size(self):
        return self.__battery_size

    # Setter method for battery size
    def set_battery_size(self, battery_size):
        self.__battery_size = battery_size

    # Overridden method to display electric car details (polymorphism)
    def display_info(self):
        # Call the base class's display_info method
        car_info = super().display_info()
        return f"{car_info}, Battery Size: {self.__battery_size}"


# Creating objects of Car and ElectricCar
car = Car("Toyota", "Camry")
electric_car = ElectricCar("Tesla", "Model S", "100K")

# Using polymorphism to call display_info on both objects
print(car.display_info())  # Calls the Car's display_info
print(electric_car.display_info())  # Calls the ElectricCar's overridden display_info

"""
Multiple Inheritance
"""


class Battery:
    def battery_info(self):
        return 'this is battery'


class Engine:
    def engine_info(self):
        return 'this is engine'


class ElectricCar2(Battery, Engine, Car):
    pass


my_tesla = ElectricCar2('Tesla', "Model", "s")
