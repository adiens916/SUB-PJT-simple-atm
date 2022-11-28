from domain.account import Account
from repository.account_repository_memory import AccountRepositoryMemory


class AccountService:
    def __init__(self, account=None) -> None:
        if isinstance(account, Account):
            self.account = account
        self.repository = AccountRepositoryMemory()

    def create_account(self) -> Account:
        account = self.repository.save(Account())
        return account

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
