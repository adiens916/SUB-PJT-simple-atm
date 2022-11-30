from unittest import TestCase
from service.card_service import CardService
from service.card_service import NoSuchElementError, EmptyValueError, WrongValueError
from domain.card import Card


class CardServiceTest(TestCase):
    card_service = CardService()

    def setUp(self) -> None:
        self.pin_number = "9173"
        self.account_number = "102-301-7523"

    def tearDown(self) -> None:
        self.card_service.repository.store.clear()

    def test_create_card(self):
        card = self.card_service.create_card(self.pin_number, self.account_number)
        validity = Card.validate_card_number(card.card_number)
        self.assertTrue(validity)

    def test_failed_create_card_by_empty_pin_number(self):
        with self.assertRaises(EmptyValueError):
            card = self.card_service.create_card(None, self.account_number)
            card = self.card_service.create_card("", self.account_number)

    def test_failed_create_card_by_wrong_pin_number(self):
        with self.assertRaises(WrongValueError):
            card_short = self.card_service.create_card("324", self.account_number)
            card_long = self.card_service.create_card("32457", self.account_number)

    def test_authenticate_card_by_pin(self):
        pass

    def test_get_linked_account_number(self):
        pass

    def test_failed_get_linked_account_number_by_empty_account(self):
        pass

    def test_change_linked_account_number(self):
        pass
