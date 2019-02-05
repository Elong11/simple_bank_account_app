class Account():
    def __init__(self, owner, balance=0):
        
        self.owner = owner
        self.balance = balance

    # Deposit Cash
    def deposit_cash(self, amount):
        self.balance = self.balance + amount
        print(f'{self.owner}, ${amount} has been added to your account balance.')

    # Withdraw Cash not to exceed balance
    def withdraw_cash(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
        else:
            print('You are not allowed to overdraft this account of balance : ' + str(self.balance))

    def __str__(self):
        return f'Owner: {self.owner} \n Balance: $ {self.balance}'


account_1 = Account('Evan', 10000000)
# grabs the balance
account_1.balance
# Deposit Cash
account_1.deposit_cash(5000)
# Withdraw Cash not to exceed balance
account_1.withdraw_cash(20)
# Withdraw Cash exceeded the balance
account_1.withdraw_cash(9999999)

account_2 = Account('Suraj', 4500)
account_2.deposit_cash(1000)
account_2.balance
