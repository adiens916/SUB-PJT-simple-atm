from .card_repository import (
    CardRepository,
    DuplicateKeySaveError,
    NoSuchCardError,
)
from domain.card import Card


class CardRepositoryMemory(CardRepository):
    store = dict()

    def save(self, card: Card) -> Card:
        if self.store.get(card.card_number) != None:
            raise DuplicateKeySaveError

        self.store[card.card_number] = card
        return card

    def find_by_card_number(self, card_number: str) -> Card:
        card = self.store.get(card_number)
        if card:
            return card
        else:
            raise NoSuchCardError

    def update_linked_account_number(self, card_number: str, account_number: str):
        card = self.find_by_card_number(card_number)
        card.linked_account_number = account_number
        self.store[card.card_number] = card
