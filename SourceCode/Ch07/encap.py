class BankAccount:
    def __init__(self, account_number, balance):
        self._account_number = account_number  # Protected attribute
        self.__balance = balance               # Private attribute
    
    def get_account_number(self):              # getter
        return self._account_number
    
    def get_balance(self):                     # getter
        return self.__balance
    
    def deposit(self, amount):                 # setter
        if amount > 0:
            self.__balance += amount
    
    def withdraw(self, amount):                # setter
        if amount > 0 and amount <= self.__balance:
            self.__balance -= amount



account = BankAccount("1234567890", 1000)
print(account.get_account_number())  # Accessing protected attribute
print(account.get_balance())         # Accessing private attribute


account.deposit(500)                 # Modifying private attribute through setter method
print(account.get_balance())


account.withdraw(200)                # Modifying private attribute through setter method
print(account.get_balance())
