import asyncio
from aiogram import Bot, Dispatcher

from bot.handlers import router


async def main():
    bot = Bot(token='8010896995:AAED1XrRKfcLiZ2n0VV5Q-sTh_-6-mFpuTI')
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
