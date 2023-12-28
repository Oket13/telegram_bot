import asyncio
import logging
from translate import Translator
from aiogram import Bot, Dispatcher, types
from aiogram.enums import ParseMode
from aiogram.filters import Command

logging.basicConfig(level=logging.INFO)

TOKEN = '6975211314:AAFdAoQfhjZ7tT73_zTzShQ0RK2RIde6IxE'
dp = Dispatcher()

ua_letters = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"
en_letters = "abcdefghijklmnopqrstuvwxyz"


@dp.message(Command('start'))
async def send_welcome(message: types.Message):
    await message.send("Привіт, я ехо бот перекладач")


@dp.message()
async def echo(message: types.Message):
    text = message.text
    if text[0].lower() in ua_letters:
        translator = Translator(from_lang="uk", to_lang="english")
    elif text[0].lower() in en_letters:
        translator = Translator(from_lang="english", to_lang="uk")
    else:
        await message.answer('Я тебе не розумію')
        return
    translation = translator.translate(text)
    await message.answer(translation)


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
