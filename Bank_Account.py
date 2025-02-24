#create a class name bank account an attrubute account_holder to store account holder and attribut balance to store the account balance initalize to 0 add following methos to class
#deposit - add given ammount to the balance
#widrow - subsract the given amount from the balance if sufficient fund exsist otherwise print an error msg
#display balane
#write small script to demostrate the following
    #create an ob of bank acc class
    #perform a few deposit and withdrowal operations
    #display the balance after each operation

class BankAccount:
    def __init__(self, bank_holder):
        self.bank_holder = bank_holder
        self.balance = 0  # Initialize balance to 0
    
    def deposit(self, deposit_ammount):
        if deposit_ammount > 0:
            self.balance += deposit_ammount  # Properly indented
        else:
            print("Amount should be positive")
        
    def withdraw(self, withdraw_ammount):  # Fixed spelling 'withdrow' to 'withdraw'
        if withdraw_ammount < 0:
            print("Amount should be positive")
        elif withdraw_ammount > self.balance:
            print("Insufficient Balance")
        else:
            self.balance -= withdraw_ammount

    def check_balance(self):  # Renamed from 'balance' to 'check_balance'
        print("Current balance =", self.balance)


# Example usage
bank_account = BankAccount("Jana")
bank_account.deposit(1000)
bank_account.withdraw(500)
bank_account.check_balance()  # Display the current balance

