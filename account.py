#Account Class for atm project
class Account:
    def __init__(self, account_name, account_number, pin, balance=0.0):
        self.account_name = account_name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    @classmethod
    def create_account(self, name, pin):
       name = input("Enter the name for new bank account: ")
       self.account_name = name
       pin = input("Enter pin for new account: ")
       self.pin = pin 

    def deposit(self, amount):
        if amount >= 0:
            self.balance += amount
            print(f"${amount} has been deposited successfully. Your new balance is {self.balance}.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount): 
        if amount >= 0:
            self.balance -= amount
            print(f"{amount} has been withdrawn from your account. Your balance is now{self.balance}.")
        else:
            print("Invalid amount.")
    
    #Update to ATM Project

