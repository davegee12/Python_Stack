class BankAccount:
    def __init__(self, int_rate=0.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        if amount > self.balance:
            self.balance -= 5
            raise ValueError("Insufficient funds: Charging a $5 fee")
        else:
            self.balance -= amount
        return self

    def display_account_info(self):
        print(self.balance)
        return self

    def yield_interest(self):
        if self.balance < 0:
            raise ValueError("Insufficient Funds")
        self.balance += (self.balance * self.int_rate)
        return self

Comerica = BankAccount(0.02, 500)
Chase = BankAccount(0.01, 400)

Comerica.deposit(200).deposit(120).deposit(40).withdraw(80).yield_interest().display_account_info()
Chase.deposit(300).deposit(20).withdraw(30).withdraw(100).withdraw(60).withdraw(100).yield_interest().display_account_info()
