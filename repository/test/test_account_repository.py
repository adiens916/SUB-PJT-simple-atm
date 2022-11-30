from unittest import TestCase
from repository.account_repository_memory import AccountRepositoryMemory
from repository.account_repository import DuplicateKeyError
from domain.account import Account


class AccountRepositoryTest(TestCase):
    repository = AccountRepositoryMemory()

    def setUp(self) -> None:
        account = Account()
        account.account_number = "123-456-7890"
        account.balance = 10000
        self.account = account

    def tearDown(self) -> None:
        self.repository.store.clear()

    def test_save(self):
        account_return = self.repository.save(self.account)
        self.assertIs(account_return.account_number, "123-456-7890")
        self.assertIs(account_return.balance, 10000)

    def test_failed_save_by_duplicate_key(self):
        self.repository.save(self.account)
        with self.assertRaises(DuplicateKeyError):
            self.repository.save(self.account)

    def test_find_by_account_number(self):
        self.repository.save(self.account)
        account = self.repository.find_by_account_number("123-456-7890")
        self.assertEqual(account.account_number, self.account.account_number)

    def test_update_balance(self):
        self.repository.save(self.account)
        account = self.repository.find_by_account_number(self.account.account_number)
        self.assertEqual(account.balance, 10000)

        account.balance += 20000
        self.repository.update_balance(self.account.account_number, account.balance)

        account = self.repository.find_by_account_number(self.account.account_number)
        self.assertEqual(account.balance, 30000)
