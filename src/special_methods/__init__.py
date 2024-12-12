class Person:
    """
    A class representing a person with a name.

    Attributes:
    name (str): The name of the person.
    """

    def __init__(self, name):
        """
        Initializes a new instance of the Person class.

        Parameters:
        name (str): The name of the person.
        """
        self.name = name

    def __str__(self):
        """
        Returns an informal string representation of the person.

        This method is used by the `str()` function and by `print()` to provide a readable
        description of the object.

        Returns:
        str: A human-readable string describing the person.
        """
        return f"Person named {self.name}"

    def __repr__(self):
        """
        Returns the official string representation of the person.

        This method is used by the `repr()` function and in debugging. It should return a
        string that, when passed to `eval()`, would create an object with the same state.

        Returns:
        str: A string that includes the class name and the name attribute of the person.
        """
        return f"Person(name={self.name!r})"


class PersonList:
    """
    A class representing a list of Person objects.

    Attributes:
    persons (list): A list of Person objects.
    """

    def __init__(self):
        """
        Initializes a new instance of the PersonList class with an empty list.
        """
        self.persons = []

    def add_person(self, person):
        """
        Adds a Person object to the list.

        Parameters:
        person (Person): The Person object to add to the list.
        """
        if isinstance(person, Person):
            self.persons.append(person)
        else:
            raise ValueError("Must be a Person object")

    def __iadd__(self, other):
        """
        Implements the in-place addition operation (+=) to add another PersonList to this one.

        Parameters:
        other (PersonList): Another PersonList object to merge with this one.

        Returns:
        PersonList: The updated PersonList object.
        """
        if isinstance(other, PersonList):
            self.persons.extend(other.persons)
        else:
            raise ValueError("Must be a PersonList object")
        return self

    def __str__(self):
        """
        Returns a string representation of the PersonList.

        Returns:
        str: A string describing the list of persons.
        """
        return ', '.join(str(person) for person in self.persons)


# Example usage
person1 = Person('ahnis')
person2 = Person('ram')
person3 = Person('andy')
person4 = Person('Gobind')

list1 = PersonList()
list1.add_person(person1)
list1.add_person(person2)

list2 = PersonList()
list2.add_person(person3)
list2.add_person(person4)

list1 += list2  # Merging list2 into list1

print(list1)
