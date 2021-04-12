class User:        
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account_balance = 0
    # deposit method
    def make_deposit(self, amount):    
        self.account_balance += amount    
    # withdrawal method
    def make_withdrawal(self, amount):
        self.account_balance -= amount
    # display balance
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")
    
rick = User("rick", "rick@dojo.com")
zaur = User("zaur", "zaur@dojo.com")
aly = User("aly", "aly@dojo.com")

rick.make_deposit(150)
rick.make_deposit(10)
rick.make_deposit(200)
rick.make_withdrawal(75)
rick.display_user_balance()

zaur.make_deposit(1000)
zaur.make_deposit(150)
zaur.make_withdrawal(350)
zaur.make_withdrawal(75)
zaur.display_user_balance()

aly.make_deposit(1000)
aly.make_withdrawal(100)
aly.make_withdrawal(150)
aly.make_withdrawal(100)
aly.display_user_balance()