import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from parser.lalafo import get_lalafo_cars

from parser.market import get_market_price

from analyzer import is_good_offer, discount_percent

from database import is_new, save_car



bot = Bot(
    BOT_TOKEN
)


dp = Dispatcher()



YOUR_CHAT_ID = 123456789



async def send_car(car, discount):

    text = f"""
🚗 Автомобиль найден

{car['title']}

📉 Ниже рынка:
{discount}%

🔗 {car['link']}
"""


    await bot.send_message(
        YOUR_CHAT_ID,
        text
    )



async def check_cars():

    while True:

        cars = await get_lalafo_cars()


        prices = []


        for car in cars:

            if car["price"]:

                prices.append(
                    car["price"]
                )


        market_price = get_market_price(
            prices
        )


        for car in cars:


            if is_new(
                car["link"]
            ):


                if is_good_offer(
                    car["price"],
                    market_price
                ):


                    discount = discount_percent(
                        car["price"],
                        market_price
                    )


                    await send_car(
                        car,
                        discount
                    )


                    save_car(
                        car["link"],
                        car["title"],
                        car["price"]
                    )


        await asyncio.sleep(
            30
        )



async def main():

    asyncio.create_task(
        check_cars()
    )


    await dp.start_polling(
        bot
    )



if __name__ == "__main__":

    asyncio.run(main())