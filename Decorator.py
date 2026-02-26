# Decorator = A function that extends the behavior of another functiom
#             Without modifying the base function
#             Pass the base function as an argument to the decorator

#For example, some people wants sprinkles on their ice cream
#You can add @add_sprinkles to get_ice_cream("Vanilla")

# Basic formula to apply a decorator
def add_sprinkles(func):
    def wrapper(*args, **kwargs):
        print("**You add sprinkles✨**")
        func(*args, **kwargs)
    return wrapper

def add_fudge(func):
    def wrapper(*args, **kwargs):
        print("** You added fudge 🍫**")
        func(*args, **kwargs)
    return wrapper

@add_sprinkles
@add_fudge
# Below is a base function
def get_ice_cream(flavor):
    print(f"Here is your {flavor} ice cream 🍦")

get_ice_cream("Vanilla")

# TypeError: add_sprinkles.<locals>.wrapper() takes 0 positional arguments but 1 was given
# Error happens because we send 1 argument to our wrapper. Our wrapper was not set to accept any parameter
# Fix: Define wrapper(*args, **kwargs) to accept any number of arguments and any keywords of arguments