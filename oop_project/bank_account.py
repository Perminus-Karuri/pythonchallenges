class BalanceException(Exception):  # handles exceprions raised
    pass

class BankAccount:
    def __init__(self, initialAmount, accName):  # properties of the class bank account
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):  # method to get balance in the bank account
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):  # method to deposit cash in tha acc
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount):  # checks if transaction should proceed only if account has required balance to complete transaction
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):  # allows user to withdraw cash and also raises an exception if amount is not enough to withdraw
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):  # method to transfer cash to another account and raise an exception if amount is not enough to complete transfer
        try:
            print("\n**********\n\nBeginning a transaction...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardAcct(BankAccount):  # class inherits from BankAccount
    def deposit(self, amount): # override method to accrue interest when user deposits cash into this account
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):  # class inherits from InterestRewardAcct
    def __init__(self, initialAmount, accName):  # properties of the class SavingsAcct
        super().__init__(initialAmount, accName) # inherits from parent BankAccount
        self.fee = 5

    def withdraw(self, amount):  # method to withdraw cash from the SavingsAcct
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
