import random


class Account:
    def __init__(self) -> None:
        self.account_number = self.make_account_number()
        self.balance = 0

    def make_account_number(self):
        num_strings = list(map(str, range(10)))
        front = "".join(random.choices(num_strings, k=3))
        middle = "".join(random.choices(num_strings, k=3))
        back = "".join(random.choices(num_strings, k=4))
        return f"{front}-{middle}-{back}"

    def is_valid_account_number(self):
        if not isinstance(self.account_number, str):
            return False

        parts = self.account_number.split("-")
        if len(parts) != 3:
            return False

        lengths = [3, 3, 4]
        for i in range(3):
            if len(parts[i]) != lengths[i]:
                return False
            for num in parts[i]:
                if not num.isdigit():
                    return False

        return True
