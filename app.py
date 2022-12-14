from controller.controller import AtmController, BankController

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

    while True:
        account_number = bank_controller.create_account().get("data")
        if account_number:
            break

    while True:
        response = bank_controller.create_card(pin_number, account_number)
        saved_card_number = response.get("data")
        if saved_card_number:
            break

    print("All works done! Now you can use this ATM.\n")


def insert_pin():
    available_input_count = 5

    while True:
        print("Please enter your PIN number.")
        pin_number = input(": ").strip()

        response = bank_controller.authenticate_card_by_pin(
            saved_card_number, pin_number
        )
        if response.get("ok") == "false":
            continue

        is_pin_correct = response.get("data")
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
            response = atm_controller.get_linked_account_number(saved_card_number)
            if response.get("ok") == "false":
                print(response)
                continue
            account = response.get("data")

            response = atm_controller.get_balance(account)
            if response.get("ok") == "false":
                print(response)
                continue

            balance = response.get("data")
            print(f"Current Balance: {balance}")

        elif command == "2":
            print("Enter amount for deposit")
            deposit = input(": ")

            response = atm_controller.get_linked_account_number(saved_card_number)
            if response.get("ok") == "false":
                print(response)
                continue
            account = response.get("data")

            response = atm_controller.deposit(account, deposit)
            if response.get("ok") == "false":
                print(response)
                continue
            updated_balance = response.get("data")

            print(f"Current Balance: {updated_balance}")

        elif command == "3":
            print("Enter amount for withdrawal")
            debit = input(": ")

            response = atm_controller.get_linked_account_number(saved_card_number)
            if response.get("ok") == "false":
                print(response)
                continue
            account = response.get("data")

            response = atm_controller.withdraw(account, debit)
            if response.get("ok") == "false":
                print(response)
                continue
            updated_balance = response.get("data")

            print(f"Current Balance: {updated_balance}")

        elif command == "4":
            return


def is_valid_pin_number(pin_number) -> bool:
    return isinstance(pin_number, str) and len(pin_number) == 4


main()
