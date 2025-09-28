from bank_account import *

Deng = BankAccount(1000, "Perminus")
Sara = BankAccount(2000, "Sara")

Deng.getBalance()
Sara.getBalance()

Sara.deposit(500)

Deng.withdraw(10000)
Deng.withdraw(10)

Deng.transfer(10000, Sara)
Deng.transfer(100, Sara)

Jim = InterestRewardAcct(1000, "Jim")

Jim.getBalance()

Jim.deposit(100)

Jim.transfer(100, Deng)

Blaze = SavingsAcct(1000, "Blaze")

Blaze.getBalance()

Blaze.deposit(100)

Blaze.transfer(10000, Sara)
Blaze.transfer(1000, Sara)