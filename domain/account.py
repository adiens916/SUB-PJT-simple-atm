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
