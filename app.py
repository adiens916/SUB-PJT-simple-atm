from controller.atm_controller import AtmController, BankController

atm_controller = AtmController()
bank_controller = BankController()

saved_card_number = ""


def main():
    print("< Simple ATM >\n")

    prep_account_and_card()
    insert_pin()
    execute_command()


def prep_account_and_card():
    global saved_card_number

    print("First, you need a card to use this ATM.")
    while True:
        print("Please input a 4-digit PIN number for the card (Ex.: 2573)")
        pin_number = input(": ").strip()
        if is_valid_pin_number(pin_number):
            break

    account_number = bank_controller.create_account().get("data")
    saved_card_number = bank_controller.create_card(pin_number, account_number).get(
        "data"
    )

    print("All works done! Now you can use this ATM.\n")


def insert_pin():
    available_input_count = 5

    while True:
        print("Please enter your PIN number.")
        pin_number = input(": ").strip()

        if not is_valid_pin_number(pin_number):
            continue

        is_pin_correct = bank_controller.authenticate_card_by_pin(
            saved_card_number, pin_number
        ).get("data")

        if is_pin_correct:
            return

        if available_input_count:
            print(
                "Different PIN number... Please retry.", f"({available_input_count}/5)"
            )
            available_input_count -= 1
        else:
            print("You have used up all input chances. Please contact a nearby bank.")
            exit()


def execute_command():
    while True:
        print()
        print("You can do one of these.")
        print("- 1. See Balance")
        print("- 2. Deposit")
        print("- 3. Withdraw")
        print("- 4. Exit")

        command = input("Enter a command number (1 ~ 4): ").strip()

        if command == "1":
            account = atm_controller.get_linked_account_number(saved_card_number).get(
                "data"
            )
            balance = atm_controller.get_balance(account).get("data")
            print(f"Current Balance: {balance}")

        elif command == "2":
            print("Enter amount for deposit")
            deposit = int(input(": "))

            account = atm_controller.get_linked_account_number(saved_card_number).get(
                "data"
            )
            updated_balance = atm_controller.deposit(account, deposit).get("data")
            print(f"Current Balance: {updated_balance}")

        elif command == "3":
            print("Enter amount for withdrawal")
            debit = int(input(": "))

            account = atm_controller.get_linked_account_number(saved_card_number).get(
                "data"
            )
            updated_balance = atm_controller.withdraw(account, debit).get("data")
            print(f"Current Balance: {updated_balance}")

        elif command == "4":
            return


def is_valid_pin_number(pin_number) -> bool:
    return isinstance(pin_number, str) and len(pin_number) == 4


main()
