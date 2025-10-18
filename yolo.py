class Dog:
    def __init__(self,name,breed):
        self.name = name
        self.breed = breed

    def Bark(self):
        print("Woof")

Loki = Dog("Loki","Stray")
Koli = Dog("Koli","Poodle")

Loki.Bark()
Koli.Bark()