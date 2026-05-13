# WGC Arcade Prize Manager
# Phase 1/3
# Christina C

"""WGC Arcade Prize Manager."""

print("\n--- WGC Arcade Prize Manager ---")
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
    # ljust() is used to left justify a string within a specified width
    # example:
    # fruit = "apple"
    # x = fruit.ljust(10)
    # print(x, "is my favorite fruit.")
    #
    # output:
    # apple      is my favorite fruit.

    # Create table header with aligned colums using ljust()
    print(" | ".join(["Name".ljust(12), "Cost".ljust(6), "Stock"]))
    print("-" * 32)

    # Loops through each prize in the list
    for prize in prizes:
        # Formats each row so each value lines up neatly
        row = [
            prize["Name"].ljust(12),
            # Without str() the programme will fail
            # Convert numvers to strings so ljust() can be used
            str(prize["Ticket Cost"]).ljust(6),
            str(prize["Current Stock"])
        ]
        print(" | ".join(row))


def menu():
    """Display menu screen."""
    # while True loop will run forever if condition is always true
    # Infinite loop keeps menu running until user chooses to exit
    while True:
        print("\n1. Prizes")
        print("2. Exit")

        # Get user choice
        choice = input("Pick 1 or 2: ")

        # Displays prize list if user selects 1
        if choice == "1":
            display_prizes()

        # Stop/exits the loop of the program if user selects 2
        elif choice == "2":
            print("Goodbye")
            break

        # Handles invalid input
        else:
            print("This is an invalid choice. Please pick either 1 or 2")

# Start of the program
menu()
