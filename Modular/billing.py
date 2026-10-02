# ------------------------------------------
# BILLING MODULE
# ------------------------------------------

def calculate_total(orders, menu):
    """Calculate the subtotal."""

    subtotal = 0

    for item, quantity in orders.items():
        subtotal += menu[item] * quantity

    return subtotal


def calculate_discount(subtotal):
    """
    Calculate discount based on subtotal.

    ₱500 or more = 10%
    ₱300 - ₱499.99 = 5%
    Below ₱300 = no discount
    """

    if subtotal >= 500:
        discount_rate = 0.10

    elif subtotal >= 300:
        discount_rate = 0.05

    else:
        discount_rate = 0

    discount = subtotal * discount_rate

    return discount, discount_rate


def calculate_final_total(subtotal, discount):
    """Calculate the final amount to pay."""

    return subtotal - discount
