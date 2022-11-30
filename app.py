saved_account_number = ""
saved_card_number = ""


def main():
    while True:
        print()
        print("< Simple ATM >")

        print("You can select one of these.")
        print("- 1. See Balance")
        print("- 2. Deposit")
        print("- 3. Withdraw")
        print("- 4. Exit")

        command = input("Enter a command: ")
        check_auth()

        if command == "1":
            balance = ""
            print(f"Current Balance: {balance}")

        elif command == "2":
            deposit = int(input())

        elif command == "3":
            withdrawal = int(input())

        elif command == "4":
            break


def check_auth():
    global saved_account_number

    if not saved_account_number:
        print("Please enter your account number (including '-').")
        print("If you don't have one, then input 'new' for creating a new account.")
        print("Otherwise, you can return by input 'no'.")
        user_input = input(": ")

        if user_input.lower() == "new":
            print("Now your account has been created!")
            print("Your account number is", saved_account_number)


main()
