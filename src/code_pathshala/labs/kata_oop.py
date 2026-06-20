"""
OOP Lab Challenge (Kata).
Implement a class BankAccount with methods to deposit, withdraw, and track transaction logs.
"""


class InsufficientFundsError(Exception):
    """Raised when withdrawing more money than is available in the account balance."""

    pass


class BankAccount:
    """
    Simulates a Bank Account with balance tracking, deposits, withdrawals, and logs.
    """

    def __init__(self, owner: str, initial_balance: float = 0.0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions: list[str] = [
            f"Account created with balance: ${initial_balance:.2f}"
        ]

    def deposit(self, amount: float) -> float:
        """
        Deposits an amount into the account. Increases balance.
        Must raise ValueError if deposit amount is negative or zero.
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount
        self.transactions.append(f"Deposited: ${amount:.2f}")
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Withdraws an amount from the account. Decreases balance.
        Must raise ValueError if withdraw amount is negative or zero.
        Must raise InsufficientFundsError if balance is less than withdraw amount.
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise InsufficientFundsError(
                f"Insufficient funds. Available balance: ${self.balance:.2f}"
            )
        self.balance -= amount
        self.transactions.append(f"Withdrew: ${amount:.2f}")
        return self.balance
