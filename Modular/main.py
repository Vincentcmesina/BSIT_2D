# ------------------------------------------
# MAIN PROGRAM
# ------------------------------------------

from menu import get_menu, display_menu
from ordering import get_order
from billing import calculate_total, calculate_discount
from reciept import print_receipt


def main():

    # Get menu
    menu = get_menu()

    # Display menu
    display_menu(menu)

    # Ask customer if they want to order
    while True:

        start_order = input(
            "\nWould you like to order? (yes/no): "
        ).lower()

        if start_order in ("yes", "y"):
            break

        elif start_order in ("no", "n"):
            print("\nThank you! Have a great day!")
            return

        else:
            print("Please answer yes or no.")

    # Get orders
    orders = get_order(menu)

    # Calculate subtotal
    subtotal = calculate_total(orders, menu)

    # Calculate discount
    discount, discount_rate = calculate_discount(subtotal)

    # Print receipt
    print_receipt(
        orders,
        menu,
        subtotal,
        discount,
        discount_rate
    )


if __name__ == "__main__":
    main()
