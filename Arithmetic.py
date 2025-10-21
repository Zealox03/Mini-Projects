#Write a program that prompts the user for two numbers and displays the addition, subtraction, multiplication,
#and division between them.

def addition(x,y):
    return(x + y)
    
def subtraction(x,y):
    return(x - y)
    
def multiplication(x,y):
    return(x * y)
    
def division(x,y):
    return(x / y)

def calculate():
    print("Addition: " + str(addition(x,y)))
    print("Subtraction: " + str(subtraction(x,y)))
    print("Multiplication: " + str(multiplication(x,y)))
    print("Division: " + str(division(x,y)))

x = float(input("Enter the first number: "))
y = float(input("Enter the second number: "))

calculate()

