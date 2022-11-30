from abc import ABCMeta, abstractmethod
from domain.card import Card


class CardRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, card: Card) -> Card:
        pass

    @abstractmethod
    def find_by_card_number(self, card_number: str) -> Card | None:
        pass

    @abstractmethod
    def update_linked_account_number(self, card_number: str, account_number: str):
        pass


class DuplicateKeyError(Exception):
    pass


class NoSuchElementError(Exception):
    pass
