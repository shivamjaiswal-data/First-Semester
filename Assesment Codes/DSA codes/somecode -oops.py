
from abc import ABC, abstractmethod


# Abstract Base Class
class BankAccount(ABC):

    bank_name = "SBI"

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance  # Encapsulation

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully")
        else:
            print("Invalid amount")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully")
        else:
            print("Insufficient balance or invalid amount")

    def get_balance(self):
        return self.__balance

    @abstractmethod
    def calculate_interest(self):
        pass


# Inheritance
class SavingsAccount(BankAccount):

    def calculate_interest(self):
        interest = self.get_balance() * 0.04
        return interest


class CurrentAccount(BankAccount):

    def calculate_interest(self):
        return 0


# Creating objects
account1 = SavingsAccount("Shivam", 101, 10000)
account2 = CurrentAccount("Rahul", 102, 20000)


# Performing operations
print("Bank:", BankAccount.bank_name)

print("\nAccount Holder:", account1.name)
print("Account Number:", account1.account_number)

account1.deposit(5000)
account1.withdraw(2000)

print("Current Balance:", account1.get_balance())
print("Interest:", account1.calculate_interest())

print("\nCurrent Account:")
print("Holder:", account2.name)
print("Balance:", account2.get_balance())
print("Interest:", account2.calculate_interest())
