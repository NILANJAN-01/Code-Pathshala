import pytest
from code_pathshala.labs.kata_oop import BankAccount, InsufficientFundsError


def test_bank_account_initialization():
    acc = BankAccount("Alice", 100.0)
    assert acc.owner == "Alice"
    assert acc.balance == 100.0
    assert len(acc.transactions) == 1


def test_bank_account_deposit():
    acc = BankAccount("Bob", 50.0)
    new_bal = acc.deposit(100.0)
    assert new_bal == 150.0
    assert acc.balance == 150.0
    assert "Deposited: $100.00" in acc.transactions[-1]


def test_bank_account_deposit_negative():
    acc = BankAccount("Bob", 50.0)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        acc.deposit(-10.0)
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        acc.deposit(0)


def test_bank_account_withdraw():
    acc = BankAccount("Charlie", 200.0)
    new_bal = acc.withdraw(75.5)
    assert new_bal == 124.5
    assert acc.balance == 124.5
    assert "Withdrew: $75.50" in acc.transactions[-1]


def test_bank_account_withdraw_insufficient_funds():
    acc = BankAccount("Charlie", 100.0)
    with pytest.raises(InsufficientFundsError):
        acc.withdraw(150.0)


def test_bank_account_withdraw_negative():
    acc = BankAccount("Charlie", 100.0)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive"):
        acc.withdraw(-20.0)
