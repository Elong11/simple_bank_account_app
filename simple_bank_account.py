class Account():
    def __init__(self,owner,balance):
        
        self.owner = owner
        self.balance = balance

    # Deposit Cash
    def deposit_cash(self,amount):
        self.balance = self.balance + amount

    # Withdraw Cash not to exceed balance
    def withdraw_cash(self,amount):
        if self.balance < amount:
            print('You are not allowed to overdraft this account of balance : ' + str(self.balance))
        
        self.balance = self.balance = amount    


account_1 = Account('Evan', 10000000)
# grabs the balance
account_1.balance
# Deposit Cash
account_1.deposit_cash(5000)
# Withdraw Cash not to exceed balance
account_1.withdraw_cash(20)
# Withdraw Cash exceeded the balance
account_1.withdraw_cash(9999999)

acct2 = Account('Suraj',4500)
acct2.deposit_cash(1000)
acct2.balance
