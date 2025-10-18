# Basic Concepts: Classes and Objects
# Create a Dog Class:
# Define a class named Dog with attributes like name and breed.
# Include an __init__ method to initialize these attributes.
# Add a method called bark() that prints a message like "Woof! My name is \[dog's name]".
# Instantiate and Interact:
# Create two Dog objects with different names and breeds.
# Call the bark() method for each dog.

class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print("Woof! My name is " + self.name)

Loki = Dog("Loki","Pitbull")
Poppy = Dog("Poppy", "Chihuahua")

Loki.bark()
Poppy.bark()