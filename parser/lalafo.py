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


    links = soup.find_all(
        "a",
        href=True
    )


    for item in links:

        title = item.get_text(
            " ",
            strip=True
        )

        link = item["href"]


        if not is_car(title):
            continue


        price = extract_price(
            title
        )


        if price == 0:
            continue


        if not link.startswith("http"):
            link = (
                "https://lalafo.kg"
                +
                link
            )


        cars.append({

            "title": title,

            "price": price,

            "link": link,

            "photo": None

        })


    return cars



def is_car(title):

    text = title.lower()


    for word in BAD_WORDS:

        if word in text:

            return False


    return True



def extract_price(text):

    numbers = re.findall(
        r'\d[\d\s]*',
        text
    )


    if not numbers:
        return 0


    price = (
        numbers[0]
        .replace(" ", "")
    )


    try:

        return int(price)

    except:

        return 0 