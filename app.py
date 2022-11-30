from controller.atm_controller import AtmController, BankController

atm_controller = AtmController()
bank_controller = BankController()

saved_card_number = ""


def main():
    print("< Simple ATM >\n")

    prep_account_and_card()
    authenticate_pin()

    while True:
        print()
        print("You can select one of these.")
        print("- 1. See Balance")
        print("- 2. Deposit")
        print("- 3. Withdraw")
        print("- 4. Exit")

        command = input("Enter a command: ").strip()

        if command == "1":
            balance = ""
            print(f"Current Balance: {balance}")

        elif command == "2":
            deposit = int(input())

        elif command == "3":
            withdrawal = int(input())

        elif command == "4":
            break


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


def authenticate_pin():
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


def is_valid_pin_number(pin_number) -> bool:
    return isinstance(pin_number, str) and len(pin_number) == 4


main()
