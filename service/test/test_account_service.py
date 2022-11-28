from unittest import TestCase
from service.account_service import AccountService
from service.account_service import (
    NoSuchElementError,
    EmptyValueError,
    WrongValueError,
    NegativeValueError,
    DecimalValueError,
)
from domain.account import Account


class AccountServiceTest(TestCase):
    account_service = AccountService()

    def test_create_account(self):
        account: Account = self.account_service.create_account()

        self.assertIsInstance(account, Account)
        self.assertIsNotNone(account.account_number)
        self.assertIsNot(account.account_number, "")
        print(account.account_number)

    def test_validate_account_number(self):
        account: Account = self.account_service.create_account()
        result = self.account_service.validate_account_number(account)
        self.assertTrue(result)

    def test_failed_validate_account_number_by_short_number(self):
        account = Account()
        account.account_number = "123-456-78"
        result = self.account_service.validate_account_number(account)
        self.assertFalse(result)

    def test_failed_validate_account_number_by_empty_number(self):
        account = Account()
        account.account_number = ""
        result = self.account_service.validate_account_number(account)
        self.assertFalse(result)

    def test_failed_validate_account_number_by_null_number(self):
        account = Account()
        account.account_number = None
        result = self.account_service.validate_account_number(account)
        self.assertFalse(result)

    def test_get_balance(self):
        pass

    def test_deposit(self):
        pass

    def test_withdraw(self):
        pass


"""
class AccountServiceTest(TestCase):
    def test_failed_find_by_account_number_by_no_such_account(self):
        self.repository.save(self.account)
        with self.assertRaises(NoSuchElementError):
            account = self.repository.find_by_account_number("000-000-0000")

    def test_failed_update_balance_by_negative_value(self):
        self.repository.save(self.account)
        with self.assertRaises(NegativeValueError):
            self.repository.update_balance(self.account.account_number, -30000)

    def test_failed_update_balance_by_decimal_value(self):
        self.repository.save(self.account)
        new_balance = self.account.balance + 2.5
        with self.assertRaises(DecimalValueError):
            self.repository.update_balance(self.account.account_number, new_balance)
"""
