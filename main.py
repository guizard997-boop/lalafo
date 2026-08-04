import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from parser.lalafo import get_lalafo_cars

bot = Bot(BOT_TOKEN)

dp = Dispatcher()


async def check_cars():

    while True:

        cars = await get_lalafo_cars()

        for car in cars:
            print(
                car["title"],
                car["link"]
            )

        await asyncio.sleep(30)

async def main():

    asyncio.create_task(check_cars())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())