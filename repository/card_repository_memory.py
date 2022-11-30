from .card_repository import CardRepository, DuplicateKeyError, NoSuchElementError
from domain.card import Card


class CardRepositoryMemory(CardRepository):
    store = dict()

    def save(self, card: Card) -> Card:
        if self.store.get(card.card_number) != None:
            raise DuplicateKeyError

        self.store[card.card_number] = card
        return card

    def find_by_card_number(self, card_number: str) -> Card:
        card = self.store.get(card_number)
        if card:
            return card
        else:
            raise NoSuchElementError

    def update_linked_account_number(self, card_number: str, account_number: str):
        card = self.find_by_card_number(card_number)
        card.linked_account_number = account_number
        self.store[card.card_number] = card
