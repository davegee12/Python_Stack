class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = {}

    def open_account(self, accountName, int_rate=2):
        self.account[accountName] = BankAccount(int_rate)

    def make_deposit(self, accountName, amount):
        self.account[accountName].deposit(amount)
        return self

    def make_withdrawal(self, accountName, amount):
        self.account[accountName].withdraw(amount)
        return self

    def display_user_balance(self, accountName):
        print(f"User: {self.name}, Balance: {self.account[accountName]}")
        return self

    def transfer_money(self, accountName, other_user, amount):
        self.account[accountName] -= amount
        other_user.account += amount
        return self

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