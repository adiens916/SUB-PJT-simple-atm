from unittest import TestCase
from service.card_service import CardService
from service.card_service import NoSuchElementError, EmptyValueError, WrongValueError
from domain.card import Card


class CardServiceTest(TestCase):
    card_service = CardService()

    def setUp(self) -> None:
        self.pin_number = "9173"
        self.account_number = "102-301-7523"

    def test_create_card(self):
        card = self.card_service.create_card(self.pin_number, self.account_number)
        validity = Card.validate_card_number(card.card_number)
        self.assertTrue(validity)

    def test_authenticate_card_by_pin(self):
        pass

    def test_get_linked_account_number(self):
        pass

    def test_failed_get_linked_account_number_by_empty_account(self):
        pass

    def test_change_linked_account_number(self):
        pass
