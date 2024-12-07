from aiogram import Bot, Dispatcher, types, F
from aiogram.filters import Command, CommandStart
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from aiogram.utils import executor
import asyncio, logging
import random
from config import token


logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher(Bot)

start_menu = ReplyKeyboardMarkup(resize_keyboard=True)
start_menu.add = (KeyboardButton("Игра"), KeyboardButton ("Наши новости"))

game_menu = ReplyKeyboardMarkup(resize_keyboard=True)
game_menu.add = (KeyboardButton("Камень, Ножницы, Бумага"), KeyboardButton("Рандомайзер"))

knb_menu = ReplyKeyboardMarkup(resize_keyboard=True)
knb_menu.add = (KeyboardButton("Камень"), KeyboardButton("Ножница"), KeyboardButton("Бумага"))

news_menu = ReplyKeyboardMarkup(resize_keyboard=True)
news_menu.add = (KeyboardButton("О нас"), KeyboardButton("Адрес"), KeyboardButton("Наши курсы"))


selection = ['Камень', 'Ножница', 'Бумага']

user_choice = message.text
bot_choice = random.choice(selection)

@dp.message(Command("start"))
async def start(message:types.Message):
    await message.answer("Добро пожаловать! Выберите одну из опций:", reply_markup=start_menu)


@dp.message(lambda message: message.text == "Игра")
async def start_game(message: types.Message):
    await message.answer("Выберите игру:", reply_markup=game_menu)


dp.message(lambda message: message.text == "Наши новости")
async def news(message: types.Message):
    await message.answer("Выберите раздел новостей:", reply_markup=news_menu)


@dp.message(lambda message: message.text == "Камен, ножницы, бумага")
async def rock_paper_scissors(message: types.Message):
    await message.answer("Выберите камень, ножницы или бумагу:", reply_markup=knb_menu)


@dp.message(lambda message: message.text == "Рандомайзер")
async def randomizer(message: types.Message):
    result = random.choice(["Вы победили!", "Вы проиграли!", "Ничья"])
    await message.answer(result)


@dp.message(lambda message: message.text in selection)
async def play_knb(message: types.Message):
    user_choice = message.text
    bot_choice = random.choice(selection)

if user_choice == bot_choice:
        result = "Ничья!"
elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "Вы победили!"
else:
        result = "Вы проиграли!"

await message.answer(f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}")
