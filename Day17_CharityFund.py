class CharityFund:
    def __init__(self, balance = 10000):
        self.balance = balance
    def SaveFund(self, amount):
        self.balance += amount
    def SpendFund(self, amount):
        self.balance -= amount
    def invest(self, ReturnRate):
        self.balance *= 1 + ReturnRate 
    def GetBalance(self):
        if self.balance < 0:
            # self.balance = -self.balance
            print(f'You have entered a deficit of {-self.balance}.')
        return self.balance
    def IsDanger(self):
        if self.balance < 5000:
            print(f'Your fund is less than 50000. Be careful of your spendings.')
        return self.balance < 50000
    
    
HelpNeedy = CharityFund()
HelpNeedy.SpendFund(10001)
print(f'Your balance is now {HelpNeedy.GetBalance()}.')
HelpNeedy.SaveFund(20000)
print(f'Your new balance is {HelpNeedy.GetBalance()}.')
HelpNeedy.invest(0.90)
print(f'Your new balance is {HelpNeedy.GetBalance()}.')
