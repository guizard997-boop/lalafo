from statistics import median



def get_market_price(prices):

    if len(prices) < 5:
        return 0

    return median(prices)