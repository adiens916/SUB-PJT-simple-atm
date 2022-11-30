from unittest import TestCase
from repository.card_repository_memory import CardRepositoryMemory
from domain.card import Card

SAMPLE_CARD_NUMBER = "1234-5678-9012-3456"
SAMPLE_PIN_NUMBER = "1234"
SAMPLE_ACCOUNT_NUMBER = "123-456-7890"


class CardRepositoryTest(TestCase):
    repository = CardRepositoryMemory()

    def setUp(self) -> None:
        card = Card()
        card.card_number = SAMPLE_CARD_NUMBER
        card.pin_number = SAMPLE_PIN_NUMBER
        card.linked_account_number = SAMPLE_ACCOUNT_NUMBER
        self.card = card

    def tearDown(self) -> None:
        self.repository.store.clear()

    def test_save(self):
        card_return = self.repository.save(self.card)
        self.assertIs(card_return.card_number, SAMPLE_CARD_NUMBER)
        self.assertIs(card_return.pin_number, SAMPLE_PIN_NUMBER)

    def test_find_by_card_number(self):
        self.repository.save(self.card)
        card = self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)
        self.assertEqual(card.card_number, self.card.card_number)
