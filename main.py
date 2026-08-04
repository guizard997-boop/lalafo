import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from parser.lalafo import get_lalafo_cars
from database import is_new, save_car
from analyzer import is_good_offer


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


# Вставь сюда свой Telegram ID
YOUR_CHAT_ID = 123456789


async def send_car(car, discount):

    text = f"""
🚗 Найден автомобиль

{car['title']}

💰 Цена:
{car['price']} сом

📉 Ниже рынка:
{discount}%

🔗 Ссылка:
{car['link']}
"""

    await bot.send_message(
        YOUR_CHAT_ID,
        text
    )



async def check_cars():

    while True:

        try:

            cars = await get_lalafo_cars()


            for car in cars:


                if is_new(car["link"]):


                    # Временно пример.
                    # В Блоке 5 заменим на настоящий анализ рынка.

                    market_price = 1500000


                    if is_good_offer(
                        car["price"],
                        market_price
                    ):


                        discount = round(
                            (
                                (market_price - car["price"])
                                /
                                market_price
                            ) * 100,
                            1
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


        except Exception as e:

            print(
                "Ошибка:",
                e
            )


        await asyncio.sleep(30)



async def main():

    asyncio.create_task(
        check_cars()
    )


    await dp.start_polling(
        bot
    )



if __name__ == "__main__":

    asyncio.run(main())