#Creating account debit and credit system in a class
class Account:
    
    def _init_(self,bal,acc):
        self.balance = bal
        self.account = acc
        
    def debit(self,amount):
        self.balance -= amount
        print(amount,"was debited from your account",)
        print("Your Remaining :",self.get_bal())
            
   
    def credit(self,amount):
        self.balance += amount
        print(amount,"was credited in your account")
        print("Your Remaining :",self.get_bal())
        
    def get_bal(self):
        return self.balance
        
        
        
acc1 = Account(10000,12345)   
acc1.debit(2000)
acc1.credit(500)