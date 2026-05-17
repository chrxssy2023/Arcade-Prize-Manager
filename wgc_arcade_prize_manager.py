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
    # Ask user how many tickets they want to add
    tickets = int(input("How many tickets would you like to add?: "))

    # Add entered amount of tickets to balance
    balance += tickets

    print(f"{tickets} tickets added.")
    print(f"The New balance: {balance}")

    # Return updated balance to menu
    return balance


def redeem_prize(balance):
    """Redeem prizes by subtracting the amount from users balance."""
    # Asks user which prize they want
    prize_name = input("Please enter prize name: ")

    # Search through prize list
    for prize in prizes:

        # Finds the prize, .lower() makes input case insensitive
        if prize["Name"].lower() == prize_name.lower():

            # Check stock and prevents redeeming unavaliable prizes
            if prize["Current Stock"] <= 0:
                print("sorry, the prize you have asked for is out of stock")
                return balance

            # Checks if user has enough tickets
            elif balance < prize["Ticket Cost"]:
                print("You do not have enough tickets")
                return balance

            else:
                # Remove ticket cost from balance
                balance -= prize["Ticket Cost"]

                # Reduce prize stock by 1 after redeeming the certain prize
                prize["Current Stock"] -= 1

                print(f"You have redeemed {prize['Name']}!")
                print(f"Remaining balance: {balance}")

                # Return updated balance
                return balance

    # This only runs if prize name does not exist
    print("Prize not found")
    return balance


def menu():
    """Display menu screen."""
    # Allows function to update ticket balance variable outside the function
    global ticket_balance

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

        # Checks current balance
        elif choice == "2":
            print(f"\nYour current balance is: {ticket_balance}")

        # Add certain amount of tickets
        elif choice == "3":
            ticket_balance = add_tickets(ticket_balance)

        # Redeem certain prize
        elif choice == "4":
            ticket_balance = redeem_prize(ticket_balance)

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
