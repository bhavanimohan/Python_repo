accounts = {
    "1234": {"name": "Ravi", "balance": 5000},
    "5678": {"name": "Meena", "balance": 12000},
    "9999": {"name": "Arjun", "balance": 800}
}

chances = 3


class InsufficientFundsError(Exception):
    pass


class Rejected(Exception):
    pass


while chances > 0:

    try:
        pin = input("Enter the pin : ")

        # Check PIN
        account = accounts[pin]

        amount = int(input("Enter the amount : "))

        # Check amount
        if amount <= 0:
            raise Rejected("Amount must be greater than zero.")

        # Check balance
        if amount > account["balance"]:
            raise InsufficientFundsError("Insufficient Funds!!!")

        # Withdraw
        account["balance"] -= amount

        name = account["name"]
        remaining_amount = account["balance"]

    except KeyError:
        print("Invalid PIN. Account not found.")

    except ValueError:
        print("Please enter a valid amount!!!")

    except InsufficientFundsError as e:
        print(e)

    except Rejected as e:
        print(e)

    except Exception as e:
        print(f"Transaction Failed: {e}")

    else:
        print("Withdrawal Successful!!!")
        print(
            f"Name: {name}, "
            f"Amount: {amount}, "
            f"Remaining Amount: {remaining_amount}"
        )

    finally:
        print("Transaction Session Ended.")

    chances -= 1