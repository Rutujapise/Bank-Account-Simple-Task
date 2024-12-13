class BankAccount:
    def __init__(self):
       
        self.balance = 0

    def deposit(self, amount):
        #For Deposit amount.
        if amount > 0:
            self.balance += amount
            print(f"Balance after deposit: {self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        #  For Withdraw  amount 
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"Balance after withdrawal: {self.balance}")
            else:
                print("Insufficient bank balance.")
        else:
            print("Withdrawal amount must be positive.")

# Example usage for given task output.
account = BankAccount()
account.deposit(1000)      
account.withdraw(200)     
