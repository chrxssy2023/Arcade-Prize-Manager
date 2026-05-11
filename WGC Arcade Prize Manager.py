# WGC Arcade Prize Manager
# Phase 1/3
# Christina C

"""WGC Arcade Prize Manager."""
prizes = [
    {"Name": "Teddy Bear", "Ticket Cost": 160, "Current Stock": 40},
    {"Name": "Fidget Toy", "Ticket Cost": 40, "Current Stock": 50},
    {"Name": "Bouncy Ball", "Ticket Cost": 5, "Current Stock": 100},
    {"Name": "Chocolate", "Ticket Cost": 45, "Current Stock": 75},
    {"Name": "Keychain", "Ticket Cost": 20, "Current Stock": 60},
    ]

while True:
    print("\n1. Prizes")
    print("2. Exit")
    choice = input("Pick 1 or 2: ")

    if choice == "1":
        print("\nPRIZES:")
        print(" | ".join(["Name".ljust(12), "Cost".ljust(4), "Stock"]))
        print("-" * 30)

        for prize in prizes:
            row = [
                prize["Name"].ljust(12),
                str(prize["Ticket Cost"]).ljust(4),
                str(prize["Current Stock"])
            ]

            print(" | ".join(row))

    elif choice == "2":
        print("Goodbye")
        break

    else:
        print("This is a invalid choice. Please pick either 1 or 2")
