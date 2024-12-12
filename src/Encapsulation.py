class Car:
    def __init__(self, brand, model):
        self.__brand = brand  # Private attribute uses __prefix
        self.__model = model  # Private attribute

    """ 
         However using name mangling
         we can still get access to private fields by 
         object._ClassName.__propertyName
         eg car  = Car('suzuki','800')
         name = car._Car__brand
 """

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


class ElectricCar(Car):
    def __init__(self, brand, model, battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size


myTesla = ElectricCar("Tesla", "Model ", "85K")

print(myTesla.battery_size)
car = Car('ss', 'sss')
var = car._Car__brand
print(var)
