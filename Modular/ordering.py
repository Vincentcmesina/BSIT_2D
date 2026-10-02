# ------------------------------------------
# ORDERING MODULE
# ------------------------------------------

def get_order(menu):
    """Get customer orders."""

    orders = {}

    while True:
        print("\nAvailable Items:")

        menu_items = list(menu.keys())

        for number, item in enumerate(menu_items, start=1):
            print(f"{number}. {item} - ₱{menu[item]:.2f}")

        # Select item
        while True:
            choice = input("\nEnter the item number: ")

            try:
                choice = int(choice)

                if 1 <= choice <= len(menu_items):
                    selected_item = menu_items[choice - 1]
                    break
                else:
                    print("Invalid item number. Please try again.")

            except ValueError:
                print("Please enter a valid number.")

        # Enter quantity
        while True:
            quantity = input("Enter quantity: ")

            try:
                quantity = int(quantity)

                if quantity > 0:
                    break
                else:
                    print("Quantity must be at least 1.")

            except ValueError:
                print("Please enter a whole number.")

        # Add order
        if selected_item in orders:
            orders[selected_item] += quantity
        else:
            orders[selected_item] = quantity

        print(f"\nAdded: {quantity} x {selected_item}")

        # Continue ordering?
        while True:
            another = input(
                "\nWould you like to order another item? (yes/no): "
            ).lower()

            if another in ("yes", "y"):
                break

            elif another in ("no", "n"):
                return orders

            else:
                print("Please answer yes or no.")
