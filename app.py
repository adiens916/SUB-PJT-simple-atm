import os
import sys

file = os.path.realpath(__file__)
parent_dir = os.path.abspath(os.path.join(file, os.pardir))
root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)


from service.account_service import AccountService
from service.card_service import CardService


account_service = AccountService()
card_service = CardService()

account_number = ""
card_number = ""


def main():

    while True:
        print()
        print("< Simple ATM >")

        print("You can select one of these.")
        print("- 1. See Balance")
        print("- 2. Deposit")
        print("- 3. Withdraw")
        print("- 4. Exit")

        command = input("Enter a command: ")
        check_auth()

        if command == "1":
            try:
                balance = account_service.get_balance(account_number)
                print(f"Current Balance: {balance}")
            except Exception:
                print("No such an account.")

        elif command == "2":
            try:
                deposit = int(input())
                account_service.deposit(account_number, deposit)
            except Exception:
                print("Not available input")

        elif command == "3":
            try:
                withdrawal = int(input())
                account_service.withdraw(account_number, withdrawal)
            except Exception:
                print("Not enough money")

        elif command == "4":
            break


def check_auth():
    global account_number

    if not account_number:
        print("Please enter your account number (including '-').")
        print("If you don't have one, then input 'new' for creating a new account.")
        print("Otherwise, you can return by input 'no'.")
        user_input = input(": ")

        if user_input.lower() == "new":
            account = account_service.create_account()
            account_number = account.account_number
            print("Now your account has been created!")
            print("Your account number is", account_number)


main()
