from abc import ABCMeta, abstractmethod
from domain.card import Card


class CardRepository(metaclass=ABCMeta):
    @abstractmethod
    def save(self, card: Card) -> Card:
        pass

    @abstractmethod
    def find_by_card_number(self, card_number: str) -> Card | None:
        pass


class DuplicateKeyError(Exception):
    pass
