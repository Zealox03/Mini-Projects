class Math: 
    @staticmethod # Methods that cannot be changed # They do something but does not change anything
    def add5(x):
        return x + 5
    
    @staticmethod
    def add10(x):
        return x + 5
    
print(Math.add5(5))
print(Math.add10(10))