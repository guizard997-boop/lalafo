import aiohttp
from bs4 import BeautifulSoup


BAD_WORDS = [
    "экскаватор",
    "трактор",
    "погрузчик",
    "кран",
    "бульдозер",
    "спецтехника",
    "самосвал"
]


GOOD_WORDS = [
    "растаможен",
    "растаможена",
    "растаможка",
    "кыргызстан",
    "кг"
]


async def get_lalafo_cars():

    url = "https://lalafo.kg/kyrgyzstan/avtomobili"

    headers = {
        "User-Agent":
        "Mozilla/5.0"
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


    # Временно пример структуры.
    # После проверки сайта подставим реальные классы Lalafo.

    for item in soup.find_all("a"):

        title = item.text.strip()

        link = item.get("href")


        if not title or not link:
            continue


        if is_car(title):

            cars.append({

                "title": title,

                "link": link

            })


    return cars



def is_car(title):

    text = title.lower()


    # убираем спецтехнику

    for word in BAD_WORDS:

        if word in text:

            return False



    return True



def has_kg_customs(text):

    text = text.lower()


    for word in GOOD_WORDS:

        if word in text:

            return True


    return False