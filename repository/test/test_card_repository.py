from unittest import TestCase
from repository.card_repository_memory import CardRepositoryMemory
from domain.card import Card

SAMPLE_CARD_NUMBER = "1234-5678-9012-3456"
SAMPLE_PIN_NUMBER = "1234"


class CardRepositoryTest(TestCase):
    repository = CardRepositoryMemory()

    def setUp(self) -> None:
        card = Card(pin_number=SAMPLE_PIN_NUMBER)
        self.card = card

    def tearDown(self) -> None:
        self.repository.store.clear()

    def test_save(self):
        card_return = self.repository.save(self.card)

        card_number_validity = Card.validate_card_number(card_return.card_number)
        self.assertTrue(card_number_validity)

        self.assertIsNotNone(card_return.hashed_pin_number)
        self.assertGreater(len(card_return.hashed_pin_number), 0)

    def test_find_by_card_number(self):
        card = Card(SAMPLE_PIN_NUMBER)
        card.card_number = SAMPLE_CARD_NUMBER
        self.repository.save(card)

        card_ret = self.repository.find_by_card_number(SAMPLE_CARD_NUMBER)
        self.assertEqual(card.card_number, card_ret.card_number)
