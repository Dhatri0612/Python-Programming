class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print("Balance after deposit:", self.balance)

    def show_balance(self):
        print("Current Balance:", self.balance)


class Savings(BankAccount):
    def add_interest(self, rate):
        interest = (self.balance * rate) / 100
        self.balance += interest
        print("Balance after interest:", self.balance)


class Current(BankAccount):
    def __init__(self, balance, overdraft_limit):
        super().__init__(balance)
        self.overdraft_limit = overdraft_limit

    def withdraw(self, amount):
        if self.balance - amount >= -self.overdraft_limit:
            self.balance -= amount
            print("Withdrawal successful. Balance:", self.balance)
        else:
            print("Overdraft limit exceeded!")



s = Savings(1000)
s.deposit(500)
s.add_interest(10)
s.show_balance()



c = Current(1000, 500)
c.withdraw(1200)   
c.withdraw(500)    
c.show_balance()