def discount_percent(price, market_price):

    if market_price == 0:
        return 0

    discount = (
        (market_price - price)
        /
        market_price
    ) * 100

    return round(discount, 1)



def is_good_offer(price, market_price):

    return discount_percent(
        price,
        market_price
    ) >= 15
  