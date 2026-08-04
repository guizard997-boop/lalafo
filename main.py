import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN
from parser.lalafo import get_lalafo_cars
from database import is_new, save_car


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


# ВСТАВЬ СЮДА СВОЙ TELEGRAM ID
YOUR_CHAT_ID = 123456789


async def send_car(car):

    text = f"""
🚗 Найден автомобиль

{car['title']}

🔗 Ссылка:
{car['link']}

📊 Анализ:
Проверка цены выполняется...
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


                    await send_car(car)


                    save_car(
                        car["link"],
                        car["title"],
                        0
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

    asyncio.run(
        main()
    )