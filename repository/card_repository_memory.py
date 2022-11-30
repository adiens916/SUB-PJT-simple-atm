from .card_repository import CardRepository, DuplicateKeyError
from domain.card import Card


class CardRepositoryMemory(CardRepository):
    store = dict()

    def save(self, card: Card) -> Card:
        if self.store.get(card.card_number) != None:
            raise DuplicateKeyError

        self.store[card.card_number] = card
        return card

    def find_by_card_number(self, card_number: str) -> Card | None:
        card = self.store.get(card_number)
        if card:
            return card
        else:
            print("The card is not found.")
            return None

    def update_linked_account_number(self, card_number: str, account_number: str):
        pass
