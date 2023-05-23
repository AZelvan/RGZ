from aiogram import Dispatcher
from bot.tools.keyboards import *
from aiogram import types

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(start, commands=['start'])

# dp.register_message_handler(start, commands=['start']) -
# регистрация обработчика сообщений для команды /start. При получении команды /start, будет вызван обработчик start.

async def start(msg: types.Message):
    await msg.answer('Меню бота', reply_markup= menu_inlines())