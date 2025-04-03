class Account:
    def __init__(self,balance,acct):
        self.balance = balance
        self.acct = acct
        

    def debit(self , amount):
        self.balance -= amount
        print("Rs",amount,"is debited from your account number",self.acct)
        print("Total Balance is =",self.get_balance())

    def credit(self,amount):
        self.balance += amount
        print("Rs",amount , "was credited from your account number",self.acct)
        print("Total Balance =",self.get_balance()) 

    def get_balance(self):
        return self.balance


acct1 = Account(10000,12345)
acct1.debit(1000)
acct1.credit(500)
acct1.credit(40000)