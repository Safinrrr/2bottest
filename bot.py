from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
import logging

API_TOKEN = '7354136013:AAEmvylGHcdVc0FVVa7fBvuV62d5f0qyRto'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])asyncdefsend_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your Telegram bot!")

@dp.message_handler()asyncdefecho(message: types.Message):
    await message.answer(message.text)

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)
