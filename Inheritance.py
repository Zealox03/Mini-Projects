# Generalization
class Pet:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old")

    def speak(self):
        print("I don't know what to say")

# Specific class inherit from generalized class
class Cat(Pet):
    def __init__(self,name,age,color):
        super().__init__(name,age)
        self.color = color

    def speak(self):
        print("Meow")

    def show(self):
        print(f"I am {self.name} and I am {self.age} years old and I am {self.color}")

# Specific class inherit from generalized class
class Dog(Pet):
    def speak(self):
        print("Bark")

# The whole point of inheritance is to avoid redundancy

p = Pet("Tim",19)
p.show()
p.speak()
c = Cat("Mia",7,"Black")
c.show()
c.speak()
d = Dog("Loki",20)
d.show()
d.speak()