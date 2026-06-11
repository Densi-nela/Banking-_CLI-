import random

from .models import Account
from .data_manager import DataManager
from .bank import create_parser, show_banner, show_success, show_error, show_balance


def main():
    show_banner()
    parser = create_parser()
    args = parser.parse_args()

    dm = DataManager()

    try:
        if args.command == "create":
            new_id = str(random.randint(100000, 999999))
            new_acc = Account(new_id, args.name, args.pin)
            dm.save_account(new_acc.to_dict())
            show_success(f"Account Created! ID: {new_id} | Name: {args.name}")

        elif args.command == "deposit":
            data = dm.get_account(args.account)
            if not data:
                show_error("Account not found.")
                return

            acc = Account.from_dict(data)
            acc.deposit(args.amount)
            dm.save_account(acc.to_dict())
            show_success(f"Deposited ${args.amount:.2f} to account {args.account}")

        elif args.command == "withdraw":
            data = dm.get_account(args.account)
            if not data:
                show_error("Account not found.")
                return

            acc = Account.from_dict(data)
            acc.withdraw(args.amount, args.pin)
            dm.save_account(acc.to_dict())
            show_success(
                f"Withdrew ${args.amount:.2f}. New Balance: ${acc.balance:.2f}"
            )

        elif args.command == "balance":
            data = dm.get_account(args.account)
            if not data:
                show_error("Account not found.")
                return

            if data["pin"] != args.pin:
                show_error("Invalid PIN")
                return

            show_balance(args.account, data["balance"])

        else:
            parser.print_help()

    except Exception as e:
        show_error(str(e))


if __name__ == "__main__":
    main()
