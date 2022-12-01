from domain.account import Account
from repository.account_repository_memory import AccountRepositoryMemory
from repository.account_repository import (
    NoSuchAccountError as NoAccountInDBError,
    DuplicateKeySaveError,
)


class AccountService:
    def __init__(self) -> None:
        self.repository = AccountRepositoryMemory()

    def create_account(self) -> Account:
        try:
            account = self.repository.save(Account())
            return account
        except DuplicateKeySaveError:
            raise DuplicateKeySaveError

    def validate_account_number(self, account_number: str) -> bool:
        return Account.validate_account_number(account_number)

    def get_balance(self, account_number: str) -> int:
        try:
            account = self.repository.find_by_account_number(account_number)
            return account.balance
        except NoAccountInDBError:
            raise NoSuchAccountError

    def deposit(self, account_number: str, money: int | str):
        if isinstance(money, float):
            raise NotIntError
        if isinstance(money, str):
            try:
                money = int(money)
            except ValueError:
                raise NotIntError

        if money == 0:
            raise ZeroDepositError
        elif money < 0:
            raise NegativeValueError

        current_balance = self.get_balance(account_number)
        current_balance += money
        self.repository.update_balance(account_number, current_balance)

    def withdraw(self, account_number: str, money: int | str):
        if isinstance(money, float):
            raise NotIntError
        if isinstance(money, str):
            try:
                money = int(money)
            except ValueError:
                raise NotIntError

        if money < 0:
            raise NegativeValueError

        current_balance = self.get_balance(account_number)
        if current_balance < money:
            raise NotEnoughBalanceError

        current_balance -= money
        self.repository.update_balance(account_number, current_balance)


class NoSuchAccountError(Exception):
    pass


class ZeroDepositError(Exception):
    pass


class NegativeValueError(Exception):
    pass


class NotIntError(Exception):
    pass


class NotEnoughBalanceError(Exception):
    pass
