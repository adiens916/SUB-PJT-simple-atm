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
        account = self.account_service.create_account()
        balance = self.account_service.get_balance(account.account_number)
        self.assertIsInstance(balance, int)

    def test_failed_get_balance_by_null_account(self):
        with self.assertRaises(NoSuchElementError):
            balance = self.account_service.get_balance("")

    def test_deposit(self):
        account = self.account_service.create_account()
        self.account_service.deposit(account.account_number, 50000)
        new_balance = self.account_service.get_balance(account.account_number)
        self.assertEqual(new_balance, 50000)

        self.account_service.deposit(account.account_number, 30000)
        new_balance = self.account_service.get_balance(account.account_number)
        self.assertEqual(new_balance, 80000)

    def test_failed_deposit_by_null_account(self):
        account_number = ""
        with self.assertRaises(NoSuchElementError):
            self.account_service.deposit(account_number, 10000)

    def test_failed_deposit_by_zero_input(self):
        account = self.account_service.create_account()
        with self.assertRaises(EmptyValueError):
            self.account_service.deposit(account.account_number, 0)

    def test_failed_deposit_by_negative_input(self):
        account = self.account_service.create_account()
        with self.assertRaises(NegativeValueError):
            self.account_service.deposit(account.account_number, -10000)

    def test_failed_deposit_by_decimal_input(self):
        account = self.account_service.create_account()
        with self.assertRaises(DecimalValueError):
            self.account_service.deposit(account.account_number, 5.5)

    def test_withdraw(self):
        pass


"""
class AccountServiceTest(TestCase):
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
