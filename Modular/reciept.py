# ------------------------------------------
# RECEIPT MODULE
# ------------------------------------------

def print_receipt(
    orders,
    menu,
    subtotal,
    discount,
    discount_rate
):
    """Print the customer's receipt."""

    final_total = subtotal - discount

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

    for item, quantity in orders.items():

        price = menu[item]
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
        f" ₱{subtotal:>10.2f}"
    )

    if discount > 0:

        percentage = int(discount_rate * 100)

        print(
            f"{'DISCOUNT (' + str(percentage) + '%):':<40}"
            f" -₱{discount:>9.2f}"
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
