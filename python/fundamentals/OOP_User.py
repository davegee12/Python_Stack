class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
        return self
    def make_withdrawal(self, amount):
        self.account_balance -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.account_balance}")
        return self
    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self

Dave = User('Dave', 'dave@python.com')
Mike = User('Mike', 'mike@python.com')
Shannon = User('Shannon', 'shannon@python.com')

# Dave.make_deposit(200)
# Dave.make_deposit(300)
# Dave.make_deposit(30)
# Dave.make_withdrawal(50)
# Dave.display_user_balance()

# Mike.make_deposit(500)
# Mike.make_deposit(230)
# Mike.make_withdrawal(40)
# Mike.make_withdrawal(100)
# Mike.display_user_balance()

# Shannon.make_deposit(600)
# Shannon.make_withdrawal(20)
# Shannon.make_withdrawal(250)
# Shannon.make_withdrawal(60)
# Shannon.display_user_balance()

# Dave.transfer_money(Shannon, 100)
# Dave.display_user_balance()
# Shannon.display_user_balance()

Dave.make_deposit(200).make_deposit(300).make_deposit(30).make_withdrawal(50).display_user_balance()
Mike.make_deposit(500).make_deposit(230).make_withdrawal(40).make_withdrawal(100).display_user_balance()
Shannon.make_deposit(600).make_withdrawal(20).make_withdrawal(250).make_withdrawal(60).display_user_balance()
Dave.transfer_money(Shannon, 100).display_user_balance()
Shannon.display_user_balance()