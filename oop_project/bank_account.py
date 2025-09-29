class BalanceException(Exception):  # custom exception class for insufficient balance errors
    pass

class BankAccount:
    def __init__(self, initialAmount, accName): # constructor method to initialize a bank account with a balance and account name
        self.balance = initialAmount
        self.name = accName
        print(f"\nAccount '{self.name}' created.\nBalance = ${self.balance:.2f}")

    def getBalance(self):  
        # method to display current balance in the bank account
        print(f"\nAccount '{self.name}' balance = ${self.balance:.2f}")
    
    def deposit(self, amount):  
        # method to deposit cash in tha acc
        self.balance = self.balance + amount
        print("\nDeposit complete.")
        self.getBalance()
    
    def viableTransaction(self, amount): 
        # checks if there are sufficient funds in the account before proceeding with a transaction
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"\nSorry, account '{self.name}' only has a balance of ${self.balance:.2f}")
        
    def withdraw(self, amount):  
        # allows user to withdraw cash and also raises an exception if balance is insufficient
        try:
            self.viableTransaction(amount)
            self.balance = self.balance - amount
            print("\nWithdraw complete")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")

    def transfer(self, amount, account):  # method to transfer cash to another account and raises an exception if balance is insufficient
        try:
            print("\n**********\n\nBeginning a transaction...🚀")
            self.viableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print("\nTransfer complete!✅\n\n**********")
        except BalanceException as error:
            print(f"\nTransfer interrupted. ❌ {error}")

class InterestRewardAcct(BankAccount):  # child class that inherits from BankAccount
    def deposit(self, amount): # overridden deposit method to add a 5% interest bonus to each deposit
        self.balance = self.balance + (amount * 1.05)
        print("\nDeposit complete.")
        self.getBalance()

class SavingsAcct(InterestRewardAcct):   # child class that inherits from InterestRewardAcct
    def __init__(self, initialAmount, accName):  # constructor method that initializes a SavingsAcct and adds a fixed withdrawal fee
        super().__init__(initialAmount, accName) # calls the parent constructor to set up the account
        self.fee = 5

    def withdraw(self, amount):   # overridden withdraw method that deducts a $5 fee for every withdrawal
        try:
            self.viableTransaction(amount + self.fee)
            self.balance = self.balance - (amount + self.fee)
            print("\nWithdraw complete.")
            self.getBalance()
        except BalanceException as error:
            print(f"\nWithdraw interrupted: {error}")
