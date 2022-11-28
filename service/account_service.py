from domain.account import Account
from repository.account_repository_memory import AccountRepositoryMemory


class AccountService:
    def __init__(self, account: Account | None) -> None:
        self.account = account
        self.repository = AccountRepositoryMemory()

    def create_account(self):
        pass

    def get_balance(self):
        pass

    def deposit(self):
        pass

    def withdraw(self):
        pass


class NoSuchElementError(Exception):
    pass


class EmptyValueError(Exception):
    pass


class WrongValueError(Exception):
    pass


class NegativeValueError(Exception):
    pass


class DecimalValueError(Exception):
    pass
