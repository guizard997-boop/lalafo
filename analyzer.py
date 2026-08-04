def calculate_discount(price, market_price):

    discount = ((market_price - price) / market_price) * 100

    return round(discount, 1)


def is_good_deal(price, market_price):

    discount = calculate_discount(
        price,
        market_price
    )

    if discount >= 15:
        return True

    return False