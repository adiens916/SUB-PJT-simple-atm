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


def get_balance(account_number: str):
    try:
        balance = account_service.get_balance(account_number)
        return f"Current Balance: {balance}"
    except Exception:
        return "No such an account."


def deposit(account_number: str, deposit: int):
    try:
        deposit = int(input())
        account_service.deposit(account_number, deposit)
        return {}
    except Exception:
        return "Not available input"


def withdraw(account_number: str, withdrawal: int):
    try:
        withdrawal = int(input())
        account_service.withdraw(account_number, withdrawal)
        return {}
    except Exception:
        return "Not enough money"
