from repository.card_repository_memory import CardRepositoryMemory
from repository.card_repository import NoSuchCardError, DuplicateKeySaveError
from domain.card import Card
from domain.account import Account


class CardService:
    def __init__(self) -> None:
        self.repository = CardRepositoryMemory()

    def create_card(self, pin_number: str, linked_account_number=None) -> Card:
        if pin_number == None or pin_number == "":
            raise EmptyPinNumberError
        if len(pin_number) != 4 or not pin_number.isdigit():
            raise WrongPinNumberError

        card = Card(pin_number, linked_account_number)

        try:
            card_saved = self.repository.save(card)
            return card_saved
        except DuplicateKeySaveError:
            raise DuplicateKeySaveError

    def authenticate_card_by_pin(self, card_number: str, pin_number: str) -> bool:
        if pin_number == None or pin_number == "":
            raise EmptyPinNumberError
        if len(pin_number) != 4 or not pin_number.isdigit():
            raise WrongPinNumberError

        try:
            card = self.repository.find_by_card_number(card_number)
            return card.validate_pin_number(pin_number)
        except NoSuchCardError:
            raise NoSuchCardError

    def get_linked_account_number(self, card_number: str) -> str:
        if not Card.validate_card_number(card_number):
            raise WrongFormatError

        try:
            card = self.repository.find_by_card_number(card_number)
        except NoSuchCardError:
            raise NoSuchCardError

        if not card.linked_account_number:
            raise NoLinkedAccountError

        return card.linked_account_number

    def change_linked_account_number(self, card_number: str, account_number: str):
        result = Account.validate_account_number(account_number)
        if not result:
            raise WrongFormatError

        try:
            card = self.repository.find_by_card_number(card_number)
        except NoSuchCardError:
            raise NoSuchCardError

        card.linked_account_number = account_number
        self.repository.update_linked_account_number(card_number, account_number)


class NoLinkedAccountError(Exception):
    pass


class EmptyPinNumberError(Exception):
    pass


class WrongPinNumberError(Exception):
    pass


class WrongFormatError(Exception):
    pass
