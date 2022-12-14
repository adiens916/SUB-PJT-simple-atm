from domain.account import Account
from .account_repository import (
    AccountRepository,
    DuplicateKeySaveError,
    NoSuchAccountError,
)


class AccountRepositoryMemory(AccountRepository):
    store = dict()

    def save(self, account: Account) -> Account:
        if self.store.get(account.account_number) != None:
            raise DuplicateKeySaveError

        self.store[account.account_number] = account
        return account

    def find_by_account_number(self, account_number: str) -> Account:
        account = self.store.get(account_number)
        if account:
            return account
        else:
            raise NoSuchAccountError

    def update_balance(self, account_number: str, balance: int) -> bool:
        account = self.find_by_account_number(account_number)
        if account:
            account.balance = balance
            self.store[account_number] = account
            return True
        else:
            return False
