import os
import json
import pytest
from app.data_manager import DataManager

@pytest.fixture
def temp_data_file(tmp_path):
    d = tmp_path / "data"
    d.mkdir()
    f = d / "test_accounts.json"
    return f

def test_data_manager_initialization(temp_data_file, mocker):
    # Mocking os.path.dirname and os.path.abspath to point to our temp directory
    # but DataManager calculates filepath relative to app/data_manager.py
    # This is tricky to test without changing DataManager to accept filepath.
    # Let's mock os.path.join in DataManager.__init__ instead, or just mock the filepath.

    mocker.patch("os.path.join", return_value=str(temp_data_file))
    dm = DataManager("test_accounts.json")
    assert dm.filepath == str(temp_data_file)

def test_load_raw_data_empty(temp_data_file, mocker):
    mocker.patch("os.path.exists", side_effect=lambda path: path == str(temp_data_file) and temp_data_file.exists())
    dm = DataManager("test_accounts.json")
    dm.filepath = str(temp_data_file)

    assert dm._load_raw_data() == []

def test_save_and_get_account(temp_data_file, mocker):
    dm = DataManager("test_accounts.json")
    dm.filepath = str(temp_data_file)

    account_data = {
        "account_number": "111222",
        "name": "Alice",
        "balance": 500.0,
        "pin": "1111"
    }

    dm.save_account(account_data)

    retrieved = dm.get_account("111222")
    assert retrieved == account_data

    # Check if file actually exists and contains data
    assert temp_data_file.exists()
    with open(temp_data_file, "r") as f:
        data = json.load(f)
        assert data == [account_data]

def test_update_account(temp_data_file):
    dm = DataManager("test_accounts.json")
    dm.filepath = str(temp_data_file)

    acc1 = {"account_number": "1", "name": "A", "balance": 100, "pin": "1"}
    dm.save_account(acc1)

    acc1_updated = {"account_number": "1", "name": "A", "balance": 200, "pin": "1"}
    dm.save_account(acc1_updated)

    all_accounts = dm._load_raw_data()
    assert len(all_accounts) == 1
    assert all_accounts[0]["balance"] == 200
