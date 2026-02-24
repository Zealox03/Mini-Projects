# Consider a Python class Product designed to represent items in an inventory. 
# This class should have a class attribute total_products_created that keeps track of the total number of Product instances ever created. 
# Additionally, it should have a class method get_total_products() that returns the value of total_products_created. 
# Each Product instance should also have instance attributes for name and price.

class Product:

    total_products_created = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        Product.add_product_()
        
    @classmethod
    def total_products_created_(cls):
        return cls.total_products_created
    
    @classmethod
    def add_product_(cls):
        cls.total_products_created += 1

p1 = Product("Milo",10)
print(Product.total_products_created_())
p2 = Product("Nestum",15)
print(Product.total_products_created_())

