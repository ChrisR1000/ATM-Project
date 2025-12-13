


#Account Class for atm project
class Account:
    def __init__(self, client_name, account_number, pin, balance=0.0):
        self.client_name = client_name
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
    
    def create_account(self):
        new_account = self.account_number

