import math 
class Account:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, summa):
        print("Your balance:", self.balance)
        if summa >= 0:
            self.balance += summa
            print("Your Balance:", self.balance)
        else:
            print("Rewrite input")

    def withdraw(self, summa):
        print("Your balance:", self.balance)
        if 0 <= summa <= self.balance:
            self.balance -= summa
            print("Withdrawal:", summa)
            print("Balance:", self.balance)
        else:
            print("You don't have enough")

owner_name = input()
i_balance = float(input())
account = Account(owner_name, i_balance)

deposit_amount = float(input())
account.deposit(deposit_amount)

withdraw_amount = float(input())
account.withdraw(withdraw_amount)


