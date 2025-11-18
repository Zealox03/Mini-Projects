# Create a BankAccount class with methods deposit() and withdraw(). 
# Then, create a SavingsAccount class that inherits from BankAccount 
# and overrides the withdraw() method to prevent withdrawals that would cause the balance to fall below $100. 

class BankAccount:
    def __init__(self,name,initial_balance=0):
        self.name = name
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance > amount:
            self.balance -= amount
        else:
            print("Insufficient amount")
    
    def show(self):
        print(f"Username: {self.name}")
        print(f"Balance: {self.balance}")
    
class SavingsAccount(BankAccount):
    def __init__(self,name,initial_balance):
        super().__init__(name,initial_balance)
    
    def withdraw(self,amount):
        if self.balance - amount >= 100:
            self.balance -= amount
        else:
            print(f"Balance must not fall below $100")

dylan_cimb = SavingsAccount("Dylan",100)
dylan_cimb.deposit(500)
dylan_cimb.withdraw(750)
dylan_cimb.show()