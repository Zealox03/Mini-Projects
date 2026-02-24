# This section is about class methods

class Person:
    number_of_people = 0
    Gravity = -9.8

    def __init__(self, name):
        self.name = name
        Person.add_person()

    @classmethod # This is to denote / decorator for class methods
    def number_of_people_(cls): # cls stands for class, you are not returning an instance # Method name should not share name as attribute
        return cls.number_of_people

    @classmethod
    def add_person(cls):
        cls.number_of_people += 1

p1 = Person("Tim")
p2 = Person("Jill")
print(Person.number_of_people_())
