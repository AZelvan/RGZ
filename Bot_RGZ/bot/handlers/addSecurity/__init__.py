from aiogram import Dispatcher
from bot.tools.keyboards import *
from aiogram import types
from aiogram.dispatcher import FSMContext
from bot.tools import database
from asyncio import sleep
from aiogram.dispatcher.filters.state import State, StatesGroup

# Dispatcher из модуля aiogram - класс, отвечающий за обработку и маршрутизацию сообщений и событий в боте.
# Различные клавиатуры (InlineKeyboardMarkup, InlineKeyboardButton, и т.д.) из модуля aiogram.types - используются
# для создания и настройки клавиатур для отправки пользователю.
# FSMContext из модуля aiogram.dispatcher - класс, представляющий контекст конечного автомата
# (FSM) для управления состояниями пользователя.
# database из модуля bot.tools - модуль для работы с базой данных.
# sleep из модуля asyncio - функция для приостановки выполнения кода на определенное время.
# State и StatesGroup из модуля aiogram.dispatcher.filters.state - используются для определения состояний в
# конечном автомате (FSM) бота.

class SecurityState(StatesGroup):
    add_security = State()


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(name_security, text='add_security')
    dp.register_message_handler(add_security, state=SecurityState.add_security)

# Функция register_handlers принимает два аргумента: dp (Dispatcher) и state (FSMContext).
# Она используется для регистрации обработчиков в dp, объекте класса Dispatcher из модуля aiogram.
#
# dp.register_callback_query_handler(name_security, text='add_security:') - регистрирует обработчик
# name_security для callback-запросов с текстом 'add_security:'. Это означает, что когда пользователь
# нажимает на кнопку с текстом 'add_security:', будет вызван обработчик name_security.
#
# dp.register_message_handler(add_security, state=fsm.SecurityState.add_security) - регистрирует
# обработчик add_security для сообщений, которые приходят в состоянии fsm.SecurityState.add_security.
# Это означает, что когда пользователь отправляет сообщение в состоянии fsm.SecurityState.add_security,
# будет вызван обработчик add_security.
#
# Оба обработчика связаны с определенными типами событий и состояниями, и при вызове соответствующего
# события или нахождении в нужном состоянии будет выполнен соответствующий обработчик.

async def name_security(callback: types.CallbackQuery, state:FSMContext):
    await callback.bot.send_message(chat_id=callback.from_user.id, text=f'Введите имя ценной бумаги')
    await state.set_state(SecurityState.add_security)

# Функция name_security является асинхронной и принимает два аргумента: callback (CallbackQuery) и state (FSMContext).
# Она используется для обработки callback-запроса и установки состояния FSM (Finite State Machine) на
# SecurityState.add_security.
#
# Внутри функции происходит следующее:
#
# await callback.bot.send_message(chat_id=callback.from_user.id, text=f'Введите имя ценной бумаги') -
# отправляется сообщение пользователю, указанному в callback.from_user.id, с текстом "Введите имя ценной бумаги".
# Это сообщение запрашивает у пользователя ввести имя ценной бумаги.
#
# await state.set_state(SecurityState.add_security) - устанавливается состояние FSM на SecurityState.add_security.
# Это означает, что после отправки сообщения пользователю, бот будет ожидать ввода имени ценной бумаги от пользователя
# и перейдет в состояние SecurityState.add_security.

async def add_security(msg: types.Message, state:FSMContext):
    name = msg.text.upper()

    if database.get_name_security_users(msg.from_user.id,name) == None:

        if database.get_name_security(name) == None:
            database.set_new_security(name)

        database.set_add_user_security(msg.from_user.id,name)
        await msg.answer(f'Ценная бумага {name} добавлена к отслеживаемым')
    else:
        await msg.answer(f'Ценная бумага {name} уже есть в базе')

    await sleep(1)

    await msg.answer('Меню бота', reply_markup=menu_inlines())
    await state.finish()

# Функция add_security является асинхронной и принимает два аргумента: msg (Message) и state (FSMContext).
# Она используется для добавления ценной бумаги к отслеживаемым.
#
# Внутри функции происходит следующее:
#
# name = msg.text.upper() - получение текста сообщения пользователя и преобразование его в верхний регистр.
# Это будет являться именем ценной бумаги, которую пользователь хочет добавить.
#
# if database.get_name_security_users(msg.from_user.id,name) == None: - проверка, что у пользователя
# нет уже добавленной ценной бумаги с таким же именем.
# Функция get_name_security_users из модуля database используется для проверки.
#
# Внутри блока if происходит следующее:
#
# if database.get_name_security(name) == None: - проверка, что ценная бумага с таким именем не существует в
# базе данных. Функция get_name_security из модуля database используется для проверки.
# database.set_new_security(name) - добавление новой ценной бумаги в базу данных.
# Функция set_new_security из модуля database используется для этого.
# database.set_add_user_security(msg.from_user.id,name) - добавление ценной бумаги к отслеживаемым пользователем.
# Функция set_add_user_security из модуля database используется для этого.
# await msg.answer(f'Ценная бумага {name} добавлена к отслеживаемым') - отправка сообщения пользователю о том,
# что ценная бумага успешно добавлена.
# Внутри блока else происходит следующее:
#
# await msg.answer(f'Ценная бумага {name} уже есть в базе') - отправка сообщения пользователю о том, что ценная
# бумага уже присутствует в базе данных.
# await sleep(1) - ожидание 1 секунды.
#
# await msg.answer('Меню бота', reply_markup=menu_inlines()) - отправка сообщения пользователю с меню бота.
# Функция menu_inlines используется для создания соответствующей разметки кнопок.
#
# await state.finish() - завершение FSM-состояния.