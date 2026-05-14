# WGC Arcade Prize Manager
# Phase 2/3
# Christina C

"""WGC Arcade Prize Manager."""

print("\n--- WGC Arcade Prize Manager ---")

# Starting ticket balance
ticket_balance = 200

# List of all prizes
prizes = [
    {"Name": "Teddy Bear", "Ticket Cost": 160, "Current Stock": 40},
    {"Name": "Fidget Toy", "Ticket Cost": 40, "Current Stock": 50},
    {"Name": "Bouncy Ball", "Ticket Cost": 5, "Current Stock": 100},
    {"Name": "Chocolate", "Ticket Cost": 45, "Current Stock": 75},
    {"Name": "Keychain", "Ticket Cost": 20, "Current Stock": 60},
]


def display_prizes():
    """Display all the prizes."""
    print("\nPRIZES:")
    # Create table header with aligned colums using ljust()
    print(" | ".join(["Name".ljust(12), "Cost".ljust(6), "Stock"]))
    print("-" * 32)

    # Loops through each prize in the list
    for prize in prizes:
        # Formats each row so each value lines up neatly
        row = [
            prize["Name"].ljust(12),
            str(prize["Ticket Cost"]).ljust(6),
            str(prize["Current Stock"])
        ]
        print(" | ".join(row))


def add_tickets(balance):
    """Add tickets to player's balance."""
    tickets = int(input("How many tickets would you like to add?: "))

    # Add chosen amount of tickets to balance
    balance += tickets

    print(f"{tickets} tickets added.")
    print(f"The New balance: {balance}")

    # Calls
    return balance


def redeem_prize(balance):
    """Redeem prizes by subtracting the amount from users balance"""


def menu():
    """Display menu screen."""
    # while True loop will run forever if condition is always true
    # Infinite loop keeps menu running until user chooses to exit
    while True:
        # Choices
        print("\n1. Prizes")
        print("2. Display Balance")
        print("3. Add Tickets")
        print("4. Redeem Prize")
        print("5. Exit")

        # Get user choice
        choice = input("Pick from 1-5: ")

        # Displays prize list if user selects 1
        if choice == "1":
            display_prizes()

        elif choice == "2":
            print(f"\nYour current ticket balance is: {ticket_balance}")

        # elif choice == "3":

        # elif choice == "4":

        # Stop/exits the loop of the program if user picks 5
        elif choice == "5":
            print("Goodbye!")
            break

        # Handles invalid input
        else:
            print("This is an invalid choice. Please pick from 1-5")


# Start of the program
if __name__ == "__main__":
    menu()
