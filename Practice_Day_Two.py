# Create a BankAccount class with methods deposit() and withdraw(). 
# Then, create a SavingsAccount class that inherits from BankAccount 
# and overrides the withdraw() method to prevent withdrawals that would cause the balance to fall below $100. 

class BankAccount:
    def __init__(self,initial_balance = 0):
        self.balance = initial_balance

    def deposit(self,amount):
        self.balance += amount
    
    def withdraw(self,amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficient amount")

    def show(self):
        print(f"Remaining balance: {self.balance}") 

class SavingsAccount(BankAccount):
    def withdraw(self,amount):
        super().__init__(self,initial_balance=0)

    def withdraw(self,amount):
        if self.balance - amount >= 100:
            self.balance -= amount
        else:
            print("Insuffecient balance")

cimb_1 = SavingsAccount(100)
cimb_1.show()
cimb_1.deposit(100)
cimb_1.show()
cimb_1.withdraw(50)
cimb_1.show()