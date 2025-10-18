# KEY NOTES
# self is passed as the first argument to every method of a class / This instance of a class


# This a class for Dog which also acts like a blueprint
class Dog:

    # A special method that is called the moment you created an object
    # It initialize an object 
    def __init__(self):
        pass

    # A method goes into a class
    def bark(self):
        print("bark")

    def add_one(self, x):
        return x + 1

d = Dog() # Assign d to an instance of class Dog 
d.bark() # d can call functions from Dog because it's an instance of Dog

print(d.add_one(5))
# 6
print(type(d))

#Expected output: <class '__main__.Dog'>


class Cat:
    def __init__(self,name,age):
        self.name = name
        self.age = age
        #print(name)

    def get_name(self):
        return self.name
    
    def get_age(self):
        return self.age

# Different name, different instances
Mia = Cat("Mia",7)
#print(Mia.name)
print(Mia.get_name())
print(Mia.get_age())


Buncit = Cat("Buncit",10)
#print(Buncit.name)
print(Buncit.get_name())
print(Buncit.get_age())