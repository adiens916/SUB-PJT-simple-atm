from unittest import TestCase
from repository.account_repository_memory import AccountRepositoryMemory
from domain.account import Account


class AccountRepositoryMemoryTest(TestCase):
    repository = AccountRepositoryMemory()

    def test_save(self):
        account = Account()
        account.account_number = "123-456-7890"
        account.balance = 10000

        account_return = self.repository.save(account)
        self.assertIs(account_return.account_number, "123-456-7890")
        self.assertIs(account_return.balance, 10000)
