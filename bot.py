import asyncio
import json
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Update, Message
from handlers import help_handler


async def main(update):
    bot: Bot = Bot(token=os.environ.get('TOKEN'))
    dp: Dispatcher = Dispatcher()

    @dp.message(CommandStart())
    async def process_start_command(message: Message):
        await message.answer(text='Привет!')

    dp.include_router(help_handler.router)

    await dp.feed_update(bot=bot, update=update)


def starting_point(event, _):
    update = Update.parse_obj(json.loads(event['body']))
    asyncio.run(main(update))
    return {
        'statusCode': 200,
        'body': '!',
    }
