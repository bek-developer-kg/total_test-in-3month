from aiogram import Bot, Dispatcher, Router, types
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import Command
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import F
import asyncio
import random

token = '7584494676:AAGMDXYFipxLpOflTCCKjAmu7n1GrPXahZA'

bot = Bot(token=token)
dp = Dispatcher()

router = Router()
dp.include_router(router)

def get_start_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Игра", callback_data="game")
    builder.button(text="Наши новости", callback_data="news")
    return builder.as_markup()

def get_game_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Камень, ножницы, бумага", callback_data="knb")
    builder.button(text="Рандомайзер", callback_data="randomizer")
    return builder.as_markup()

def get_knb_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="Камень", callback_data="rock")
    builder.button(text="Ножницы", callback_data="scissors")
    builder.button(text="Бумага", callback_data="paper")
    return builder.as_markup()

def get_news_keyboard():
    builder = InlineKeyboardBuilder()
    builder.button(text="О нас", callback_data="about")
    builder.button(text="Адрес", callback_data="address")
    builder.button(text="Наши курсы", callback_data="courses")
    return builder.as_markup()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        "Привет! Я твой бот. Выбери действие:",
        reply_markup=get_start_keyboard()
    )

@router.callback_query(F.data == "game")
async def game_menu(callback: types.CallbackQuery):
    if callback.message.text != "Выберите игру:" or callback.message.reply_markup != get_game_keyboard():
        await callback.message.edit_text(
            "Выберите игру:",
            reply_markup=get_game_keyboard()
        )

@router.callback_query(F.data == "news")
async def news_menu(callback: types.CallbackQuery):
    if callback.message.text != "Выберите информацию:" or callback.message.reply_markup != get_news_keyboard():
        await callback.message.edit_text(
            "Выберите информацию:",
            reply_markup=get_news_keyboard()
        )

@router.callback_query(F.data == "knb")
async def rps_menu(callback: types.CallbackQuery):
    if callback.message.text != "Выберите камень, ножницы или бумагу:" or callback.message.reply_markup != get_knb_keyboard():
        await callback.message.edit_text(
            "Выберите камень, ножницы или бумагу:",
            reply_markup=get_knb_keyboard()
        )

@router.callback_query(F.data.in_({"rock", "scissors", "paper"}))
async def play_knb(callback: types.CallbackQuery):
    bot_choice = random.choice(["Камень", "Ножницы", "Бумага"])
    user_choice_map = {
        "rock": "Камень",
        "scissors": "Ножницы",
        "paper": "Бумага"
    }
    user_choice = user_choice_map[callback.data]

    if user_choice == bot_choice:
        result = "Ничья"
    elif (user_choice == "Камень" and bot_choice == "Ножницы") or \
         (user_choice == "Ножницы" and bot_choice == "Бумага") or \
         (user_choice == "Бумага" and bot_choice == "Камень"):
        result = "Вы победили!"
    else:
        result = "Вы проиграли!"

    if callback.message.text != f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}" or callback.message.reply_markup != get_knb_keyboard():
        await callback.message.edit_text(
            f"Вы выбрали: {user_choice}\nБот выбрал: {bot_choice}\n{result}",
            reply_markup=get_knb_keyboard()
        )

@router.callback_query(F.data == "randomizer")
async def randomizer(callback: types.CallbackQuery):
    result = random.choice(["Вы победили!", "Вы проиграли!", "Ничья"])

    if callback.message.text != result or callback.message.reply_markup != get_game_keyboard():
        await callback.message.edit_text(
            result,
            reply_markup=get_game_keyboard()
        )

@router.callback_query(F.data == "about")
async def about_us(callback: types.CallbackQuery):
    if callback.message.text != "Международная IT-академия Geeks (Гикс) была основана Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018 году" or callback.message.reply_markup != get_news_keyboard():
        await callback.message.edit_text(
            "Международная IT-академия Geeks (Гикс) была основана Fullstack-разработчиком Айдаром Бакировым и Android-разработчиком Нургазы Сулаймановым в 2018 году",
            reply_markup=get_news_keyboard()
        )

@router.callback_query(F.data == "address")
async def address(callback: types.CallbackQuery):
    if callback.message.text != "Наш адрес: ул. Мырзалы Аматова 1Б, БЦ Томирис, цокольный этаж (здание Визион)" or callback.message.reply_markup != get_news_keyboard():
        await callback.message.edit_text(
            "Наш адрес: ул. Мырзалы Аматова 1Б, БЦ Томирис, цокольный этаж (здание Визион)",
            reply_markup=get_news_keyboard()
        )

@router.callback_query(F.data == "courses")
async def courses(callback: types.CallbackQuery):
    if callback.message.text != "Backend-разработчик, Frontend-разработчик, UX/UI-дизайнер. Обучение в месяц 10.000сом" or callback.message.reply_markup != get_news_keyboard():
        await callback.message.edit_text(
            "Backend-разработчик, Frontend-разработчик, UX/UI-дизайнер. Обучение в месяц 10.000сом",
            reply_markup=get_news_keyboard()
        )

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())
