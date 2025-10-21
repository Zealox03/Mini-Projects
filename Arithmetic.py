#Write a program that prompts the user for two numbers and displays the addition, subtraction, multiplication,
#and division between them.

def addition(x,y):
    print(x + y)
    
def subtraction(x,y):
    print(x - y)
    
def multiplication(x,y):
    print(x * y)
    
def division(x,y):
    print(x / y)

def calculate():
    addition(x,y)
    subtraction(x,y)
    multiplication(x,y)
    division(x,y)

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

calculate()

