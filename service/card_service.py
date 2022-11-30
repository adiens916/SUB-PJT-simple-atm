from repository.card_repository_memory import CardRepositoryMemory
from domain.card import Card


class CardService:
    def __init__(self) -> None:
        self.repository = CardRepositoryMemory()

    def create_card(self, pin_number: str, linked_account_number=None) -> Card:
        if pin_number == None or pin_number == "":
            raise EmptyValueError
        if len(pin_number) != 4 or not pin_number.isdigit():
            raise WrongValueError

        card = Card(pin_number, linked_account_number)
        card_saved = self.repository.save(card)
        return card_saved

    def authenticate_card_by_pin(self, card_number: str, pin_number: str) -> bool:
        if pin_number == None or pin_number == "":
            raise EmptyValueError
        if len(pin_number) != 4 or not pin_number.isdigit():
            raise WrongValueError

        card = self.repository.find_by_card_number(card_number)
        return card.validate_pin_number(pin_number)

    def get_linked_account_number(self, card_number: str) -> str:
        pass

    def change_linked_account_number(self, card_number: str, account_number: str):
        pass


class NoSuchElementError(Exception):
    pass


class EmptyValueError(Exception):
    pass


class WrongValueError(Exception):
    pass
