from domain.account import Account
from repository.account_repository_memory import AccountRepositoryMemory


class AccountService:
    def __init__(self) -> None:
        self.repository = AccountRepositoryMemory()

    def create_account(self) -> Account:
        account = self.repository.save(Account())
        return account

    def validate_account_number(self, account_number: str) -> bool:
        return Account.validate_account_number(account_number)

    def get_balance(self, account_number: str) -> int:
        if not account_number:
            raise NoSuchAccountError

        account = self.repository.find_by_account_number(account_number)
        if not account:
            raise NoSuchAccountError

        return account.balance

    def deposit(self, account_number: str, money: int):
        if money == 0:
            raise ZeroDepositError
        elif money < 0:
            raise NegativeValueError
        elif isinstance(money, float):
            raise DecimalValueError

        current_balance = self.get_balance(account_number)
        current_balance += money
        self.repository.update_balance(account_number, current_balance)

    def withdraw(self, account_number: str, money: int):
        if money < 0:
            raise NegativeValueError
        elif isinstance(money, float):
            raise DecimalValueError

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


class DecimalValueError(Exception):
    pass


class NotEnoughBalanceError(Exception):
    pass
