class Account:
    def __init__(self, account_number, name, initial_balance=0):
        self.account_number = account_number
        self.name = name
        self.balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} to {self.name}'s account.")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount} from {self.name}'s account.")
        else:
            print("Insufficient funds or invalid withdrawal amount.")

    def check_balance(self):
        print(f"Account Balance for {self.name}: {self.balance}")
        return self.balance


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
        else:
            account = Account(account_number, name, initial_balance)
            self.accounts[account_number] = account
            print(f"Account created for {name} with account number {account_number}.")

    def get_account(self, account_number):
        account = self.accounts.get(account_number)
        if account:
            return account
        else:
            print("Account not found.")
            return None


# Main function to demonstrate usage
def main():
    bank = Bank()

    # Creating accounts
    bank.create_account("12345", "Alice", 1000)
    bank.create_account("67890", "Bob", 500)

    # Accessing and performing operations on an account
    account = bank.get_account("12345")
    if account:
        account.check_balance()
        account.deposit(500)
        account.check_balance()
        account.withdraw(200)
        account.check_balance()

    # Accessing another account
    account = bank.get_account("67890")
    if account:
        account.check_balance()
        account.withdraw(700)  # Should print insufficient funds message


if __name__ == "__main__":
    main()
