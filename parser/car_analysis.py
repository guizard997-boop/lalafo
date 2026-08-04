from statistics import median


def get_car_key(title):

    """
    Получаем ключ машины:
    марка + модель + год
    """

    words = title.lower().split()

    return " ".join(words[:3])



def find_similar_cars(target, cars):

    result = []

    target_key = get_car_key(
        target["title"]
    )


    for car in cars:

        if get_car_key(car["title"]) == target_key:

            if car["price"] > 0:
                result.append(
                    car["price"]
                )


    return result



def calculate_market_price(prices):

    if len(prices) < 5:
        return 0


    return median(prices)



def discount(price, market):

    if market == 0:
        return 0


    return round(
        ((market-price)/market)*100,
        1
    )