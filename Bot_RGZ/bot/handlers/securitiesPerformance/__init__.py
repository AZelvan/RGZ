from aiogram import Dispatcher
from bot.tools.keyboards import *
from aiogram import types
from bot.tools import database,task


def register_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(name_security,text='indicators_security')
    dp.register_callback_query_handler(back_menu, text='back')
# dp.register_callback_query_handler(name_security, text='indicators_security') - регистрация обработчика для
# callback-запросов с текстом 'indicators_security'. Когда пользователь нажимает кнопку с таким текстом,
# будет вызван обработчик name_security.
#
# dp.register_callback_query_handler(back_menu, Text(contains='back')) - регистрация обработчика для callback-запросов,
# содержащих текст 'back'. Когда пользователь нажимает кнопку с текстом, содержащим 'back', будет вызван обработчик back_menu
#


async def name_security(callback: types.CallbackQuery):
    securities = database.get_security(callback.from_user.id)
    if securities!= None:
        message = "Список ценных бумаг :\n"
        for security in securities:
            price = database.get_median_price(security)
            if price != None:
                message += f"{security} - {price}\n"
            else:
                if task.get_daily_closing_prices(security)!=None:
                    price = task.get_daily_closing_prices(security)
                    message += f"{security} - {price}\n"
                    database.set_add_security(security, price)
                else:
                    message += f"{security} -  не обслуживается \n"

        await callback.bot.send_message(chat_id=callback.from_user.id,text=f'{message} ',reply_markup=back())
    else:
        await callback.bot.send_message(chat_id=callback.from_user.id,text=f'У вас пока нечего отслеживать, вернитесь в меню и добавьте ценные бумаги ',reply_markup=back())


# Функция name_security является обработчиком для callback-запросов и принимает объект callback класса
# types.CallbackQuery.
#
# Внутри функции происходит следующая логика:
#
# Получение списка ценных бумаг пользователя с помощью функции get_security из модуля database.
#
# Если список ценных бумаг не является пустым (securities != None), происходит формирование сообщения с информацией о
# каждой ценной бумаге и их текущей цене. Если цена доступна в базе данных (price != None),
# она добавляется в сообщение. Если цена отсутствует в базе данных, вызывается функция get_daily_closing_prices из
# модуля task для получения текущей цены. Если текущая цена доступна (task.get_daily_closing_prices(price) != None),
# она добавляется в сообщение и сохраняется в базе данных с помощью функции set_add_security из модуля database.
# Если текущая цена недоступна, выводится сообщение об этом.
#
# Отправка сформированного сообщения пользователю с помощью метода send_message объекта bot из объекта callback.
# Также добавляется клавиатура "Назад" с помощью reply_markup=back().
#
# Если список ценных бумаг пользователя является пустым (securities == None), отправляется сообщение о том,
# что у пользователя пока нет отслеживаемых ценных бумаг, и предлагается вернуться в меню с помощью клавиатуры
# "Назад".
#
# Обработчик name_security должен быть зарегистрирован с помощью метода
# dp.register_callback_query_handler(name_security, text='indicators_security') в функции
# register_handlers для обработки callback-запросов с текстом 'indicators_security'.

async def back_menu(callback: types.CallbackQuery):
    await callback.bot.send_message(chat_id=callback.from_user.id,text=f'Меню бота', reply_markup =menu_inlines())

#
# Функция back_menu является обработчиком для callback-запросов и принимает объект callback класса types.CallbackQuery.
#
# Внутри функции происходит следующая логика:
#
# Отправляется сообщение пользователю с текстом "Меню бота" и клавиатурой,
# сформированной с помощью функции menu_inlines() из модуля inlines. Сообщение отправляется с помощью
# метода send_message объекта bot из объекта callback.
# Обработчик back_menu должен быть зарегистрирован с помощью метода
# dp.register_callback_query_handler(back_menu, Text(contains='back')) в
# функции register_handlers для обработки callback-запросов, текст которых содержит строку 'back'.