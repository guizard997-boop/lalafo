def calculate_market_price(cars):

    """
    cars - список цен похожих машин
    """

    if len(cars) == 0:
        return 0


    cars = sorted(cars)


    middle = len(cars) // 2


    return cars[middle]



def discount_percent(price, market_price):

    if market_price == 0:
        return 0


    result = (
        (market_price - price)
        /
        market_price
    ) * 100


    return round(result, 1)



def is_good_offer(price, market_price):

    discount = discount_percent(
        price,
        market_price
    )


    if discount >= 15:
        return True


    return False
