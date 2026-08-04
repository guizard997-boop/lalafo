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


    for item in soup.find_all(
        "a",
        href=True
    ):

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


        customs = check_customs(
            title
        )


        photo = get_photo(
            item
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

            "photo": photo,

            "customs": customs

        })


    return cars



def is_car(title):

    text = title.lower()


    for word in BAD_WORDS:

        if word in text:

            return False


    return True



def check_customs(text):

    text = text.lower()


    for word in CUSTOMS_WORDS:

        if word in text:

            return True


    return False



def extract_price(text):

    numbers = re.findall(
        r'\d[\d\s]*',
        text
    )


    if not numbers:

        return 0


    try:

        return int(
            numbers[0]
            .replace(" ", "")
        )

    except:

        return 0



def get_photo(item):

    image = item.find(
        "img"
    )


    if image:

        return image.get(
            "src"
        )


    return None