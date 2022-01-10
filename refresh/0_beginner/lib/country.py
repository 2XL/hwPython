"""
Model for country
"""
from faker import Faker


class Country:
    """
    Convention use _[varname]
    Avoid naming collision/clash.

    In python everything is PUBLIC
    (public, private, protected)???

    class invariants, truths about an object that endure for its lifetime.

    """

    def __init__(self, name):
        self._name = name
        self._people = []
        pass

    def country_code(self):
        return self._name[0:3]

    def phone_prefix(self):
        return sum([ord(x) for x in self._name])

    def register_citizenship(self, person):
        self._people.append(person)

    def population(self):
        return len(self._people)

    pass


def make_country(num_people):
    faker = Faker()

    faker.name()
    spain = Country("SPAIN")

    [spain.register_citizenship(faker.name()) for _ in range(num_people)]
    # spain.register_citizenship("Manolo")
    # spain.register_citizenship("张国为")

    return spain
    pass


def make_passport():
    pass


def make_citizen():
    pass
