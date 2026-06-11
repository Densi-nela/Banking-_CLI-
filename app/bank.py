import argparse


def create_parser():
    parser = argparse.ArgumentParser(
        prog="bank-cli",
        description="Secure Banking CLI System",
        epilog="Example: python -m app create --name User --pin 1234",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    create_account = subparsers.add_parser("create", help="Open a new account")
    create_account.add_argument("--name", required=True, help="Account holder's name")
    create_account.add_argument("--pin", required=True, help="4-digit PIN")

    account_deposit = subparsers.add_parser("deposit", help="Add funds")
    account_deposit.add_argument("--account", required=True, help="Account Number")
    account_deposit.add_argument(
        "--amount", type=float, required=True, help="Amount to deposit"
    )

    account_withdraw = subparsers.add_parser("withdraw", help="Withdraw funds")
    account_withdraw.add_argument("--account", required=True, help="Account Number")
    account_withdraw.add_argument(
        "--amount", type=float, required=True, help="Amount to withdraw"
    )
    account_withdraw.add_argument("--pin", required=True, help="Security PIN")

    account_balance = subparsers.add_parser("balance", help="Check balance")
    account_balance.add_argument("--account", required=True, help="Account Number")
    account_balance.add_argument("--pin", required=True, help="Security PIN")

    return parser


def show_banner():
    print(
        """
    |      Welcome to Secure Banking CLI       |
    |   Your Trusted Partner in Financial Management  |
    """
    )


def show_success(message):
    print(f"[SUCCESS] {message}")


def show_error(message):
    print(f"[ERROR] {message}")


def show_balance(account, balance):
    print(f"[INFO] Account: {account} | Balance: ${balance:,.2f}")
