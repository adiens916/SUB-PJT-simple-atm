# For importing services in other folders
import os
import sys

file = os.path.realpath(__file__)
parent_dir = os.path.abspath(os.path.join(file, os.pardir))
root_dir = os.path.abspath(os.path.join(parent_dir, os.pardir))
sys.path.append(root_dir)

# Import services
from service.account_service import (
    AccountService,
    NoSuchAccountError,
    ZeroDepositError,
    NegativeValueError,
    NotIntError,
    NotEnoughBalanceError,
)
from service.card_service import (
    CardService,
    NoLinkedAccountError,
    EmptyPinNumberError,
    WrongPinNumberError,
    WrongFormatError,
)
from repository.account_repository import (
    NoSuchAccountError as NoAccountInDBError,
    DuplicateKeySaveError as DuplicateAccountError,
)
from repository.card_repository import (
    NoSuchCardError,
    DuplicateKeySaveError as DuplicateCardError,
)

account_service = AccountService()
card_service = CardService()

# Import type
from .controller_type import Response


class AtmController:
    def get_linked_account_number(self, card_number: str) -> Response:
        try:
            account_number = card_service.get_linked_account_number(card_number)
            return {"data": account_number, "ok": "true", "message": ""}
        except WrongFormatError:
            return {
                "data": "",
                "ok": "false",
                "message": "Incorrect card number format.",
            }
        except NoSuchCardError:
            return {"data": "", "ok": "false", "message": "No such card."}
        except NoLinkedAccountError:
            return {
                "data": "",
                "ok": "false",
                "message": "No linked account to the card.",
            }

    def get_balance(self, account_number: str) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": -1, "ok": "false", "message": "Not valid account."}

        try:
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": ""}
        except NoAccountInDBError:
            return {"data": -1, "ok": "false", "message": "No such an account."}

    def deposit(self, account_number: str, deposit: int) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": -1, "ok": "false", "message": "Not valid account."}

        try:
            account_service.deposit(account_number, deposit)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except ZeroDepositError:
            return {"data": -1, "ok": "false", "message": "Not available zero input."}
        except NegativeValueError:
            return {
                "data": -1,
                "ok": "false",
                "message": "Not available negative value.",
            }
        except NotIntError:
            return {
                "data": -1,
                "ok": "false",
                "message": "No integer value.",
            }

    def withdraw(self, account_number: str, withdrawal: int) -> Response:
        validity = account_service.validate_account_number(account_number)
        if not validity:
            return {"data": -1, "ok": "false", "message": "Not valid account."}

        try:
            account_service.withdraw(account_number, withdrawal)
            balance = account_service.get_balance(account_number)
            return {"data": balance, "ok": "true", "message": "Balance updated."}
        except NegativeValueError:
            return {
                "data": -1,
                "ok": "false",
                "message": "Not available negative value.",
            }
        except NotIntError:
            return {
                "data": -1,
                "ok": "false",
                "message": "No integer value.",
            }
        except NotEnoughBalanceError:
            return {"data": -1, "ok": "false", "message": "Not enough money."}


class BankController:
    def create_account(self) -> Response:
        while True:
            try:
                account = account_service.create_account()
                return {
                    "data": account.account_number,
                    "ok": "true",
                    "message": "Account created.",
                }
            except DuplicateAccountError:
                continue

    def create_card(self, pin_number: str, account_number: str) -> Response:
        while True:
            try:
                card = card_service.create_card(pin_number, account_number)
                return {
                    "data": card.card_number,
                    "ok": "true",
                    "message": "Card created.",
                }
            except EmptyPinNumberError:
                return {"data": "", "ok": "false", "message": "Empty pin number."}
            except WrongPinNumberError:
                return {"data": "", "ok": "false", "message": "Wrong pin number."}
            except DuplicateCardError:
                continue

    def authenticate_card_by_pin(self, card_number: str, pin_number: str) -> Response:
        try:
            result = card_service.authenticate_card_by_pin(card_number, pin_number)
            if result == True:
                return {"data": True, "ok": "true", "message": "Matched PIN."}
            else:
                return {"data": False, "ok": "true", "message": "Not matched PIN."}
        except NoSuchCardError:
            return {"data": "", "ok": "false", "message": "No such card."}
        except EmptyPinNumberError:
            return {"data": "", "ok": "false", "message": "Empty pin number."}
        except WrongPinNumberError:
            return {"data": "", "ok": "false", "message": "Wrong pin number."}
