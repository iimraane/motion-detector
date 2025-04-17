import logging
import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

TOKEN = "7876431851:AAEUeICZo-Fqdnd0IVVdiA7zAfzNxL2NIAA"


bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_command(message: types.Message):
    chat_id = message.chat.id
    print(f"Chat ID: {chat_id}")
    await message.answer(f"Ton chat id est : {chat_id}")

async def main():
    logging.basicConfig(level=logging.INFO)
    # Démarrer le polling du bot
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
