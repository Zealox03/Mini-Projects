# This section is talking about class attributes
# Class attributes - attributes specific to a class but not an object or instance of that class

class Person:
    # Define for entire class 
    number_of_people = 0

    def __init__(self,name):
        self.name = name
        Person.number_of_people += 1

p1 = Person("Tim") # This is an instamce of class Person
print(Person.number_of_people)
p2 = Person("Dylan")
print(Person.number_of_people)

#print(p1.number_of_people)
#print(Person.number_of_people)

# Both will return the same output

# Changing the attributes
#Person.number_of_people = 10
#print(p1.number_of_people)
#print(p2.number_of_people)
