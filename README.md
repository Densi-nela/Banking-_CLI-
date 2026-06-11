#  Banking CLI

A simple yet powerful command-line banking application built purely with Python's standard library. No external dependencies required!

##  Description

Banking CLI is a lightweight banking system that runs entirely in your terminal. It demonstrates clean architecture principles by separating interface logic, business logic, and data persistence layers. Users can manage their bank accounts with simple commands—create accounts, deposit money, withdraw funds, and check balances—all through an intuitive command-line interface.

##  Features

- **Account Creation**: Generate a new bank account with a unique 6-digit account number
- **Secure Authentication**: PIN-based security for all transactions
- **Deposit Money**: Add funds to your account
- **Withdraw Money**: Securely withdraw funds with PIN verification
- **Balance Inquiry**: Check your current account balance
- **Data Persistence**: All account data is stored locally in JSON format

## Project Structure
```
banking-cli/
├── app/
│   ├── __main__.py        # Project entry point
│   ├── bank.py           # CLI interface layer (user interaction)
│   ├── models.py         # Business logic layer (validation & instances)
│   └── data_manager.py   # Data persistence layer (JSON storage)
├── data/
│   └── accounts.json     # User account data storage
├── tests/
│   ├── test_models.py    # Unit tests for business logic
│   └── test_data_manager.py # Unit tests for data persistence
└── README.md
```

## Application Flow
```
User Input (CLI)
       ↓
bank.py (Interface Logic)
       ↓
models.py (Validation & Business Logic)
       ↓
data_manager.py (Data Persistence)
       ↓
accounts.json (Storage)
```

1. **Interface Layer** (`bank.py`): Handles user interaction through CLI commands
2. **Logic Layer** (`models.py`): Validates input and creates/manages account instances
3. **Data Layer** (`data_manager.py`): Ensures data persistence by reading/writing to JSON storage

## Technologies Used

This project uses only Python's standard library:

- **`typing`** - Type hints and type inference for better code quality
- **`os`** - File system operations and path management
- **`json`** - JSON data serialization and storage
- **`argparse`** - CLI argument parsing and command interface creation

##  Installation & Setup

### Prerequisites
- Python 3.6 or higher
- Git

### Clone the Repository
```bash
git clone git@github.com:Densi-nela/Banking-_CLI-.git

cd CLI
```

No additional dependencies need to be installed for the main application!

## Testing

This project uses `pytest` for testing.

### Install Testing Dependencies
```bash
pip install pytest pytest-mock
```

### Run Tests
```bash
PYTHONPATH=. pytest
```

##  Usage


### 1. Create an Account

Create a new bank account by providing your name and a secure PIN.
```bash
python3 -m app create --name "Densinela" --pin "1234"
```



### 2. Deposit Money

Deposit funds into your account using your account number.
```bash
python3 -m app deposit --account "123456" --amount 1000
```



![Deposit Example]

### 3. Withdraw Money

Withdraw funds from your account with PIN authentication.
```bash
python3 -m app withdraw --account "123456" --amount 500 --pin "1234"
```



![Withdraw Example]

### 4. Check Balance

View your current account balance securely with your PIN.
```bash
python3 -m app balance --account "123456" --pin "1234"
```



![Balance Check Example]

##  Command Reference

| Command | Arguments | Description |
|---------|-----------|-------------|
| `create` | `--name`, `--pin` | Create a new bank account |
| `deposit` | `--account`, `--amount` | Deposit money to an account |
| `withdraw` | `--account`, `--amount`, `--pin` | Withdraw money from an account |
| `balance` | `--account`, `--pin` | Check account balance |

##  Security Features

- PIN authentication for sensitive operations (withdraw, balance check)
- Data validation for all inputs
- Secure local storage of account information

##  Error Handling

The application handles common errors gracefully:
- Invalid account numbers
- Incorrect PINs
- Insufficient funds for withdrawal
- Invalid input formats



## 👥 Authors

- Densinela Chepngetich

## 🙏 Acknowledgments

- Built as part of SFD17 Python module learning project
- Demonstrates clean architecture and separation of concerns
- Great example of CLI development using Python's standard library

---
