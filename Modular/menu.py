# ------------------------------------------
# MENU MODULE
# ------------------------------------------

def get_menu():
    """Return the restaurant menu."""

    menu = {
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

    return menu


def display_menu(menu):
    """Display the complete menu."""

    print("\n" + "=" * 45)
    print("           JOLLIBEE EXPRESS")
    print("              FULL MENU")
    print("=" * 45)

    for item, price in menu.items():
        print(f"{item:<30} ₱{price:.2f}")

    print("=" * 45)
