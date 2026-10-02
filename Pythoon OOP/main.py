# ==========================================
# JOLLIBEE EXPRESS - OOP VERSION
# ==========================================


# ------------------------------------------
# CLASS: Menu
# ------------------------------------------

class Menu:

    def __init__(self):
        self.items = {
            "Chickenjoy": 89.00,
            "Jolly Spaghetti": 65.00,
            "Yumburger": 45.00,
            "Burger Steak": 75.00,
            "Chicken Sandwich": 85.00,
            "French Fries": 50.00,
            "Peach Mango Pie": 40.00,
            "Chocolate Sundae": 45.00,
            "Coke": 35.00,
            "Iced Tea": 40.00
        }


    def display(self):
        """Display the complete menu."""

        print("\n" + "=" * 45)
        print("           JOLLIBEE EXPRESS")
        print("              FULL MENU")
        print("=" * 45)

        for item, price in self.items.items():
            print(f"{item:<30} ₱{price:.2f}")

        print("=" * 45)


    def get_items(self):
        """Return menu items."""

        return list(self.items.keys())


    def get_price(self, item):
        """Return the price of an item."""

        return self.items[item]


# ------------------------------------------
# CLASS: Order
# ------------------------------------------

class Order:

    def __init__(self):
        self.items = {}


    def add_item(self, item, quantity):
        """Add an item to the order."""

        if item in self.items:
            self.items[item] += quantity

        else:
            self.items[item] = quantity


    def calculate_subtotal(self, menu):
        """Calculate the subtotal."""

        subtotal = 0

        for item, quantity in self.items.items():
            price = menu.get_price(item)
            subtotal += price * quantity

        return subtotal


# ------------------------------------------
# CLASS: Customer
# ------------------------------------------

class Customer:

    def __init__(self):
        self.order = Order()


    def place_order(self, menu):
        """Allow the customer to place an order."""

        while True:

            print("\nAvailable Items:")

            menu_items = menu.get_items()

            for number, item in enumerate(menu_items, start=1):
                price = menu.get_price(item)

                print(
                    f"{number}. "
                    f"{item} - ₱{price:.2f}"
                )

            # Select item
            while True:

                choice = input(
                    "\nEnter the item number: "
                )

                try:

                    choice = int(choice)

                    if 1 <= choice <= len(menu_items):
                        selected_item = menu_items[
                            choice - 1
                        ]
                        break

                    else:
                        print(
                            "Invalid item number. "
                            "Please try again."
                        )

                except ValueError:

                    print(
                        "Please enter a valid number."
                    )

            # Quantity
            while True:

                quantity = input(
                    "Enter quantity: "
                )

                try:

                    quantity = int(quantity)

                    if quantity > 0:
                        break

                    else:
                        print(
                            "Quantity must be "
                            "at least 1."
                        )

                except ValueError:

                    print(
                        "Please enter a whole number."
                    )

            # Add item
            self.order.add_item(
                selected_item,
                quantity
            )

            print(
                f"\nAdded: {quantity} "
                f"x {selected_item}"
            )

            # Another item?
            while True:

                another = input(
                    "\nWould you like to order "
                    "another item? (yes/no): "
                ).lower()

                if another in ("yes", "y"):
                    break

                elif another in ("no", "n"):
                    return

                else:
                    print(
                        "Please answer yes or no."
                    )


# ------------------------------------------
# CLASS: Discount
# ------------------------------------------

class Discount:

    @staticmethod
    def calculate(subtotal):
        """
        Calculate discount.

        ₱500 or more = 10%
        ₱300 - ₱499.99 = 5%
        Below ₱300 = no discount
        """

        if subtotal >= 500:
            rate = 0.10

        elif subtotal >= 300:
            rate = 0.05

        else:
            rate = 0

        discount = subtotal * rate

        return discount, rate


# ------------------------------------------
# CLASS: Receipt
# ------------------------------------------

class Receipt:

    def __init__(
        self,
        order,
        menu,
        subtotal,
        discount,
        discount_rate
    ):

        self.order = order
        self.menu = menu
        self.subtotal = subtotal
        self.discount = discount
        self.discount_rate = discount_rate


    def print_receipt(self):
        """Display the official receipt."""

        final_total = (
            self.subtotal - self.discount
        )

        print("\n")
        print("=" * 55)
        print("                 JOLLIBEE EXPRESS")
        print("                  OFFICIAL RECEIPT")
        print("=" * 55)

        print(
            f"{'ITEM':<25}"
            f"{'QTY':>5}"
            f"{'PRICE':>10}"
            f"{'TOTAL':>12}"
        )

        print("-" * 55)

        for item, quantity in self.order.items.items():

            price = self.menu.get_price(item)

            item_total = price * quantity

            print(
                f"{item:<25}"
                f"{quantity:>5}"
                f"₱{price:>9.2f}"
                f"₱{item_total:>11.2f}"
            )

        print("-" * 55)

        print(
            f"{'SUBTOTAL:':<40}"
            f" ₱{self.subtotal:>10.2f}"
        )

        if self.discount > 0:

            percentage = int(
                self.discount_rate * 100
            )

            print(
                f"{'DISCOUNT (' + str(percentage) + '%):':<40}"
                f" -₱{self.discount:>9.2f}"
            )

        else:

            print(
                f"{'DISCOUNT:':<40}"
                f" ₱0.00"
            )

        print("-" * 55)

        print(
            f"{'TOTAL:':<40}"
            f" ₱{final_total:>10.2f}"
        )

        print("=" * 55)
        print("          Thank you for ordering!")
        print("             Please come again!")
        print("=" * 55)


# ------------------------------------------
# CLASS: JollibeeExpress
# ------------------------------------------

class JollibeeExpress:

    def __init__(self):

        self.menu = Menu()


    def start(self):
        """Start the restaurant ordering system."""

        # Display menu
        self.menu.display()

        # Ask if customer wants to order
        while True:

            start_order = input(
                "\nWould you like to order? (yes/no): "
            ).lower()

            if start_order in ("yes", "y"):
                break

            elif start_order in ("no", "n"):

                print(
                    "\nThank you! Have a great day!"
                )

                return

            else:

                print(
                    "Please answer yes or no."
                )

        # Create customer
        customer = Customer()

        # Place order
        customer.place_order(self.menu)

        # Calculate subtotal
        subtotal = customer.order.calculate_subtotal(
            self.menu
        )

        # Calculate discount
        discount, discount_rate = (
            Discount.calculate(subtotal)
        )

        # Create receipt
        receipt = Receipt(
            customer.order,
            self.menu,
            subtotal,
            discount,
            discount_rate
        )

        # Print receipt
        receipt.print_receipt()


# ------------------------------------------
# RUN PROGRAM
# ------------------------------------------

if __name__ == "__main__":

    restaurant = JollibeeExpress()
    restaurant.start()
