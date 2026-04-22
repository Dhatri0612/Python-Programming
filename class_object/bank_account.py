class BankAccount:
    def __init__(self,name,balance):
        self.name=name
        self.balance=balance
    def deposit(self,amount):
        self.balance+=amount
        print("Deposited: ",amount)
    def withdraw(self, amount):
        if amount<=self.balance:
            self.balance-=amount
            print("Withdrawn: ",amount)
        else:
            print("Insufficient balance")
    def show_balance(self):
        print("Current balance: ",self.balance)

a=BankAccount("Priti",10000)
a.deposit(500)
a.withdraw(400)
a.withdraw(20000)
a.show_balance()