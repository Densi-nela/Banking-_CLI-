import pytest
from app.models import Account

def test_account_initialization():
    acc = Account("123456", "Test User", "1234", 100.0)
    assert acc.account_number == "123456"
    assert acc.name == "Test User"
    assert acc.pin == "1234"
    assert acc.balance == 100.0

def test_account_deposit():
    acc = Account("123456", "Test User", "1234", 100.0)
    acc.deposit(50.0)
    assert acc.balance == 150.0

def test_account_deposit_negative():
    acc = Account("123456", "Test User", "1234", 100.0)
    with pytest.raises(ValueError, match="Can't deposit negative or zero!"):
        acc.deposit(-10.0)

def test_account_withdraw_success():
    acc = Account("123456", "Test User", "1234", 100.0)
    acc.withdraw(40.0, "1234")
    assert acc.balance == 60.0

def test_account_withdraw_wrong_pin():
    acc = Account("123456", "Test User", "1234", 100.0)
    with pytest.raises(Exception, match="Wrong PIN!"):
        acc.withdraw(40.0, "4321")

def test_account_withdraw_insufficient_funds():
    acc = Account("123456", "Test User", "1234", 100.0)
    with pytest.raises(Exception, match="Not enough money!"):
        acc.withdraw(150.0, "1234")

def test_account_withdraw_negative():
    acc = Account("123456", "Test User", "1234", 100.0)
    with pytest.raises(ValueError, match="Withdrawal amount must be positive!"):
        acc.withdraw(-10.0, "1234")

def test_account_to_dict():
    acc = Account("123456", "Test User", "1234", 100.0)
    expected = {
        "account_number": "123456",
        "name": "Test User",
        "balance": 100.0,
        "pin": "1234",
    }
    assert acc.to_dict() == expected

def test_account_from_dict():
    data = {
        "account_number": "123456",
        "name": "Test User",
        "balance": 100.0,
        "pin": "1234",
    }
    acc = Account.from_dict(data)
    assert acc.account_number == "123456"
    assert acc.name == "Test User"
    assert acc.balance == 100.0
    assert acc.pin == "1234"
