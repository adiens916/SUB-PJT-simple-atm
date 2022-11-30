class Card:
    def __init__(self, pin_number: str, linked_account_number=None) -> None:
        self.card_number = self.assign_card_number()
        self.hashed_pin_number = self.get_hashed_pin_number(pin_number)

        if isinstance(linked_account_number, str):
            self.linked_account_number = linked_account_number
        else:
            self.linked_account_number = ""

    def assign_card_number(self) -> str:
        pass

    def validate_card_number(self, card_number: str) -> bool:
        pass

    def get_hashed_pin_number(self, pin_number: str) -> str:
        pass
