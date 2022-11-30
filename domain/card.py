import random


class Card:
    def __init__(self, pin_number: str, linked_account_number=None) -> None:
        self.card_number = self.make_card_number()
        self.hashed_pin_number = self.get_hashed_pin_number(pin_number)

        if isinstance(linked_account_number, str):
            self.linked_account_number = linked_account_number
        else:
            self.linked_account_number = ""

    def make_card_number(self) -> str:
        num_strings = list(map(str, range(10)))
        generate_random_num_string = lambda size: "".join(
            random.choices(num_strings, k=size)
        )

        card_number_parts = [generate_random_num_string(4) for _ in range(4)]
        return "-".join(card_number_parts)

    def get_hashed_pin_number(self, pin_number: str) -> str:
        pass

    @staticmethod
    def validate_card_number(card_number: str) -> bool:
        if not isinstance(card_number, str):
            return False

        parts = card_number.split("-")
        if len(parts) != 4:
            return False

        for i in range(4):
            if len(parts[i]) != 4:
                return False
            for num in parts[i]:
                if not num.isdigit():
                    return False

        return True
