from .card_repository import CardRepository
from domain.card import Card


class CardRepositoryMemory(CardRepository):
    store = dict()

    def save(self, card: Card) -> Card:
        self.store[card.card_number] = card
        return card

    def find_by_card_number(self, card_number: str) -> Card | None:
        card = self.store.get(card_number)
        if card:
            return card
        else:
            print("The card is not found.")
            return None
