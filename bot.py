from aiogram import Bot, Dispatcher, types
from aiogram.utils.executor import start_webhook
import logging
import os

API_TOKEN = os.getenv('API_TOKEN')

WEBHOOK_HOST = 'bottestq-f224cf-219af2-46-8-230-125.traefik.me'
WEBHOOK_PATH = '/webhook/' + API_TOKEN
WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

WEBAPP_HOST = '0.0.0.0'
WEBAPP_PORT = int(os.getenv('PORT', 3000))

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])asyncdefsend_welcome(message: types.Message):
    await message.reply("Hi!\nI'm your Telegram bot!")

@dp.message_handler()asyncdefecho(message: types.Message):
    await message.answer(message.text)

asyncdefon_startup(dp):
    await bot.set_webhook(WEBHOOK_URL)

asyncdefon_shutdown(dp):
    await bot.delete_webhook()

if __name__ == '__main__':
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )
