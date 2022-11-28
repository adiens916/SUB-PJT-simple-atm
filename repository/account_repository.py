import abc
from domain.account import Account


class AccountRepository:
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def save(self, account: Account) -> Account:
        pass

    @abc.abstractmethod
    def find_by_account_number(self, account_number: str) -> Account | None:
        pass

    @abc.abstractmethod
    def update_balance(self, account_number: str, balance: int) -> bool:
        pass
