import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
import os
from crud_functions import *
from dotenv import load_dotenv

load_dotenv()
api = os.getenv('BOT1_TOKEN')
bot = Bot(token=api)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button1 = KeyboardButton(text='Информация')
button2 = InlineKeyboardButton(text='Купить')
button3 = InlineKeyboardButton(text='Регистрация')
kb.add(button, button1)
kb.add(button2, button3)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
button1 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(button, button1)

ikb2 = InlineKeyboardMarkup(resize_keyboard=True)
button = InlineKeyboardButton(text='Product1', callback_data='product_buying')
button1 = InlineKeyboardButton(text='Product2', callback_data='product_buying')
button2 = InlineKeyboardButton(text='Product3', callback_data='product_buying')
button3 = InlineKeyboardButton(text='Product4', callback_data='product_buying')
ikb2.add(button, button1, button2, button3)


class UserState(StatesGroup):
    growth = State()
    age = State()
    weight = State()


class RegistrationState(StatesGroup):
    username = State()
    email = State()
    age = State()
    balance = 1000


@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию', reply_markup=ikb)


@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.answer('Для мужчин: 10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')
    await call.answer()


@dp.callback_query_handler(text='calories')
async def set_age(call):
    await call.message.answer('Введите свой возраст:')
    await call.answer()
    await UserState.age.set()


@dp.message_handler(state=UserState.age)
async def set_growth(message, state):
    try:
        await state.update_data(age=int(message.text))
        await UserState.growth.set()
        await message.answer('Введите свой рост:')
    except ValueError:
        await message.answer('Введен неправильный тип данных')


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    try:
        await state.update_data(growth=int(message.text))
        await UserState.weight.set()
        await message.answer('Введите свой вес:')
    except ValueError:
        await message.answer('Введен неправильный тип данных')


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    try:
        await state.update_data(weight=int(message.text))
        data = await state.get_data()
        result = 10 * float(data['weight']) + 6.25 * float(data['growth']) - 5 * float(data['age']) + 5
        await message.answer(f'Ваша суточная норма: {result} ккал')
    except ValueError:
        await message.answer('Ошибка данных, пробуем снова')
    finally:
        await state.finish()


@dp.message_handler(commands='start')
async def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.', reply_markup=kb)


@dp.message_handler(text='Информация')
async def info(message):
    await message.answer('Этот бот считает суточную норму каллорий по введенным параметрам', reply_markup=kb)


@dp.message_handler(text='Купить')
async def get_buying_list(message):
    products = get_all_products()
    for product in products:
        await message.answer(f'Название: {product[1]} | Описание: {product[2]} | Цена: {product[3]}')
        with open(f'{product[0]}.jpg', 'rb') as img:
            await message.answer_photo(img)
    await message.answer('Выберите продукт для покупки: ', reply_markup=ikb2)


@dp.callback_query_handler(text='product_buying')
async def send_confirm_message(call):
    await call.message.answer('Вы успешно приобрели продукт!')
    await call.answer()


@dp.message_handler(text='Регистрация')
async def sign_up(message):
    await message.answer('Введите имя пользователя (только латинский алфавит):')
    await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.username)
async def set_username(message, state):
    if not is_included(message.text):
        await state.update_data(username=message.text)
        await message.answer('Введите свой email:')
        await RegistrationState.email.set()
    else:
        await message.answer('Пользователь существует, введите другое имя')
        await RegistrationState.username.set()


@dp.message_handler(state=RegistrationState.email)
async def set_email(message, state):
    await state.update_data(email=message.text)
    await message.answer('Введите свой возраст:')
    await RegistrationState.age.set()


@dp.message_handler(state=RegistrationState.age)
async def set_age(message, state):
    await state.update_data(age=message.text)
    reg = await state.get_data()
    add_user(**reg)
    await state.finish()
    await message.answer('', eply_markup=kb)


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
