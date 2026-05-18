# WGC Arcade Prize Manager
# Phase 3/3
# Christina C

"""WGC Arcade Prize Manager."""

print("\n--- WGC Arcade Prize Manager ---")

# Starting ticket balance
ticket_balance = 200

# List of all prizes
prizes = [
    {"name": "Teddy Bear", "ticket_cost": 160, "current_stock": 40},
    {"name": "Fidget Toy", "ticket_cost": 40, "current_stock": 50},
    {"name": "Bouncy Ball", "ticket_cost": 5, "current_stock": 100},
    {"name": "Chocolate", "ticket_cost": 45, "current_stock": 75},
    {"name": "Keychain", "ticket_cost": 20, "current_stock": 60},
]


def display_prizes():
    """Display all the prizes."""
    print("\nPRIZES:")
    # Create table header with aligned columns using ljust()
    print(" | ".join(["Name".ljust(12), "Cost".ljust(6), "Stock"]))
    print("-" * 32)

    # Loops through each prize in the list
    for prize in prizes:
        # Formats each row so each value lines up neatly
        row = [
            prize["name"].ljust(12),
            str(prize["ticket_cost"]).ljust(6),
            str(prize["current_stock"])
        ]
        print(" | ".join(row))


def add_tickets(balance):
    """Add tickets to player's balance."""
    # Ask user how many tickets they want to add
    user_input = input("How many tickets would you like to add?: ")

    try:
        tickets = int(user_input)

        # Checks for positive number
        if tickets <= 0:
            print("Please enter a number greater than 0!")
            return balance

        # Add entered amount of tickets to balance
        balance += tickets

        print(f"{tickets} tickets added.")
        print(f"The New balance: {balance}")

        # Return updated balance to menu
        return balance

    except ValueError:
        print("That is not a number, please try again")
        return balance


def redeem_prize(balance):
    """Redeem prizes by subtracting the amount from users balance."""
    # Asks user which prize they want
    prize_name = input("Please enter prize name: ")

    # Search through prize list
    for prize in prizes:

        # Finds the prize, .lower() makes input case insensitive
        if prize["name"].lower() == prize_name.lower():

            # Check stock and prevents redeeming unavaliable prizes
            if prize["current_stock"] <= 0:
                print("sorry, the prize you have asked for is out of stock")
                return balance

            # Checks if user has enough tickets
            elif balance < prize["ticket_cost"]:
                print("You do not have enough tickets")
                return balance

            else:
                # Remove ticket cost from balance
                balance -= prize["ticket_cost"]

                # Reduce prize stock by 1 after redeeming the certain prize
                prize["current_stock"] -= 1

                print(f"You have redeemed {prize['name']}!")
                print(f"Remaining balance: {balance}")

                # Return updated balance
                return balance

    # This only runs if prize name does not exist
    print("Prize not found")
    return balance


def find_affordable_prizes(balance):
    """Find affordable prize(s) depending on how much user wants to spend."""
    while True:
        user_input = input("\nHow many tickets would you like to spend? ")

        try:
            amount = int(user_input)

            if amount < 0:
                print("Please enter a number bigger than 0")
                continue
            break

        except ValueError:
            print("Please enter a real whole number")

    for prize in prizes:

        if prize["ticket_cost"] <= amount and prize["current_stock"] > 0:
            print(f"{prize['name']} - {prize['ticket_cost']} tickets")


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
        print("4. Prize affordability")
        print("5. Redeem Prize")
        print("6. Exit")

        # Get user choice
        choice = input("Pick from 1-6: ")

        # Displays prize list if user selects 1
        if choice == "1":
            display_prizes()

        # Checks current balance
        elif choice == "2":
            print(f"\nYour current balance is: {ticket_balance}")

        # Add certain amount of tickets
        elif choice == "3":
            ticket_balance = add_tickets(ticket_balance)

        # Checks users balance for what prize they can afford
        elif choice == "4":
            find_affordable_prizes(ticket_balance)

        # Redeem certain prize
        elif choice == "5":
            ticket_balance = redeem_prize(ticket_balance)

        # Stop/exits the loop of the program if user picks 6
        elif choice == "6":
            print("Goodbye!")
            break

        # Handles invalid input
        else:
            print("This is an invalid choice. Please pick from 1-6")


# Start of the program
if __name__ == "__main__":
    menu()
