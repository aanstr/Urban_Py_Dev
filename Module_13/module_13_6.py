import asyncio
from aiogram import Bot, Dispatcher, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup
from Keys.telegtam_tokens import Urban_module13

bot = Bot(token=Urban_module13)
dp = Dispatcher(bot, storage=MemoryStorage())

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text='Рассчитать')
button1 = KeyboardButton(text='Информация')
kb.add(button, button1)

ikb = InlineKeyboardMarkup(resize_keyboard=True)
ibatton = InlineKeyboardButton(text='Рассчитать норму калорий', callback_data='calories')
ibatton1 = InlineKeyboardButton(text='Формулы расчёта', callback_data='formulas')
ikb.add(ibatton, ibatton1)


class UserState(StatesGroup):
    growth = State()
    age = State()
    weight = State()


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


@dp.message_handler()
async def all_messages(message):
    await message.answer('Введите команду /start, чтобы начать общение.')


if name == 'main':
    executor.start_polling(dp, skip_updates=True)