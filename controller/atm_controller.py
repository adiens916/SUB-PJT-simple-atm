# For importing services in other folders
import os
import sys

file = os.path.realpath(__file__)
parent_dir = os.path.abspath(os.path.join(file, os.pardir))
root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

# Import services
from service.account_service import AccountService
from service.card_service import CardService

account_service = AccountService()
card_service = CardService()

# Import type
from .atm_controller_type import Response


class AtmController:
    def get_balance(account_number: str) -> Response:
        try:
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": ""}
        except Exception:
            return {"data": None, "ok": "false", "message": "No such an account."}

    def deposit(account_number: str, deposit: int) -> Response:
        try:
            account_service.deposit(account_number, deposit)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except Exception:
            return {"data": None, "ok": "false", "message": "Not available input."}

    def withdraw(account_number: str, withdrawal: int) -> Response:
        try:
            account_service.withdraw(account_number, withdrawal)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except Exception:
            return {"data": None, "ok": "false", "message": "Not enough money."}
