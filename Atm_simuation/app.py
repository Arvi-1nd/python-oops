#---------------------ATM Simulations-------------------------------#########


class Account:
    def __init__(self,name,account_no,pin,balance,phone,email):
        self.name = name
        self.account_no = account_no
        self.pin = pin
        self.balance = balance
        self.phone = phone
        self.email = email
        
class Notification:
    def  send_sms(self, phone, message):
        print(f"sms sent to {phone}: {message}")
        
    def send_mail(self, email, message):
        print(f"mail sent to {email}: {message}")
        
        
class ATM:
    def __init__(self):
        self.notification = Notification()
        
    def authenticate(self, account, pin):
        return account.pin == pin
    
    
    def deposit(self, account, pin, amount):
        if not self.authenticate(account,pin):
            print("invalid pin")
            return
        
        account.balance += amount
        print(f"Deposited {amount}")
        print(f"Current balance: {account.balance}")
        
        message = f"Amount deposited {amount} . Available Balance {account.balance}"
        self.notification.send_sms(account.phone, message)
        self.notification.send_mail(account.email, message)
        
    def withdraw(self, account, pin, amount):
        if not self.authenticate(account,pin):
            print("Invalid pin")
            return
        
        if amount > account.balance:
            print("Insufficient Balance")
            return
        
        account.balance -= amount
        print(f"Withdraw {amount}")
        print(f" Remaining Balance: {account.balance}")
        
        message = f"{amount} withdrawn. Remaining balance {account.balance}"
        self.notification.send_sms(account.phone,message)
        self.notification.send_mail(account.email,message)
        
    def check_balance(self, account, pin):
        if not self.authenticate(account,pin):
            print("Invalid pin")
            return
        
        print(f" Available Balance: {account.balance}")
        
        message = f"Balance enquiry: {account.balance}"
        self.notification.send_sms(account.phone,message)
        self.notification.send_mail(account.email,message)
        

if __name__ == "__main__":
    
    user = Account(
        name="Sonia",
        account_no="56783",
        pin=3457,
        balance=5000,
        phone="8903456789",
        email="allisgood@gmailcom"
    )
    
    atm = ATM()
        
    print("\n---Deposit-------")
    atm.deposit(user, 3457,2000)
    
    print("\n---Withdraw------")
    atm.withdraw(user, 3457, 1500)
    
    print("\n----Check Balance ---")
    atm.check_balance(user, 3457)