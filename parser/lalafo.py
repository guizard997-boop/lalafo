import aiohttp
from bs4 import BeautifulSoup
import re


BAD_WORDS = [
    "трактор",
    "экскаватор",
    "кран",
    "погрузчик",
    "бульдозер",
    "спецтехника",
    "самосвал"
]


CUSTOMS_WORDS = [
    "растаможен",
    "растаможена",
    "растаможка",
    "кыргызстан",
    "кг"
]


async def get_lalafo_cars():

    url = "https://lalafo.kg/kyrgyzstan/avtomobili"

    headers = {
        "User-Agent": "Mozilla/5.0"
    }


    async with aiohttp.ClientSession() as session:

        async with session.get(
            url,
            headers=headers
        ) as response:

            html = await response.text()


    soup = BeautifulSoup(
        html,
        "html.parser"
    )


    cars = []


    for item in soup.find_all("a"):

        title = item.text.strip()

        link = item.get("href")


        if not title or not link:
            continue


        price = get_price(title)


        if is_car(title):

            cars.append({

                "title": title,

                "link": link,

                "price": price

            })


    return cars



def is_car(text):

    text = text.lower()


    for word in BAD_WORDS:

        if word in text:
            return False


    return True



def has_customs(text):

    text = text.lower()


    for word in CUSTOMS_WORDS:

        if word in text:
            return True


    return False



def get_price(text):

    numbers = re.findall(
        r'\d+',
        text
    )


    if not numbers:
        return 0


    price = int(
        numbers[0]
    )


    return price