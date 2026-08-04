import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from parser.lalafo import get_lalafo_cars

from parser.car_analysis import (
    find_similar_cars,
    calculate_market_price,
    discount
)

from database import (
    is_new,
    save_car
)


bot = Bot(
    token=BOT_TOKEN
)

dp = Dispatcher()


# ВСТАВЬ СЮДА СВОЙ TELEGRAM ID
YOUR_CHAT_ID = 123456789



async def send_car(car, discount_value):

    text = f"""
🚗 {car.get('title', 'Без названия')}

💰 Цена:
{car.get('price', 0)} сом

📉 Ниже рынка:
{discount_value}%

🛃 Растаможка:
{"✅ Да" if car.get('customs') else "❓ Не указано"}

🔗 Ссылка:
{car.get('link', '')}
"""


    try:

        if car.get("photo"):

            await bot.send_photo(
                chat_id=YOUR_CHAT_ID,
                photo=car["photo"],
                caption=text
            )

        else:

            await bot.send_message(
                chat_id=YOUR_CHAT_ID,
                text=text
            )


    except Exception as e:

        print(
            "Ошибка отправки:",
            e
        )



async def check_cars():

    while True:

        try:

            cars = await get_lalafo_cars()


            for car in cars:


                if not is_new(
                    car["link"]
                ):
                    continue



                similar_prices = find_similar_cars(
                    car,
                    cars
                )


                market_price = calculate_market_price(
                    similar_prices
                )


                discount_value = discount(
                    car["price"],
                    market_price
                )



                if discount_value >= 15:


                    await send_car(
                        car,
                        discount_value
                    )


                    save_car(
                        car["link"],
                        car["title"],
                        car["price"]
                    )


        except Exception as e:

            print(
                "Ошибка проверки:",
                e
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

    asyncio.run(
        main()
    )