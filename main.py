import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN


bot = Bot(BOT_TOKEN)

dp = Dispatcher()


async def check_cars():

    while True:

        # Здесь позже подключим Lalafo

        print("Проверка объявлений...")

        await asyncio.sleep(30)


async def main():

    asyncio.create_task(check_cars())

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())