from unittest import TestCase
from service.card_service import CardService
from service.card_service import NoSuchElementError, EmptyValueError, WrongValueError
from domain.card import Card

SAMPLE_PIN_NUMBER = "9173"
SAMPLE_ACCOUNT_NUMBER = "102-301-7523"
NEW_SAMPLE_ACCOUNT_NUMBER = "101-320-3518"


class CardServiceTest(TestCase):
    card_service = CardService()

    def tearDown(self) -> None:
        self.card_service.repository.store.clear()

    def test_create_card(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER, SAMPLE_ACCOUNT_NUMBER)
        validity = Card.validate_card_number(card.card_number)
        self.assertTrue(validity)

    def test_failed_create_card_by_empty_pin_number(self):
        with self.assertRaises(EmptyValueError):
            card = self.card_service.create_card(None, SAMPLE_ACCOUNT_NUMBER)
            card = self.card_service.create_card("", SAMPLE_ACCOUNT_NUMBER)

    def test_failed_create_card_by_wrong_pin_number(self):
        with self.assertRaises(WrongValueError):
            card_short = self.card_service.create_card("324", SAMPLE_ACCOUNT_NUMBER)
            card_long = self.card_service.create_card("32457", SAMPLE_ACCOUNT_NUMBER)

    def test_authenticate_card_by_pin(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)
        result = self.card_service.authenticate_card_by_pin(
            card.card_number, SAMPLE_PIN_NUMBER
        )
        self.assertTrue(result)

    def test_failed_authenticate_card_by_pin_by_wrong_pin(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)
        result = self.card_service.authenticate_card_by_pin(card.card_number, "0000")
        self.assertFalse(result)

    def test_failed_authenticate_card_by_pin_by_empty_pin(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)

        with self.assertRaises(EmptyValueError):
            result = self.card_service.authenticate_card_by_pin(card.card_number, None)

        with self.assertRaises(EmptyValueError):
            result = self.card_service.authenticate_card_by_pin(card.card_number, "")

    def test_failed_authenticate_card_by_pin_by_wrong_format(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)

        with self.assertRaises(WrongValueError):
            result = self.card_service.authenticate_card_by_pin(card.card_number, "123")

    def test_get_linked_account_number(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER, SAMPLE_ACCOUNT_NUMBER)
        account = self.card_service.get_linked_account_number(card.card_number)
        self.assertEqual(account, SAMPLE_ACCOUNT_NUMBER)

    def test_failed_get_linked_account_number_by_empty_account(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)
        with self.assertRaises(NoSuchElementError):
            self.card_service.get_linked_account_number(card.card_number)

    def test_failed_get_linked_account_number_by_empty_card(self):
        with self.assertRaises(WrongValueError):
            self.card_service.get_linked_account_number(None)
            self.card_service.get_linked_account_number("")

    def test_change_linked_account_number(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER, SAMPLE_ACCOUNT_NUMBER)
        self.card_service.change_linked_account_number(
            card.card_number, NEW_SAMPLE_ACCOUNT_NUMBER
        )

        card_changed = self.card_service.repository.find_by_card_number(
            card.card_number
        )
        self.assertEqual(card_changed.linked_account_number, NEW_SAMPLE_ACCOUNT_NUMBER)

    def test_change_linked_account_number_by_empty_account(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER)
        self.card_service.change_linked_account_number(
            card.card_number, NEW_SAMPLE_ACCOUNT_NUMBER
        )

        card_changed = self.card_service.repository.find_by_card_number(
            card.card_number
        )
        self.assertEqual(card_changed.linked_account_number, NEW_SAMPLE_ACCOUNT_NUMBER)

    def test_failed_change_linked_account_number_by_wrong_account(self):
        card = self.card_service.create_card(SAMPLE_PIN_NUMBER, SAMPLE_ACCOUNT_NUMBER)

        with self.assertRaises(WrongValueError):
            self.card_service.change_linked_account_number(
                card.card_number, "1111111111"
            )

    def test_failed_change_linked_account_number_by_not_owned_account(self):
        pass
