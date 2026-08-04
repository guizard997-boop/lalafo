import aiohttp
from bs4 import BeautifulSoup


BAD_WORDS = [
    "трактор",
    "экскаватор",
    "кран",
    "погрузчик",
    "бульдозер",
    "спецтехника"
]


async def get_lalafo_cars():

    url = (
        "https://lalafo.kg/"
        "kyrgyzstan/avtomobili"
    )


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


    for item in soup.find_all("a"):

        title = item.text.strip()

        link = item.get("href")


        if not title or not link:
            continue


        if check_car(title):

            cars.append({

                "title": title,

                "link": link,

                "price": 0

            })


    return cars



def check_car(title):

    text = title.lower()


    for word in BAD_WORDS:

        if word in text:

            return False


    return True