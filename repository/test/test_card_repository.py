from unittest import TestCase
from repository.card_repository_memory import CardRepositoryMemory
from repository.card_repository import (
    DuplicateKeySaveError,
    NoSuchCardError,
)
from domain.card import Card

SAMPLE_CARD_NUMBER = "1234-5678-9012-3456"
SAMPLE_PIN_NUMBER = "1234"
SAMPLE_ACCOUNT_NUMBER = "012-345-6789"


class CardRepositoryTest(TestCase):
    repository = CardRepositoryMemory()

    def setUp(self) -> None:
        card = Card(pin_number=SAMPLE_PIN_NUMBER)
        self.card = card

    def tearDown(self) -> None:
        self.repository.store.clear()

    def test_save(self):
        card_return = self.repository.save(self.card)
        self.assertIsNotNone(card_return)
        self.assertIsNot(card_return.card_number, "")
        self.assertIsNot(card_return.card_number, None)
        self.assertIsNotNone(card_return.hashed_pin_number)
        self.assertGreater(len(card_return.hashed_pin_number), 0)

    def test_failed_save_by_same_card_number(self):
        self.repository.save(self.card)
        with self.assertRaises(DuplicateKeySaveError):
            self.repository.save(self.card)

    def test_find_by_card_number(self):
        card = Card(SAMPLE_PIN_NUMBER)
        card.card_number = SAMPLE_CARD_NUMBER
        self.repository.save(card)

        card_ret = self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)
        self.assertEqual(card.card_number, card_ret.card_number)

    def test_failed_find_by_card_number_by_non_existent_card(self):
        with self.assertRaises(NoSuchCardError):
            self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)

    def test_update_linked_account_number(self):
        card = Card(SAMPLE_PIN_NUMBER)
        card.card_number = SAMPLE_CARD_NUMBER
        self.repository.save(card)

        card_saved = self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)
        self.repository.update_linked_account_number(
            card_saved.card_number, SAMPLE_ACCOUNT_NUMBER
        )

        card_saved = self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)
        self.assertEqual(card_saved.linked_account_number, SAMPLE_ACCOUNT_NUMBER)
