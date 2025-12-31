class BankAccount(ABC):
    def __init__(self, account_number, holder_name, balance=0):
        self._account_number = account_number
        self._holder_name = holder_name
        self._balance = balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        if amount <= self._balance:
            self._balance -= amount
            print(f"₹{amount} withdrawn successfully.")
        else:
            print("Insufficient balance.")

    def get_balance(self):
        return self._balance

    @abstractmethod
    def account_type(self):
        pass

    def display_details(self):
        print("\n--- Account Details ---")
        print(f"Account Number : {self._account_number}")
        print(f"Holder Name   : {self._holder_name}")
        print(f"Account Type  : {self.account_type()}")
        print(f"Balance       : ₹{self._balance}")


class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"


class CurrentAccount(BankAccount):
    def account_type(self):
        return "Current Account"

class Bank:
    def __init__(self, name):
        self.name = name
        self.accounts = {}

    def create_account(self, account):
        self.accounts[account._account_number] = account
        print("Account created successfully!")

    def get_account(self, account_number):
        return self.accounts.get(account_number)

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)

        if sender and receiver:
            if sender.get_balance() >= amount:
                sender.withdraw(amount)
                receiver.deposit(amount)
                print("Transfer successful!")
            else:
                print("Insufficient balance for transfer.")
        else:
            print("Invalid account number.")


if __name__ == "__main__":
    bank = Bank("My Python Bank")

    acc1 = SavingsAccount(101, "Alex", 5000)
    acc2 = CurrentAccount(102, "Jordan", 3000)

    bank.create_account(acc1)
    bank.create_account(acc2)

    acc1.deposit(1000)
    acc1.withdraw(2000)

    bank.transfer(101, 102, 1500)

    acc1.display_details()
    acc2.display_details()
