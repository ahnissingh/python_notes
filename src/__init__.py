class Car:
    brand = None
    model = None

    def __init__(self, brand: str, model):
        self.brand = brand
        self.model = model

    def __str__(self) -> str:
        return f'brand {self.brand} model {self.model}'

    def full_name(self):
        return f'{self.brand},{self.model}'


myCar = Car('suzuki', '800')
print(myCar)
