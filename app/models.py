class Account:
    def __init__(self, account_number, name, pin, balance=0):
        self.account_number = account_number
        self.name = name
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        """Add money to account"""
        if amount <= 0:
            raise ValueError("Can't deposit negative or zero!")
        self.balance += amount
        return self.balance

    def withdraw(self, amount, pin):
        """Take money out if PIN is correct and funds available"""
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive!")

        if pin != self.pin:
            raise Exception("Wrong PIN!")

        if amount > self.balance:
            raise Exception("Not enough money!")

        self.balance -= amount
        return self.balance

    def to_dict(self):
        """Convert account to dictionary for saving"""
        return {
            "account_number": self.account_number,
            "name": self.name,
            "balance": self.balance,
            "pin": self.pin,
        }

    @classmethod
    def from_dict(cls, data):
        """Create account from dictionary (loading from file)"""
        return cls(data["account_number"], data["name"], data["pin"], data["balance"])
