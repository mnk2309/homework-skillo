class BankAccount:
    def __init__(self, initial_balance=0):
        self.balance = initial_balance

    def get_balance(self):
        return self.balance


class Deposit:
    def __init__(self, account):
        self.account = account

    def deposit(self, amount):
        if amount > 0:
            self.account.balance += amount
            print(f'Deposit ${amount}. Balance: ${self.account.get_balance()}')
        else:
            return f'Invalid deposit amount. Amount should be greater than zero '


class Withdraw:
    def __init__(self, account):
        self.account = account

    def withdraw(self, amount):
        if amount > 0 <= self.account.get_balance():
            self.account.balance -= amount
            print(f'Withdrew ${amount} from your bank account. Current balance: {self.account.get_balance()}')
        else:
            return f'Unauthorised withdrawal! Amount must be greater than zero'


account = BankAccount(10000)
deposit = Deposit(account)
withdraw = Withdraw(account)

deposit.deposit(500)
withdraw.withdraw(1500)
