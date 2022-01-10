"""
Approach to oop design can reduce coupling
"""


def classes():
    """
    What is a class?
    relatives
    new class instance
    methods
    self args
    initializers
    collaborate
    implementation, interface, combine class
    """
    from lib.country import Country, make_country

    spain = make_country(5)

    print(spain.country_code())
    print(spain.phone_prefix())
    print(spain.population())

    pass


def polymorphism():
    """
    Using objects of different types through a uniform interface
    It applies to both functions as well as more complex types.

    Duck typing, when I see a duck that taks like a person and swims like a fish i call it human fish duck
    An object's fitness for use is only determined at use.
    """


def inheritance():
    """
    1. nominally-typed languages use inheritance for polymorphism
    2. python use late binding

    inheritance in python is primarily useful for sharing implementation between classes.
    """
    from datetime import time, datetime, date
    class MetaEntity:
        def __init__(self, name):
            self._name = name
            self._birthday = datetime.now()
            pass

        def __str__(self):
            return self._name

        def whoami(self):
            return self._name

    class Robot(MetaEntity):
        serial_number = 0

        def __init__(self):
            Robot.serial_number += 1
            super().__init__(name="Robot: #{}".format(Robot.serial_number))
            pass

        pass

    class Human(MetaEntity):
        pass

    class Animal(MetaEntity):
        pass

    one = Robot()
    two = Human(name="Joe")
    three = Animal(name="Cat")
    print(one, two, three)


if __name__ == '__main__':
    classes()
    inheritance()
    pass
