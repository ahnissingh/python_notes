class InvalidAgeException(Exception):
    def __init__(self, age, message="Age must be greater than 18"):
        self.age = age
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"InvalidAgeException: {self.message} (Provided Age: {self.age})"


def check_age(age):
    if age < 18:
        raise InvalidAgeException(age)


try:
    age_input = int(input("Enter age: "))
    check_age(age_input)
except InvalidAgeException as e:
    print(f"Error: {e}")
