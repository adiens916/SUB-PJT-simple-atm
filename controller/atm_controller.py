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
from .controller_type import Response


class AtmController:
    def get_linked_account_number(self, card_number: str) -> Response:
        try:
            account_number = card_service.get_linked_account_number(card_number)
            return {"data": account_number, "ok": "true", "message": ""}
        except Exception:
            return {"data": "", "ok": "false", "message": "No linked account."}

    def get_balance(self, account_number: str) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": 0, "ok": "false", "message": "Not valid account."}

        try:
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": ""}
        # TODO: Specific exception needed
        except Exception:
            return {"data": 0, "ok": "false", "message": "No such an account."}

    def deposit(self, account_number: str, deposit: int) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": 0, "ok": "false", "message": "Not valid account."}

        try:
            account_service.deposit(account_number, deposit)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except Exception:
            return {"data": 0, "ok": "false", "message": "Not available input."}

    def withdraw(self, account_number: str, withdrawal: int) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": 0, "ok": "false", "message": "Not valid account."}

        try:
            account_service.withdraw(account_number, withdrawal)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except Exception:
            return {"data": 0, "ok": "false", "message": "Not enough money."}


class BankController:
    def create_account(self) -> Response:
        account = account_service.create_account()
        return {
            "data": account.account_number,
            "ok": "true",
            "message": "Account created.",
        }

    def create_card(self, pin_number: str, account_number: str) -> Response:
        card = card_service.create_card(pin_number, account_number)
        return {"data": card.card_number, "ok": "true", "message": "Card created."}

    def authenticate_card_by_pin(self, card_number: str, pin_number: str) -> Response:
        result = card_service.authenticate_card_by_pin(card_number, pin_number)
        if result == True:
            return {"data": True, "ok": "true", "message": "Matched PIN."}
        else:
            return {"data": False, "ok": "true", "message": "Not matched PIN."}
